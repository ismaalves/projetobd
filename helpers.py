from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators

class FormIngresso(FlaskForm):
    flamenguista = IntegerField('Flamenguista', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    adulto = IntegerField('Adulto', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    estudante = IntegerField('Estudante', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    infantil = IntegerField('Infantil', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    idoso = IntegerField('Idoso', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    comprar = SubmitField('Comprar')
