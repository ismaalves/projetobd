from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField, FloatField, DateField, validators
from wtforms.validators import DataRequired
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


class FormBusca(FlaskForm):
    searched = StringField("Pesquisar", [validators.DataRequired('Invalido')])
    submit = SubmitField('Buscar')
    
class cadastrofilmeForm(FlaskForm):
    
    nome = StringField("Nome", validators=[DataRequired()])

    classificacao = IntegerField("Classificacao", validators=[DataRequired()])
    duracao = IntegerField("Duracao", validators=[DataRequired()])
    ano = IntegerField("Ano", validators=[DataRequired()])
    
    sinopse = StringField("Sinopse", validators=[DataRequired()])
    nacionalidade = SelectField(u"Nacionalidade", choices = [('Nacional'), ('Estrangeiro')], validators=[DataRequired()])
    produtor = StringField("Produtor", validators=[DataRequired()])
    diretor = StringField("Diretor", validators=[DataRequired()])

    genero = SelectField(u"Gênero (1-Comédia 2-Romance 3-Ação 4-Aventura 5-Fantasia 6-Terror )",choices = [(1), (2), (3), (4), (5), (6)], validators=[DataRequired()])
    atores = StringField("Atores", validators=[DataRequired()])
    img = StringField("Imagem", validators=[DataRequired()])
    
    cadastrar = SubmitField('Cadastrar')

class cadastrosessaoForm(FlaskForm):
    
    experiencia = SelectField("Experiência", choices=[('VIP'), ('IMAX'), ('MACRO EX')], validators=[DataRequired()])
    formato = SelectField("Formato", choices=[('2D'), ('3D')], validators=[DataRequired()])
    idioma = SelectField("Idioma", choices=[('LEGENDADO'), ('DUBLADO')], validators=[DataRequired()])

    salas = SelectField('Sala',choices=[], validators=[DataRequired()])
    filmes = SelectField('Filme',choices=[], validators=[DataRequired()])
    horarios = SelectField('Horario',choices=[], validators=[DataRequired()])

    dia = DateField('Data', validators=[DataRequired()])
    valor = IntegerField('Valor', validators=[DataRequired()])
    disponibilidade = IntegerField('Disponibilidade', validators=[DataRequired()])

    cadastrar2 = SubmitField('Cadastrar')
