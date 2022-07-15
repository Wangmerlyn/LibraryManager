# -*- coding:utf-8 -*-
from flask import Flask, request, session, url_for, redirect, render_template,jsonify,g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from sqlalchemy import and_, or_
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

access=""

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
    __tablename__ = 'newlala'
    # 定义列对象
    bookID = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.Text(), nullable=False)
    authors = db.Column(db.Text(), nullable=False)
    isbn10 = db.Column(db.Text(), nullable=False)
    categories = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    publication_date = db.Column(db.Integer, nullable=False)
    average_rating = db.Column(db.Text(), nullable=False)
    num_pages = db.Column(db.Integer, nullable=False)
    ratings_count = db.Column(db.Integer, nullable=False)


class BookSchema(ma.Schema):
    class Meta:
        fields = ('bookID', 'title', 'authors', 'isbn10', 'categories', 'description', 
                  'publication_date', 'average_rating', 'num_pages', 'ratings_count')

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
    date_borrow = db.Column(db.Text())
    date_return = db.Column(db.Text())


#1.登录
@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']

# #欢迎界面
# @app.route("/")
# def index():
#     #return jsonify({"success": False})
#     return render_template('index.html')

#登录界面
@app.route('/login', methods=['POST'])
def login():
    error = None
    global access
    if request.json['username'] == app.config["ADMIN_NAME"]:
        if request.json['password'] != app.config['ADMIN_PWD']:
            error = 'Invalid password'
        else:
            session['user_id'] = app.config['ADMIN_ID']
            
            access="admin"
            
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
            access="user"
            return jsonify({"identity": "user", "success": True})
            #return redirect(url_for('student'))
    access="wrong_authority"
    return jsonify({"identity": "wrong_authority", "success": False})
    #return render_template('login.html', error=error)

@app.route('/currentUser',methods=['GET'])
def get_current_User_authority():
    print(access)
    if access != "":
        return jsonify({"success": "true","data":{"name":access,\
            "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',"access":access}})
    elif access == "wrong_authority":
        return jsonify({"success": "false","data":{"access":""}})
    else:
        return jsonify({"success": "false","data":{"access":""}})

@app.route('/login/outLogin')
def logout():
    global access
    access=""
    print("logout")
    session.pop('user_id', None)
    return jsonify({"data":{},"success": "true"})

# #管理员界面
# @app.route('/admin')
# def admin():
#     return render_template('admin.html')

# #学生界面
# @app.route('/student')
# def student():
#     return render_template('student.html')


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
    print('234')
    book = Books.query.get(id)
    results = book_schema.dump(book)
    return jsonify(results)
    #return render_template('admin_book.html', book=book)

@app.route('/admin/book/add', methods=['POST'])
def add_book():
    if not request.json['bookID']:
        error = 'You should input the BookID'
    elif not request.json['authors']:
        error = 'You should input the authors'
    elif not request.json['title']:
        error = 'You should input the title'
    elif not request.json['isbn10']:
        error = 'You should input the isbn10'
    elif not request.json['categories']:
        error = 'You should input the categories'
    elif not request.json['description']:
        error = 'You should input the description'
    elif not request.json['publication_date']:
        error = 'You should input the publication_date'
    elif not request.json['average_rating']:
        error = 'You should input the average_rating'
    elif not request.json['num_pages']:
        error = 'You should input the num_pages'
    elif not request.json['ratings_count']:
        error = 'You should input the ratings_count'
    else:
        bookID = request.json['bookID']
        title = request.json['title']
        authors = request.json['authors']
        isbn10 = request.json['isbn10']
        categories = request.json['categories']
        description = request.json['description']
        publication_date = request.json['publication_date']
        average_rating = request.json['average_rating']
        num_pages = request.json['num_pages']
        ratings_count = request.json['ratings_count']

        book = Books(bookID=bookID, title=title, authors=authors, isbn10=isbn10,
                     categories=categories, description=description,  publication_date=publication_date,
                     average_rating=average_rating, num_pages=num_pages, ratings_count=ratings_count)
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
        if not request.json['bookID']:
            error = 'You should input the BookID'
        elif not request.json['authors']:
            error = 'You should input the authors'
        elif not request.json['title']:
            error = 'You should input the title'
        elif not request.json['isbn10']:
            error = 'You should input the isbn10'
        elif not request.json['categories']:
            error = 'You should input the categories'
        elif not request.json['description']:
            error = 'You should input the description'
        elif not request.json['publication_date']:
            error = 'You should input the publication_date'
        elif not request.json['average_rating']:
            error = 'You should input the average_rating'
        elif not request.json['num_pages']:
            error = 'You should input the num_pages'
        elif not request.json['ratings_count']:
            error = 'You should input the ratings_count'
        else:
            book.bookID = request.json['bookID']
            book.title = request.json['title']
            book.authors = request.json['authors']
            book.isbn10 = request.json['isbn10']
            book.categories = request.json['categories']
            book.description = request.json['description']
            book.publication_date = request.json['publication_date']
            book.average_rating = request.json['average_rating']
            book.num_pages = request.json['num_pages']
            book.ratings_count = request.json['ratings_count']
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
            borrow = Borrow(book_id=bookid, book_name=bookname, student_name=studentname, date_borrow=current_time,
                            date_return=return_time)
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
            student = Students.query.get(g.user)
            if student.student_name != ifborrow.student_name:
                error = 'the book is not borrowed by you'
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
    else:
        student.student_id = request.json['student_id']
        session.pop('user_id', None)
        session['user_id'] = student.student_id
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
#4.检索
@app.route('/search', methods=['POST'])
def reader_query():
    # reader_judge()
    error = None
    books = None
    print(request.json)
    if request.method == 'POST':
        if request.json['bookID'] or request.json['title'] or request.json['authors'] or request.json['categories']:
            limit = 20
            books1 = Books.query.filter((Books.bookID == request.json['bookID'])).all()
            books2 = Books.query.filter(
                                        or_(Books.categories.like(('%{}%').format(request.json['categories'])),
                                            Books.title.like(('%{}%').format(request.json['title'])),
                                            Books.authors.like(('%{}%').format(request.json['authors']))
                                           )).order_by(
                                        (
                                            Books.categories.like(('%{}%').format(request.json['categories'])) +
                                            Books.title.like(('%{}%').format(request.json['title'])) +
                                            Books.authors.like(('%{}%').format(request.json['authors'])) +
                                            (Books.categories == request.json['categories']) * 2 +
                                            (Books.title == request.json['title']) * 2 +
                                            (Books.authors == request.json['authors']) * 2
                                        )
                                    .desc()).limit(limit).all()
            data1 = books_schema.dump(books1)
            data2 = books_schema.dump(books2)
            data = data1 + data2
            # data=data1
            #sqlcmd = ('select * from books where bookID LIKE %{}%').format(request.form['bookID'])
            results = {
                "success": True,
                "data": data
            }
            return jsonify(results)
        else:
            success = False
    return jsonify({"success": False})


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)