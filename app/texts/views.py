""""""
from typing import List, Dict
from datetime import datetime
from functools import reduce

from pymystem3 import Mystem
import RAKE
from flask_login import current_user
from langdetect import detect

from app.database import db
from app.exceptions import NotFoundError, UnauthorizedError
from app.models import Text
from app.config import STOP_WORDS_DIR_ENG, STOP_WORDS_DIR_RU


RU_STOP_WORDS_DIR = '/'


def get_texts(query_params: Dict) -> Dict[str, List[Text]]:
    """Get all texts"""

    _check_anonymity()
    texts = _filters(query_params)

    return {'texts': texts}


def add_text(payload: Dict) -> Text:
    """Add new text"""

    _check_anonymity()
    tags_string = ','.join(get_tags(payload['text']))

    new_text = Text(text=payload['text'],
                    creation_dt=datetime.now(),
                    tags=tags_string,
                    user_id=current_user.id)

    db.session.add(new_text)
    db.session.commit()
    print('id:', new_text.id)

    return new_text


def get_text(text_id: int) -> Text:
    """Get text by id"""

    _check_anonymity()
    text = db.session.query(Text).filter(Text.id == text_id).first()

    return text


def update_text(text_id: int, payload: Dict) -> None:
    """Update existing text"""

    _check_anonymity()
    query = db.session.query(Text).filter(Text.id == text_id)

    try:
        new_tags_string = ''.join(get_tags(payload['text']))
        new_data = {'text': payload['text'],
                    'tags': new_tags_string,
                    'last_update_dt': datetime.now()}
        query.update(new_data)
        db.session.commit()
    except KeyError:
        pass


def delete_text(text_id: int) -> None:
    """Delete text"""

    _check_anonymity()
    text = db.session.query(Text).filter(Text.id == text_id).first()

    db.session.delete(text)
    db.session.commit()


def check_text_existing(text_id: int) -> None:
    """Check text for existing

    :raise NotFoundError: Raises if text not found in db
    """

    text = db.session.query(Text).filter(Text.id == text_id).first()

    if not text or text.owner != current_user:
        raise NotFoundError(f'texts/{text_id}')


def get_tags(text: str) -> List[str]:
    """Get text key words"""
    language = detect(text)
    original_text = text
    normalize_text = None
    keywords_dict = None
    rake_obj = None

    if language == 'ru':
        rake_obj = RAKE.Rake(STOP_WORDS_DIR_RU)
        m = Mystem()
        normalize_text = ''.join(m.lemmatize(original_text))

    if language == 'en':
        rake_obj = RAKE.Rake(STOP_WORDS_DIR_ENG)

    if rake_obj is not None:
        keywords_dict = rake_obj.run(normalize_text, maxWords=2, minCharacters=2)
    keywords = []
    if keywords_dict:
        mean_rate = reduce(
            lambda item1, item2: item1 + item2[1], keywords_dict, 0
        ) / len(keywords_dict)

        keywords = [item[0] for item in keywords_dict if item[1] >= mean_rate]

    return keywords


def _filters(params: Dict) -> List[Text]:
    """Filter texts by query params"""

    query = db.session.query(Text)

    if params['creationDateFrom']:
        query = query.filter(Text.creation_dt >= params['creationDateFrom'])

    if params['creationDateTo']:
        query = query.filter(Text.creation_dt <= params['creationDateTo'])

    if params['lastUpdateDateFrom']:
        query = query.filter(Text.last_update_dt >= params['lastUpdateDateFrom'])

    if params['lastUpdateDateTo']:
        query = query.filter(Text.last_update_dt <= params['lastUpdateDateTo'])

    texts = query.all()
    texts_copy = texts.copy()

    for text in texts_copy:
        if text.owner.username != current_user.username:
            texts.remove(text)

    return texts


def _check_anonymity():
    """Check that current user is not anonymous"""

    if current_user.is_anonymous:
        raise UnauthorizedError('Please Log In')
