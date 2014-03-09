from app import db
from app.utils import current_milli_time, hash_password
from os import urandom

books = db.Table('tags',
                 db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                 db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
                )


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    books = db.relationship('Book', secondary=books, backref=db.backref('books', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Author %d : %r>' % (self.id, self.name)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    authors = db.relationship('Author', secondary=books, backref=db.backref('authors', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Book %d : %r>' % (self.id, self.name)


class AuthorizationToken(db.Model):
    TTL = 3600*1000
    id = db.Column(db.String(128), primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    expires = db.Column(db.Integer)

    def __init__(self, username, ttl=TTL):
        self.id = urandom(128)
        self.expires = current_milli_time() + ttl
        self.user = username

    def is_expired(self):
        return current_milli_time() < self.expires


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(512))
    salt = db.Column(db.string(512))
    tokens = db.relationship('Token', backref='user', lazy='dynamic')

    def __init__(self, name, password):
        self.name = name
        self.salt = urandom(512)
        self.password_hash = hash_password(password, self.salt)

    def is_valid_password(self, password):
        return hash_password(password, self.salt) == self.password_hash