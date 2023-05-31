from jogoteca import db
from datetime import datetime 


class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


#class Usuarios(db.Model):
 #   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  #  nickname = db.Column(db.String(8), primary_key=True)
  #  nome = db.Column(db.String(20), nullable=False)
   # senha = db.Column(db.String(100), nullable=False)
    #lgpd = db.Column(db.Boolean, nullable=False)
    #termosID = db.Column(db.Integer, nullable=False)

    #def __repr__(self):
     #   return '<Name %r>' % self.nome

#class Termos(db.Model):
 #   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  #  lgpd = db.Column(db.Boolean, nullable=False)
   # termosID = db.Column(db.Integer, nullable=False)
   # criacao = db.Column(db.DateTime, default=datetime.utcnow())
   # versao = db.Column(db.String(12), nullable=False)
   # aceite = db.Column(db.Boolean, nullable=False)
   
class Termo(db.Model):
        id = db.Column(db.Integer, primary_key=True)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    nickname = db.Column(db.String(50)) 
    senha = db.Column(db.String(100))
    lgpd = db.Column(db.Boolean)
    termosID = db.Column(db.Integer, db.ForeignKey('termo.id'))
    termo = db.relationship('Termo', backref='usuarios')

    def __repr__(self):
        return '<Name %r>' % self.nome