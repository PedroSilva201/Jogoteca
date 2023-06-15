from jogoteca import db
from datetime import datetime 


class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

#adicionar usu_nome_da_tabela
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    nickname = db.Column(db.String(50))
    endereco = db.Column(db.String(100))
    telefone = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    termo_id = db.Column(db.Integer, db.ForeignKey('termos.id'))
    termo = db.relationship('Termos', backref='usuario')
    #
    #versao = db.Column(db.String(30))
    
class Termos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lgpd = db.Column(db.Boolean)
    historico_id = db.Column(db.Integer, db.ForeignKey('historico.id'))
    historico = db.relationship('Historico', backref='termo')
    versao = db.Column(db.String(30))
    
class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    termosID = db.Column(db.String(30))
    termosID2 = db.Column(db.String(30))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.relationship('Usuarios', backref='historico')
    #data = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __repr__(self):
        return '<Name %r>' % self.nome