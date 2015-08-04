# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username==u'管理员' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message=u'错误的用户名或密码',username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
