from flask import Flask
from flask_webpack import Webpack
from flask import request, redirect, render_template, url_for
# from app import app

from config import DevelopmentConfig
# from flaskext.stylus2css import stylus2css stylus2css(app, css_folder=’css’, stylus_folder=’src/stylus’)
# from live_stylus import ConvStylus

import forms

webpack = Webpack()


app = Flask(__name__)
# webpack.init_app(app)
app.config.from_object(DevelopmentConfig)
# if app.debug:
    # from flaskext.stylus2css import stylus2css 
    # stylus2css(app)


@app.route('/')
def index():
    return render_template(
            'index.html'
            )


@app.route('/home')
def home():
    return render_template(
            'home.html'
            )


@app.route('/skills')
def skills():
    return render_template(
            'skills.html'
						)


@app.route('/extra')
def extra():
    return render_template(
            'extra.html'
            )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# @app.route('/about')
# @app.route('/about/<int:num1>/<int:num2>')
# def about(num1=0, num2=0):
    # contexto = {'num1': num1, 'num2': num2}
    # return render_template(
            # 'about.html',
            # **contexto
            # )


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


if __name__ == '__main__':
    # ConvStylus() # ('path')
    app.run(port=8000)

