import os

class Config:
    SECRET_KEY = 'thisissecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False' #to suppress the warning
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('GMAIL_DEV')
    MAIL_PASSWORD = os.environ.get('GMAIL_DEV_PASS')
