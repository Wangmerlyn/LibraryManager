import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =
# app.config['SQLALCHEMY_']
db = SQLAlchemy(app)
ma = Marshmallow(app)


'''
    第一部分：/admin/book 图书信息增删查改 (查：hya)
    第二部分：/admin/student 学生信息增删查改 (查：hya)
    第三部分：/student 学生信息管理 (查：hya)
    第四部分：/student/book 借阅管理
'''

#############################################
# 类定义
# 1. Books类
class Books(db.Model):
    # 定义表名
    __tablename__ = 'lala'
    # 定义列对象
    bookID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(254))
    authors = db.Column(db.VARCHAR(750))
    average_rating = db.Column(db.VARCHAR(93))
    isbn = db.Column(db.VARCHAR(10))
    isbn13 = db.Column(db.VARCHAR(13))
    language_code = db.Column(db.VARCHAR(13))
    num_pages = db.Column(db.VARCHAR(11))
    ratings_count = db.Column(db.VARCHAR(13))
    text_reviews_count = db.Column(db.VARCHAR(18))
    publication_date = db.Column(db.VARCHAR(16))
    publisher = db.Column(db.VARCHAR(67))


class BookSchema(ma.Schema):
    class Meta:
        fields = ('bookID', 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages',
                  'ratings_count', 'text_reviews_count', 'publicati on_date', 'publisher')

book_schema = BookSchema()
books_schema = BookSchema(many=True)

# 2. Students类
class Students(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Interger, primary_key=True)
    student_name = db.Column(db.Text())
    pwd = db.Column(db.Text())
    college = db.Column(db.Text())
    email = db.Column(db.Text())
    sex = db.Column(db.Text())
    tel = db.Column(db.Text())

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('student_id', 'student_name', 'pwd', 'college', 'email', 'sex', 'tel')

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

########################################################
# 接口
# 1. /admin/book
@app.route('/admin/book', method=['GET'])
def get_books():
    all_articles = Books.query.all()
    results = books_schema.dump(all_articles)
    return jsonify(results)


@app.route('/admin/book/<id>/', method=['GET'])
def book_details(id):
    book = Books.query.get(id)
    return book_schema.jsonify(book)


@app.route('/admin/book/add', method=['POST'])
def add_book():
    if not request.json['BookID']:
        error = 'You should input the BookID'
    elif not request.json['authors']:
        error = 'You should input the authors'
    elif not request.json['title']:
        error = 'You should input the title'
    elif not request.json['publication_date']:
        error = 'You should input the publication_date'
    elif not request.json['publisher']:
        error = 'You should input the publisher'
    else:
        bookID = request.json['bookID']
        title = request.json['title']
        authors = request.json['authors']
        average_rating = request.json['authors']
        isbn = request.json['authors']
        isbn13 = request.json['isbn13']
        language_code = request.json['language_code']
        num_pages = request.json['num_pages']
        ratings_count = request.json['ratings_count']
        text_reviews_count = request.json['text_reviews_count']
        publication_date = request.json['publication_date']
        publisher = request.json['publisher']

        book = Books(bookID=bookID, title=title, authors=authors, average_rating=average_rating,
                     isbn=isbn, isbn13=isbn13, language_code=language_code,
                     num_pages=num_pages, ratings_count=ratings_count, text_reviews_count=text_reviews_count,
                     publication_date=publication_date, publisher=publisher)
        db.session.add(book)
        db.session.commit()
    return book_schema.jsonify(book)


@app.route('/admin/book/delete', method=['DELETE'])
def delete_book(id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return book_schema.jsonify(book)


@app.route('/admin/book/update/<id>', method=['POST'])
def update_book(id):
    book = Books.query.get(id)

    book.bookID = request.json['bookID']
    book.title = request.json['title']
    book.authors = request.json['authors']
    book.average_rating = request.json['authors']
    book.isbn = request.json['authors']
    book.isbn13 = request.json['isbn13']
    book.language_code = request.json['language_code']
    book.num_pages = request.json['num_pages']
    book.ratings_count = request.json['ratings_count']
    book.text_reviews_count = request.json['text_reviews_count']
    book.publication_date = request.json['publication_date']
    book.publisher = request.json['publisher']

    db.session.cmmit()
    return book_schema.jsonify(book)

###########################################################
# 2. /admin/student

@app.route('/admin/student', method=['GET'])
def get_student():
    all_students = Students.query.all()
    results = students_schema.dump(all_students)
    return jsonify(results)


@app.route('/admin/student/<id>/', method=['GET'])
def student_details(id):
    student = Students.query.get(id)
    return books_schema.jsonify(student)


# 增
@app.route('/admin/student/libcard', method=['POST'])
def add_student():
    if not request.json['student_id']:
        error = 'You should input the student id'
    if not request.json['student_name']:
        error = 'You should input the student name'
    if not request.json['pwd']:
        error = 'You should input the passward'
    if not request.json['college']:
        error = 'You should input the college'
    if not request.json['email']:
        error = 'You should input the email'

    student_id = request.json['student_id']
    student_name = request.json['student_name']
    pwd = request.json['pwd']
    college = request.json['college']
    email = request.json['email']
    sex = request.json['sex']
    tel = request.json['tel']

    student = Students(student_id=student_id, student_name=student_name, pwd=pwd,
                       college=college, email=email, sex=sex, tel=tel)
    db.session.add(student)
    db.session.commit()
    return student_schema.jsonify(student)


# 删
@app.route('/admin/student/libcardLogout', method=['DELETE'])
def delete_student(id):
    student = Students.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return book_schema.jsonify(student)

# 改
@app.route('/admin/student/libcardModify', method=['POST'])
def update_student(id):
    student = Students.query.get(id)

    student.student_id = request.json['student_id']
    student.student_name = request.json['student_name']
    student.pwd = request.json['pwd']
    student.college = request.json['college']
    student.email = request.json['email']
    student.sex = request.json['sex']
    student.tel = request.json['tel']

    db.session.cmmit()
    return book_schema.jsonify(student)


##############################################################
# 3.学生信息管理
@app.route('/student/<id>/', method=['GET'])
def student_details(id):
    student = Students.query.get(id)
    return books_schema.jsonify(student)


@app.route('/student/libcardModify', method=['POST'])
def update_student(id):
    student = Students.query.get(id)

    student.student_id = request.json['student_id']
    student.student_name = request.json['student_name']
    student.pwd = request.json['pwd']
    student.college = request.json['college']
    student.email = request.json['email']
    student.sex = request.json['sex']
    student.tel = request.json['tel']

    db.session.cmmit()
    return book_schema.jsonify(student)



