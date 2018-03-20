from flask import Flask
app = Flask(__name__)
from app import views # esta linea siempre al final

# from config import DevelopmentConfig

# app.config.from_object(DevelopmentConfig)




