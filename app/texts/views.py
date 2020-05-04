""""""
from typing import List, Dict

from app.database import db
from app.exceptions import NotFoundError
from app.models import Text


def get_texts() -> Dict[str, List[Text]]:
    """Get all texts"""

    pass


def add_text() -> Text:
    """Add new text"""

    pass


def get_text(text_id: int) -> Text:
    """Get text by id"""

    pass


def update_text(text_id: int) -> None:
    """Update existing text"""

    pass


def delete_text(text_id: int) -> None:
    """Delete text"""

    pass


def check_text_existing(text_id: int) -> None:
    """Check text for existing

    :raise NotFoundError: Raises if text not found in db
    """
    pass


def _tags_cloud(text: str) -> List[str]:
    """"""

    pass


def _add_tags(tags: List[str]) -> None:
    """"""

    pass
