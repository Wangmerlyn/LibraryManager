# -*- coding:utf-8 -*-
from flask import Flask, request, session, url_for, redirect, render_template,jsonify,g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import time
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://iair:Iair1234!@115.154.251.17:3306/lala_db'
# 协议：mysql+pymysql
# 用户名：iair
# 密码：Iair1234!
# IP地址：115.154.251.17
# 端口：3306
# 数据库名：lala_db #这里的数据库需要提前建好
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config['ADMIN_NAME'] = 'admin'
app.config['ADMIN_PWD'] = '123456'
app.config['ADMIN_ID'] = '0'

'''
    开始部分 类定义
    第一部分 登录模块
    第二部分 管理员模块
    第三部分 学生模块
    第四部分 检索模块
'''

#类定义
class Books(db.Model):
    # 定义表名
    __tablename__ = 'lala'
    # 定义列对象
    bookID = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.VARCHAR(254), nullable=False)
    authors = db.Column(db.VARCHAR(750), nullable=False)
    average_rating = db.Column(db.VARCHAR(93), nullable=False)
    isbn = db.Column(db.VARCHAR(10), nullable=False)
    isbn13 = db.Column(db.VARCHAR(13), nullable=False)
    language_code = db.Column(db.VARCHAR(13), nullable=False)
    num_pages = db.Column(db.VARCHAR(11), nullable=False)
    ratings_count = db.Column(db.VARCHAR(13), nullable=False)
    text_reviews_count = db.Column(db.VARCHAR(18), nullable=False)
    publication_date = db.Column(db.VARCHAR(16), nullable=False)
    publisher = db.Column(db.VARCHAR(67), nullable=False)

class BookSchema(ma.Schema):
    class Meta:
        fields = ('bookID', 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages',
                  'ratings_count', 'text_reviews_count', 'publication_date', 'publisher')

book_schema = BookSchema()
books_schema = BookSchema(many=True)

class Students(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    student_name = db.Column(db.Text(), nullable=False)
    pwd = db.Column(db.Text(), nullable=False)
    college = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text())
    sex = db.Column(db.Text())
    tel = db.Column(db.Text())

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('student_id', 'student_name', 'pwd', 'college', 'email', 'sex', 'tel')

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

class Borrow(db.Model):
    __tablename__ = 'borrow'
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.Text(), nullable=False)
    student_name = db.Column(db.Text(), nullable=False)
    date_borrow = db.Column(db.Text(), nullable=False)
    date_return = db.Column(db.Text())


#1.登录
@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']

#欢迎界面
@app.route("/")
def index():
    #return jsonify({"success": False})
    return render_template('index.html')

#登录界面
@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.json['username'] == app.config["ADMIN_NAME"]:
        if request.json['password'] != app.config['ADMIN_PWD']:
            error = 'Invalid password'
        else:
            session['user_id'] = app.config['ADMIN_ID']
            return jsonify({"identity": "admin", "success": True})
            #return redirect(url_for('admin'))
    else:
        student = Students.query.filter_by(student_name = request.json['username']).first()
        if student is None:
            error = 'Invalid username'
        elif student.pwd != request.json['password']:
            error = 'Invalid password'
        else:
            session['user_id'] = student.student_id
            return jsonify({"identity": "user", "success": True})
            #return redirect(url_for('student'))
    return jsonify({"identity": "user", "success": False})
    #return render_template('login.html', error=error)

#登出界面
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

#管理员界面
@app.route('/admin')
def admin():
    return render_template('admin.html')

#学生界面
@app.route('/student')
def student():
    return render_template('student.html')


#2.管理员模块
#2.1 书籍管理 /admin/book
@app.route('/admin/book', methods=['GET'])
def admin_books():
    all_books = Books.query.all()
    results = books_schema.dump(all_books)
    return jsonify(results)
    #return render_template('admin_books.html', books=all_books)

@app.route('/admin/book/<id>/', methods=['GET'])
def admin_book(id):
    book = Books.query.get(id)
    results = book_schema.dump(book)
    return jsonify(results)
    #return render_template('admin_book.html', book=book)

@app.route('/admin/book/add', methods=['POST'])
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
        return jsonify({"success": True})
        #return redirect(url_for('admin_books'))
    return jsonify({"success": False})
    #return render_template('admin_book_add.html', error=error)


@app.route('/admin/book/delete', methods=['POST'])
def delete_book():
    error =None
    id = request.json['bookID']
    book = Books.query.get(id)
    if book is None:
        error = 'no this book'
    else:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"success": True})
        #return redirect(url_for('admin_books'))
    return jsonify({"success": False})
    #return render_template('admin_book_delete.html', error=error)

@app.route('/admin/book/modify', methods=['POST'])
def update_book():
    error = None
    id = request.json['bookID']
    book = Books.query.get(id)
    if book is None:
        error = 'no this book'
    else:
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
            book.bookID = request.json['BookID']
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
            db.session.commit()
            return jsonify({"success": True})
            #return redirect(url_for('admin_books'))
    return jsonify({"success": False})
    #return render_template('admin_book_update.html', error=error)

#2.2管理员学生管理 /admin/student
@app.route('/admin/student', methods=['GET'])
def admin_students():
    all_students = Students.query.all()
    results = students_schema.dump(all_students)
    return jsonify(results)
    #return render_template('admin_students.html', students=all_students)

@app.route('/admin/student/<id>/', methods=['GET'])
def admin_student(id):
    student = Students.query.get(id)
    results = student_schema.dump(student)
    return jsonify(results)
    #return render_template('admin_student.html', student=student)

