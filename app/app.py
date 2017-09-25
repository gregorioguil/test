#!flask/bin/python
#mongo.py
from flask import Flask, render_template , Blueprint
from flask import jsonify
from flask import request
from flask import json
from flask_pymongo import PyMongo
from wtforms import Form,BooleanField, StringField, PasswordField, validators
from pymongo import MongoClient
import os

app = Blueprint('app', __name__)

name = ""
passWord = ""
cont = 1

clientdb = MongoClient("192.168.1.153:27017")
db = clientdb.test_database
album= db.test_collection


class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('password', [validators.Length(min=6, max=35)])




def upload():
    global cont
        #global data

    con = 0
        #while( con <= 100):
    # data =  [{
    #         'id': '0',
    #         'ttime': '10'
    #     }]
    #
    # album.insert_many(data)
    dat = album.find_one({'id':cont})
    aux =  json.dumps(dat['ttime'])
    aux1 = aux.split('"')
    aux2 = aux1[1].split("'")
    data = [(cont*1000),int(aux1[1])]
    cont = cont + 1

    print(dat)
    return json.dumps(data)



def check_login(username,password):
        if name == username and passWord == password:
                return True
        else:
                return False

@app.route('/')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.route('/login', methods=['POST'])
def do_login():
        form = LoginForm(request.form)
        if check_login(form.username.data, form.password.data):
                x = upload()

                print(x)
                return render_template('index.html',x=x)
        else:
                return "<p>Login failed.</p>"


@app.route('/up')
def index():
        x = upload()
        print(x)
        return x

@app.route('/get',methods=['GET'])
def getAll():
        return jsonify({'data':data})


@app.route('/post',methods=['POST'])
def createData():
        print("create ")

        dat = {
                'ttime': '0',
        }

        dat = request.data
        return jsonify(data)
