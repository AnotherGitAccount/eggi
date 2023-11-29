import os
from flask import Flask, render_template
from eggi.database import db, init_app

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=os.path.join(app.instance_path, "eggi.sqlite"),
    SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, "eggi.sqlite")
)
app.config.from_pyfile("config.py", silent=True)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)
init_app(app)

@app.route('/')
def index():
    return render_template("index.html")