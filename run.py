from flask import Flask
from flask import request, redirect, render_template, url_for
# from app import app
from flask_assets import Environment, Bundle

# from config import DevelopmentConfig

import app/forms
# from app import forms

app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)
assets = Environment(app)
assets.config['less_bin'] = '/usr/lib/node_modules/less/bin/lessc'


@app.route('/')
def init():
    return render_template(
        'init.html'
    )


@app.route('/home')
def home():
    return render_template(
        'home.html'
    )


@app.route('/about')
@app.route('/about/<int:num1>/<int:num2>')
def about(num1=0, num2=0):
    contexto = {'num1': num1, 'num2': num2}
    return render_template(
        'about.html',
        **contexto
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print("Not in POST")

    return render_template(
        'contact.html',
        email="sruizdegopegui[at]gmail[dot]com",
        telefono="660 366 599",
        github="sarudego",
        form=comment_form
    )


@app.route('/skills')
def skills():
    return render_template(
        'skills.html',
        skill=[
            {"programming": "Python, AngularJS"},
            {"languages": "spanish, english"}
        ]

    )


@app.route('/extra')
def extra():
    return render_template(
        'extra.html'
    )


if __name__ == '__main__':
    app.run(port=8000)