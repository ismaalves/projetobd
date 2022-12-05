from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField, FloatField, DateField, validators
from models2 import Cliente, Venda


class FormIngresso(FlaskForm):
    flamenguista = IntegerField('Flamenguista', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    adulto = IntegerField('Adulto', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    estudante = IntegerField('Estudante', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    infantil = IntegerField('Infantil', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    idoso = IntegerField('Idoso', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)], default=0)
    comprar = SubmitField('Comprar')


class FormVenda(FlaskForm):
    idVenda = IntegerField('ID da Venda', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)])
    fkCliente = SelectField('ID do Cliente', choices=[], default=None, validate_choice=False)
    tipoPagamento = SelectField('Tipo de Pagamento', [validators.DataRequired('Invalido')], choices=[('Credito', 'Credito'), ('Debito', 'Debito'), ('Dinheiro', 'Dinheiro')])
    estado = StringField('Estado de Pagamento', [validators.DataRequired('Invalido')])
    total = FloatField('Total da Venda', [validators.DataRequired('Invalido'), validators.NumberRange(min=0)])
    data_venda = DateField('Data da Venda', [validators.DataRequired('Invalido')])
    pagar = SubmitField('Prosseguir')
