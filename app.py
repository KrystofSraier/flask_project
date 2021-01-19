from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")
 
@flask_app.route("/about/") 
def view_about():
    return render_template("about.jinja")
    
@flask_app.route("/krystof/")
def view_kokotko():
    return "Hello Krystof"
    
@flask_app.route("/krystof/<string:name>/", methods=["GET", "POST"])
def view_kokotko_name(name):
    return "Hello {}".format(name)
    
@flask_app.route("/article/<int:art_id>/neco/<float:foo>/")
def view_kokotko_etc(art_id, foo):
    return "Article{} neco:  {}".format(art_id, foo)