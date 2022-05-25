import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676fde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'The Blackthorn'
    MAIL_PASSWORD = '15gbstorage2'
    UPLOAD_FOLDER = '/home/savit/Dashboard/Orthrus/dataset/my_contracts'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
