from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

from wtforms import validators


class CommentForm(Form):
    username = StringField('Username',
            [
                validators.DataRequired(message='El username es requerido.'),
                validators.length(min=4, max=25, message="Ingrese un username válido, 4 carácteres mínimo.")
            ])
    email = EmailField('Email',
            [
                validators.Required(message='El email es requerido.'),
                validators.Email(message="Ingrese un email válido.")
            ])
    comment = TextField('Comentario')
