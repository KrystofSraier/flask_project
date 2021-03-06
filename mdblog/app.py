from flask import Flask
from flask import render_template

from .models import db
from .mod_main import main
from .mod_blog import blog
from .mod_admin import admin

from .mod_main.form import NewsletterForm

from celery import Celery

import os

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


flask_app = Flask(__name__)

flask_app.config.from_pyfile("/vagrant/configs/default.py")

if "MDBLOG_CONFIG" in os.environ:
    flask_app.config.from_envvar("MDBLOG_CONFIG")
db.init_app(flask_app)

celery = make_celery(flask_app)

flask_app.register_blueprint(main)
flask_app.register_blueprint(blog)
flask_app.register_blueprint(admin, url_prefix="/admin")

@flask_app.errorhandler(500)
def internal_server_error(error):
    return render_template ("errors/500.jinja"), 500
    
@flask_app.errorhandler(404)
def internal_server_error(error):
    return render_template ("errors/404.jinja"), 404
    
@flask_app.context_processor
def inject_newsletter_form():
    return dict (newsletter_form = NewsletterForm())

## Celery

@celery.task
def foobar(arg):
    import time
    print ("starting task {}".format(arg))
    for x in range (10):
        time.sleep(2)
        print (x)
    print ("task {} finished".format(arg))
    
@flask_app.route("/foobar/")
def start_task():
    foobar.delay(3332)
    return "ok"




## CLI COMMAND
def init_db(app):
    with app.app_context():
        db.create_all()
        print("database inicialized")
        
        default_user = User(username="admin")
        default_user.set_password("admin")
        
        db.session.add(default_user)
        db.session.commit()
        print ("created")