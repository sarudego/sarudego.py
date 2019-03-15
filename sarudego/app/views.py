from flask import render_template
from app import app

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


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


if __name__ == '__main__':
    # ConvStylus() # ('path')
    app.run(port=8000)

