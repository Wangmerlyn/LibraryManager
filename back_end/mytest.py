from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
    render_template, abort, g, flash, _app_ctx_stack
from werkzeug.security import check_password_hash, generate_password_hash
import time

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route('/manager_login', methods=['GET', 'POST'])
def manager_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config["MANAGER_NAME"]:
            error = 'Invalid username'
        elif request.form['password'] != app.config['MANAGER_PWD']:
            error = 'Invalid password'
        else:
            session['user_id'] = app.config['MANAGER_NAME']
            return redirect(url_for('manager'))
    return render_template('manager_login.html', error=error)


@app.route('/reader_login', methods=['GET', 'POST'])
def reader_login():
    error = None
    if request.method == 'POST':
        user = query_db('''select * from users where user_name = ?''',
                        [request.form['username']], one=True)
        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['pwd'], request.form['password']):
            error = 'Invalid password'
        else:
            session['user_id'] = user['user_name']
            return redirect(url_for('reader'))
    return render_template('reader_login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password'] != request.form['password2']:
            error = 'The two passwords do not match'
        elif get_user_id(request.form['username']) is not None:
            error = 'The username is already taken'
        else:
            db = get_db()
            db.execute('''insert into users (user_name, pwd, college, num, email) \
				values (?, ?, ?, ?, ?) ''', [request.form['username'], generate_password_hash(
                request.form['password']), request.form['college'], request.form['number'],
                                             request.form['email']])
            db.commit()
            return redirect(url_for('reader_login'))
    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))
