SQLALCHEMY_DATABASE_URI = "postgres://docker:docker@database"
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = b'""\x9ac\xbc\x82\xcb\xd0\xa7\xe8Y\xecsV/\x93F\xeax\x99\xa3\x7f\x03\t'

NEWSLETTER_MAIL_USER = "krystofsraier17@gmail.com"
NEWSLETTER_MAIL_PASSWORD = "waagejeadela17"

## CELERY CONFIG
BROKER_URL = "pyamqp://guest@rabbitmq//"

