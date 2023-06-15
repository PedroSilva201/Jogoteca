import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, validators, RadioField

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

class FormularioCadastro(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=50)])
    nickname = StringField('Nickname (Apelido que deseja colocar durante o uso)', [validators.DataRequired(), validators.Length(min=1, max=8)])
    endereco = StringField('Endereço',[validators.DataRequired(), validators.Length(min=1, max=100)])
    confirmarendereco = StringField('Confirmar Endereço',[validators.DataRequired(), validators.Length(min=1, max=100)])
    telefone = StringField('Telefone',[validators.DataRequired(), validators.Length(min=1, max=15)])
    confirmartelefone = StringField('Confirmar Telefone',[validators.DataRequired(), validators.Length(min=1, max=15)])
    email = StringField('E-mail',[validators.DataRequired(), validators.Length(min=1, max=50)])
    confirmaremail = StringField('Confirmar E-mail',[validators.DataRequired(), validators.Length(min=1, max=50)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    confirmarsenha = PasswordField('Confirmar senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    LGPD = BooleanField('Ao aceitar, você deverá concordar com nossa política de privacidade e os nossos termos de uso de acordo com a legislação bem como a coleta destes dados durante o ato.', [validators.DataRequired()])
    termosID = RadioField('', choices=[('Sim','Sim'),('Não','Não')], validators=[validators.DataRequired()])#termosID usará este campo de seleção
    termosID2 = RadioField('', choices=[('Sim','Sim'),('Não','Não')], validators=[validators.DataRequired()])#termosID usará este campo de seleção
    versao = RadioField('', choices=[('1.0','Versão 1.0')], validators=[validators.DataRequired()])
    cadastro = SubmitField('Cadastrar usuario')
    salvar = SubmitField('Salvar')
    
#class FormularioTermos(FlaskForm):
#    LGPD = BooleanField('Ao aceitar, você deverá concordar com nossa política de privacidade e os nossos termos de uso de acordo com a legislação bem como a coleta destes dados durante o ato.', [validators.DataRequired()])
#    termosID = RadioField('', choices=[('Versão 1.0','Versão 1.0'),('Versão 2.0','Versão 2.0')])#termosID usará este campo de seleção
#Jogos
def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH']), arquivo)