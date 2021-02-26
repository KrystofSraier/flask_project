import os

SECRET_KEY = b'\x8eJ|P7\x8c\xe6X\xb3\x9c\xaf\x17C\xbaz\x17\xbb\xc81`_\xe3\xac\xc2'
USERNAME = "admin"
PASSWORD = "admin"

DEBUG = True
# DATABASE = "/vagrant/blog.db"
SQLALCHEMY_DATABASE_URI = "sqlite:////vagrant/blog.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
CELERY_BROKER_URL="pyamqp://guest@localhost//"

EMAIL_USERNAME=os.environ.get("MDBLOG_EMAIL_USERNAME", None)
EMAIL_PASSWORD=os.environ.get("MDBLOG_EMAIL_PASSWORD", None)