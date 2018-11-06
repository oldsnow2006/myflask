from flask import render_template

from . import webadmin


@webadmin.route('/')
def main():
    return 'adasdads'

@webadmin.route('/login/')
def login():

    return render_template('templates/admin/login.html')

@webadmin.route('/reg')
def reg():
    return render_template('templates/admin/reg.html')