# 增
@app.route('/admin/student/libcard', methods=['POST'])
def add_student():
    if not request.json['student_id']:
        error = 'You should input the student id'
    elif not request.json['student_name']:
        error = 'You should input the student name'
    elif not request.json['pwd']:
        error = 'You should input the passward'
    elif not request.json['college']:
        error = 'You should input the college'
    elif not request.json['email']:
        error = 'You should input the email'
    else:
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
        return jsonify({"success": True})
        #return redirect(url_for('admin_students'))
    return jsonify({"success": False})
    #return render_template('student_add.html', error=error)

# 删
@app.route('/admin/student/libcardLogout', methods=['POST'])
def delete_student():
    error =None
    id = request.json['student_id']
    student = Students.query.get(id)
    if student is None:
        error = 'no this student'
    else:
        db.session.delete(student)
        db.session.commit()
        return jsonify({"success": True})
        #return redirect(url_for('admin_students'))
    return jsonify({"success": False})
    #return render_template('student_delete.html',error=error)

# 改
@app.route('/admin/student/libcardModify', methods=['POST'])
def update_student():
    error = None
    id = request.json['student_id']
    student = Students.query.get(id)
    if student is None:
        error = 'no this student'
    else:
        if not request.json['student_id']:
            error = 'You should input the student id'
        elif not request.json['student_name']:
            error = 'You should input the student name'
        elif not request.json['pwd']:
            error = 'You should input the passward'
        elif not request.json['college']:
            error = 'You should input the college'
        elif not request.json['email']:
            error = 'You should input the email'
        else:
            student.student_id = request.json['student_id']
            student.student_name = request.json['student_name']
            student.pwd = request.json['pwd']
            student.college = request.json['college']
            student.email = request.json['email']
            student.sex = request.json['sex']
            student.tel = request.json['tel']
            db.session.commit()
            return jsonify({"success": True})
            #return redirect(url_for('admin_students'))
    return jsonify({"success": False})
    #return render_template('student_update.html',error=error)


#3学生
#3.1学生借还书
@app.route('/student/book')
def student_book():
    return render_template('student_book.html')

@app.route('/student/book/borrow', methods =['POST'])
def student_book_borrow():
    error = None
    thebook = Books.query.get(request.json['bookID'])
    if thebook is None:
        error = 'no this book'
    else:
        ifborrow = Borrow.query.get(request.json['bookID'])
        student = Students.query.get(g.user)
        if ifborrow is None:
            bookid = thebook.bookID
            bookname = thebook.title
            studentname = student.student_name
            current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            return_time = time.strftime('%Y-%m-%d', time.localtime(time.time() + 2600000))
            borrow = Borrow(book_id=bookid, book_name=bookname, student_name=studentname, data_borrow=current_time,
                            data_return=return_time)
            db.session.add(borrow)
            db.session.commit()
            return jsonify({"success": True})
            #return redirect(url_for('student_book_borrow'))
        else:
            error = 'The book has already borrowed.'
    return jsonify({"success": False})
    #return render_template('student_book_borrow.html', error=error)

@app.route('/student/book/return', methods =['POST'])
def student_book_return():
    error = None
    thebook = Books.query.get(request.json['bookID'])
    if thebook is None:
        error = 'no this book'
    else:
        ifborrow = Borrow.query.get(request.json['bookID'])
        if ifborrow is None:
            error = 'The book has not been borrowed.'
        else:
            borrow = Borrow.query.get(request.json['bookID'])
            db.session.delete(borrow)
            db.session.commit()
            return jsonify({"success": True})
            #return redirect(url_for('student_book_return'))
    return jsonify({"success": False})
    #return render_template('student_book_borrow.html', error=error)

#3.2学生信息管理
@app.route('/student/info', methods=['GET'])
def student_info():
    student = Students.query.get(g.user)
    results = student_schema.dump(student)
    return jsonify(results)
    #return render_template('student_info.html', student=student)

#信息修改
@app.route('/student/libcardModify', methods=['POST'])
def student_libcardModify():
    student = Students.query.get(g.user)
    if not request.json['student_id']:
        error = 'You should input the student id'
    elif not request.json['student_name']:
        error = 'You should input the student name'
    elif not request.json['pwd']:
        error = 'You should input the passward'
    elif not request.json['college']:
        error = 'You should input the college'
    elif not request.json['email']:
        error = 'You should input the email'
    else:
        student.student_id = request.json['student_id']
        student.student_name = request.json['student_name']
        student.pwd = request.json['pwd']
        student.college = request.json['college']
        student.email = request.json['email']
        student.sex = request.json['sex']
        student.tel = request.json['tel']
        db.session.commit()
        return jsonify({"success": True})
        #return redirect(url_for('student'))
    return jsonify({"success": False})
    #return render_template('student_libcardModify.html', error=error)

#4.检索
@app.route('/search', methods=['GET', 'POST'])
def reader_query():
    # reader_judge()
    error = None
    books = None
    if request.method == 'POST':
        if (not request.form['bookID']) and (not request.form['BookName']) and (not request.form['Writer']) and (not request.form['SortID']):
            success = True
            sqlcmd = ('select * from books where bookID LIKE %{}%').format(request.form['bookID'])
            books = db.session.execute(sqlcmd)
            results = books_schema.dump(books)
            return jsonify(results)
        else:
            success = False
    return jsonify({"success": False})
    #return render_template('reader_query.html', books=books, error=error)




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)