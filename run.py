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

@app.route('/index')
def index():
    return render_template( 'index.html')



@app.route('/home')
def home():
    return render_template(
        'home.html'
    )


# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
    # comment_form = forms.CommentForm(request.form)
    # if request.method == 'POST' and comment_form.validate():
        # print(comment_form.username.data)
        # print(comment_form.email.data)
        # print(comment_form.comment.data)
    # else:
        # print("Not in POST")

    # return render_template(
        # 'contact.html',
        # email="sruizdegopegui[at]gmail[dot]com",
        # telefono="660 366 599",
        # github="sarudego",
        # form=comment_form
    # )


@app.route('/extra')
def extra():
    return render_template(
        'extra.html'
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(port=8000)

