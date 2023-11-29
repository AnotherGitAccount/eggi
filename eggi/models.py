from eggi.database import db
from enum import Enum

class Roles(Enum):
    READER    = "reader"
    PUBLISHER = "publisher"
    ADMIN     = "admin"

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email    = db.Column(db.Text, nullable=False)
    role     = db.Column(db.Text, nullable=False)

class Library(db.Model):
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name       = db.Column(db.Text, unique=True, nullable=False)
    is_private = db.Column(db.Boolean, nullable=False)

class Subscrition(db.Model):
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id       = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    library_id    = db.Column(db.Integer, db.ForeignKey("library.id"), nullable=False)
    is_maintainer = db.Column(db.Text, nullable=False)

class Revision(db.Model):    
    id               = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commit_hash      = db.Column(db.Text, nullable=False)
    version          = db.Column(db.Text, nullable=False)
    changelog        = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.Text, nullable=False)
    downloads_cnt    = db.Column(db.Integer, nullable=False)
    status           = db.Column(db.Text, nullable=False)
    activity_info    = db.Column(db.Text, nullable=False)
    library_id       = db.Column(db.Integer, db.ForeignKey("library.id"), nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint('library_id', 'version', name='unique_library_version'),
    )
    
class Dependency(db.Model):
    id           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    index_url    = db.Column(db.Text, nullable=False)
    name         = db.Column(db.Text, nullable=False)
    version      = db.Column(db.Text, nullable=False)
    revision_id  = db.Column(db.Integer, db.ForeignKey("revision.id"), nullable=False)