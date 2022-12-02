from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators

class FormIngresso(FlaskForm):
    flamenguista = IntegerField('Flamenguista', [validators.DataRequired('Invalido')])
    adulto = IntegerField('Adulto', [validators.DataRequired('Invalido')])
    estudante = IntegerField('Estudante', [validators.DataRequired('Invalido')])
    infantil = IntegerField('Infantil', [validators.DataRequired('Invalido')])
    idoso = IntegerField('Idoso', [validators.DataRequired('Invalido')])
    comprar = SubmitField('Comprar')

    #É PRECISO VALIDAR, SE PELO MENOS UM INGRESSO FOI COMPRADO NO TOTAL