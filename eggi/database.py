import sqlite3
import click
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

def create_db():
    conn = None
    try:
        conn = sqlite3.connect(current_app.config["DATABASE"])
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()

from eggi.models import *
def init_db():
    db.create_all()
    admin = User(
        id=None,
        username="eggi",
        password=generate_password_hash("eggi"),
        email="eggi@eggi.com",
        role=Roles.ADMIN.value                                    
    )
    db.session.add(admin)
    db.session.commit()

@click.command("init-db")
def init_db_command():
    create_db()
    init_db()
    click.echo("Database created and initialized!")

def init_app(app):
    app.cli.add_command(init_db_command)