from mdblog.app import flask_app
from mdblog.models import db
from mdblog.models import Article

from loremipsum import get_sentences
import random

COUNT = 50

def create_article(num):
    title = "Article {:02}".format(num)
    
    content = " ".join(get_sentences(random.randint(3,9), True))
    article = Article(title=title, content=content)
    return article
    
with flask_app.app_context():

    for num in range(1, COUNT+1):
        article = create_article(num)
        db.session.add(article)
        db.session.commit()
        print ("article #{:02d} created!".format(num))