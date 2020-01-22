#!/usr/bin/python3.7
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

from flask import render_template
#from flask_appbuilder.models.sqla.interface import SQLAInterface
#from flask_appbuilder import ModelView, ModelRestApi
from log_generator import generate_access_log
#from . import appbuilder, db
from os.path import join
#from random import randint
from profile_generator import Person
from datetime import timedelta, datetime


"""
    Application wide 404 error handler
"""

@app.route('/')
def welcome():
    message = "This is not for you"
    return render_template('index.html', message = message)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e)
@app.route('/admin/log/<entries>/')
@app.route('/log/<entries>/')
def make_access_log(entries):
    log_entries = generate_access_log(entries, datetime.now()-timedelta(days=1))
    outfile = join('static/','fakeaccesslog.txt')
    fh = open(outfile, '+w')
    for entry in log_entries:
        fh.write(entry+"\r")
    fh.close()
    return render_template('fake_access_log.html', log=log_entries)

"""View fake logs"""
@app.route('/admin/log/')
@app.route('/log/')
@app.route('/admin/access')
def get_access_log():
    infile = join('static/', 'fakeaccesslog.txt')

    fh = open(infile, 'r')
    #log = fh.read()
    log_entries = fh.readlines()
    #log = fh.read()
    fh.close()
    for i in log_entries:
        if len(i) < 2:
            log_entries.remove(i)
        i = i.replace("\r", "").replace('\n', '').strip()


    return render_template('fake_access_log.html', log=log_entries)
@app.route('/admin/account_dump/')
@app.route('/admin/users/')
def fake_users():
    users = []
    for i in range(14):
        try:
            a = Person()
        except IndexError:
            a = Person()
        users.append(a.get_json_str())
        del a
    return render_template('list.html', list=users)
#db.create_all()


