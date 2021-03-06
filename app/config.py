""""""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STOP_WORDS_DIR_ENG = os.path.join(BASE_DIR, 'StopWords.txt')
STOP_WORDS_DIR_RU = os.path.join(BASE_DIR, 'StopWords_Ru.txt')


class Config(object):
    """"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_VALIDATE = True
    ERROR_404_HELP = False
