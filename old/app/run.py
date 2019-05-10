from flask import Flask
from flask import render_template
# from flaskext.lesscss import lesscss
#from app import app

from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# lesscss(app)


@app.route('/')
def index():
    return render_template(
            'index.html'
            )

@app.route('/about')
def about():
    return render_template(
            'about.html'
            )

@app.route('/projects')
def projects():
    return render_template(
            'projects.html'
            )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    # ConvStylus() # ('path')
    # print(app.root_path)
    # print(app.secret_key)
    # print(app.static_url_path)
    # print(app.static_folder)
    app.run(port=8000)

