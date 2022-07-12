import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =
# app.config['SQLALCHEMY_']
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Articles(db.Module):
    id = db.Column(db.Interger, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DataTime, datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


@app.route('/get', method=['GET'])
def get_articles():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)


@app.route('/get/<id>/', method=['GET'])
def post_details(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)


@app.route('/add', method=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)


@app.route('/update/<id>', method=['PUT'])
def update_article(id):
    article = Articles.query.get(id)
    title = request.json['title']
    body = request.json['body']
    article.title = title
    article.body = body

    db.session.commit()
    return article_schema.jsonify(article)


@app.route('delete/<id>', method=['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article)


# class book(db.Model):
#     # 定义表名
#     __tablename__ = 'lala'
#     # 定义列对象
#     bookID = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.VARCHAR(254))
#     authors = db.Column(db.VARCHAR(750))
#     average_rating = db.Column(db.VARCHAR(93))
#     isbn = db.Column(db.VARCHAR(10))
#     isbn13 = db.Column(db.VARCHAR(13))
#     language_code = db.Column(db.VARCHAR(13))
#     num_pages = db.Column(db.VARCHAR(11))
#     ratings_count = db.Column(db.VARCHAR(13))
#     text_reviews_count = db.Column(db.VARCHAR(18))
#     publication_date = db.Column(db.VARCHAR(16))
#     publisher = db.Column(db.VARCHAR(67))
#     """
#     def __init__(self, bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publicati on_date, publisher):
#     """
#
#
#
# class Students(db.Model):
#     __tablename__ = 'students'
#     student_id = db.Column(db.Interger, primary_key=True)
#     student_name = db.Column(db.Text())
#     pwd = db.Column(db.Text())
#     college = db.Column(db.Text())
#     num = db.Column(db.Text())
#     email = db.Column(db.Text())
#     sex = db.Column(db.Text())
#     tel = db.Column(db.Text())
#     """
#         def __init__(self, student_id, student_name, pwd, college, email, sex, tel):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.pwd = pwd
#         self.college = college
#         self.email = email
#         self.sex = sex
#         self.tel = tel
#     """
#
#
# class History(db.Model):
#     __tablename__ = 'hiatory'
#     histroy_id = db.Column(db.Interger, primary_key=True)
#     book_id = db.Column(db.Interger)
#     student_name = db.Column(db.Text())
#     date_borrow = db.Column(db.Text())
#     date_return = db.Column(db.Text())
#     status = db.Column(db.Text(), default = 'not return')
#     """
#         def __init__(self, history_id, book_id, student_name, date_borrow, date_return, status):
#         self.histroy_id = history_id
#         self.book_id = book_id
#         self.user_name = student_name
#         self.date_borrow = date_borrow
#         self.date_return = date_return
#         self.status = status
#     """