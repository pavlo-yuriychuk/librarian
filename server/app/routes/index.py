from app import app, db
from flask import make_response
from json import loads, dumps
from app.models import Book, Author, AuthorizationToken, User

NOT_AUTHORIZED = {'code': 401, 'message': 'Access to this endpoint is prohibited'}
BAD_REQUEST = {'code': 400, 'message': 'Bad request'}
NOT_FOUND = {'code': 404, 'message': 'Not found'}
DELETED_SUCCESSFULLY = {'code': 204, 'message': 'Deleted successfully'}

@app.route('/')
def index():
    return dumps(NOT_AUTHORIZED)


@app.route('/books', methods=['GET', 'POST'])
def query_books_or_create():
    if request.method == 'GET':
        query_author = request.args.get('author', '')
        if not query_author:
            books = Book.query.all()
        else:
            books = Book.query.filter_by(author=query_author)
        return make_response(dumps(books), 200)
    elif request.method == 'POST':
        if request.data is dict:
            name = request.data.get('name', '')
            if not Name:
                return make_response(dumps(BAD_REQUEST), 400)
            else:
                book = Book(name=name)
                with db.session as db_session:
                    db_session.add(book)
                    db_session.commit()
                book = Book.query.filter_by(name=name).first()
                return make_response(dumps(book), 201)
        else:
            return make_response(dumps(BAD_REQUEST), 400)
    else:
        return make_response(dumps(BAD_REQUEST), 400)


@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    if id is None:
        return make_response(dumps(BAD_REQUEST), 400)
    book = Book.query.filter_by(id=id).first()
    if book is None:
        return make_response(dumps(NOT_FOUND), 404)
    else:
        return make_response(dumps(book), 200)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    if id is None:
        return make_response(dumps(BAD_REQUEST), 400)
    book = Book.query.filter_by(id=id).first()
    if book is None:
        return make_response(dumps(NOT_FOUND), 404)
    else:
        with db.session as db_session:
            db_session.delete(book)
            db_session.commit()
        return make_response(dumps(DELETED_SUCCESSFULLY), 204)

@app.route('/authors', methods=['GET'])
def query_authors_or_create():
    if request.method == 'GET':
        query_book = request.args.get('book', '')
        if not query_book:
            books = Book.query.all()
        else:
            books = Book.query.filter_by(book=query_book)
        return dumps(books)
    elif request.method == 'POST':
        if request.data is dict:
            name = request.data.get('name', '')
            if not Name:
                return make_response(dumps(BAD_REQUEST), 400)
            else:
                author = Author(name=name)
                with db.session as db_session:
                    db_session.add(author)
                    db_session.commit()
                author = Author.query.filter_by(name=name).first()
                return make_response(dumps(author), 201)
        else:
            return make_response(dumps(BAD_REQUEST), 400)
    else:
        return dumps(BAD_REQUEST)

@app.route('/authors/<int:id>', methods=['GET'])
def get_author_by_id(id):
    if id is None:
        return make_response(dumps(BAD_REQUEST), 400)
    author = Author.query.filter_by(id=id).first()
    if author is None:
        return make_response(dumps(NOT_FOUND), 404)
    else:
        return make_response(dumps(author), 200)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_author_by_id(id):
    if id is None:
        return make_response(dumps(BAD_REQUEST), 400)
    author = Author.query.filter_by(id=id).first()
    if author is None:
        return make_response(dumps(NOT_FOUND), 404)
    else:
        with db.session as db_session:
            db_session.delete(author)
            db_session.commit()
        return make_response(dumps(DELETED_SUCCESSFULLY), 204)

@app.route('/logout', methods=['POST'])
def logout():
    token_id  = request.data.get('token', '')
    if not token_id:
        return make_response(dumps(BAD_REQUEST), 404)
    token = AuthorizationToken.query.filter_by(id=token_id).first()
    if token:
        with db.session as db_session:
            db_session.delete(token)
            db_session.commit()
        return dumps({'message': 'Logged out', 'code': 200})
    else:
        return make_response(dumps(NOT_FOUND), 404)

@app.route('/login', methods=['POST'])
def login():
    data = request.data
    if data is dict:
        username = data.get('username', '')
        password = data.get('password', '')
        if not username:
            return make_response(dumps(BAD_REQUEST), 404)
        if not password:
            return make_response(dumps(BAD_REQUEST), 404)
        user = User.query.filter_by(name=username).first()
        if not user:
            return make_response(dumps(NOT_FOUND), 404)
        if user.is_valid_password(password):
            token = AuthorizationToken(username)
            with db.session as db_session:
                db_session.add(token)
                db_session.commit()
            return make_response(dumps({'token': token.id}), 200)
        else:
            return make_response(dumps(NOT_AUTHORIZED), 401)
    else:
        return make_response(dumps(BAD_REQUEST), 404)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.data
    if data is dict:
        username = data.get('username', '')
        password = data.get('password', '')
        if not username:
            return make_response(dumps(BAD_REQUEST), 404)
        if not password:
            return make_response(dumps(BAD_REQUEST), 404)
        user = User(name=username, password=password)
        with db.session as db_session:
            db_session.add(user)
            db_session.commit()
        user = User.query.filter_by(username=username).first()
        return make_response(dumps(user), 201)
    else:
        return make_response(dumps(BAD_REQUEST), 404)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(dumps(NOT_FOUND), 404)
    return resp

@app.errorhandler(400)
def not_found(error):
    resp = make_response(dumps(BAD_REQUEST), 404)
    return resp

@app.errorhandler(401)
def not_found(error):
    resp = make_response(dumps(NOT_AUTHORIZED), 401)
    return resp