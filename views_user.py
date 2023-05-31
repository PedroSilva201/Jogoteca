from jogoteca import app, db 
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario, FormularioCadastro, FormularioTermos
from flask_bcrypt import check_password_hash, generate_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/novo_usuario')
def novo_usuario():
    form = FormularioCadastro()
    return render_template('cadastrar.html', form=form)

@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    proxima = request.args.get('proxima')
    form = FormularioCadastro()
    #cadastro de usuarios
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    print (usuario)
    if not usuario:
        nome = form.nome.data
        senha = form.senha.data
        nickname = form.nickname.data
        lgpd = form.LGPD.data
        termosID = form.termosID.data
        print(termosID)
        #certification = form.certification.data
        print(lgpd)
        senha = generate_password_hash(form.senha.data).decode('utf-8')
        print(senha)
        novo_usuario = Usuarios(nome = nome, nickname = nickname, senha = senha, lgpd = lgpd, termosID = termosID)
        db.session.add(novo_usuario)
        db.session.commit()
        flash(nickname + ' cadastrado com sucesso!')
        return redirect(url_for('login'))
    else:
        #sem valor de retorno
        flash('Usuario ja cadastrado!')
        return redirect(url_for('novo_usuario'))
    
#@app.route('/cadastrartermos', methods=['POST',])
#def cadastrarTermos():
#    proxima = request.args.get('proxima')
#    form = FormularioTermos()
#    #cadastro de termos
#    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
#    print(usuario)
#    if not usuario:
#        lgpd = form.LGPD.data
#        termosID = form.termosID.data
#        print(termosID)
#        #certification = form.certification.data
#        print(lgpd)
#        novo_usuario = Usuarios( lgpd = lgpd, termosID = termosID)
#        db.session.add(novo_usuario)
#        db.session.commit()
#        return redirect(url_for('login'))
@app.route('/usuario', methods=['POST'])
def create_usuario():
    nome = request.json.get('nome')
    senha = request.json.get('senha')

    termo = termosLGPD()
    db.session.add(termo)
    db.session.flush()

    usuario = Usuarios(nome=nome, senha=senha, termo_id=termo.id)
    db.session.add(usuario)
    db.session.commit()

    return 'Usuário criado com sucesso'

    
#criaçao de uma rota para completar o cadastro do usuario no site (se houver necessidade)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    if usuario == None :
       flash('Usuario nao encontrado.')
       return redirect(url_for('login'))
    else : 
        print ('usuario', usuario)
        senha = check_password_hash(usuario.senha, form.senha.data) 
        print ('senha', senha)
        if usuario and senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!/logada com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        #funciona
        else :
            flash('Usuario ou senha não cadastradas.')
            return redirect(url_for('login'))
 
@app.route('/logout')
def logout():
    session['usuario_logado'] #= logout()
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

#PARTE DE SEGURANÇA DO SITE
#ROTA PARA OS TERMOS DA LGPD

@app.route('/LGPD')
def termosLGPD():
    return render_template('LGPD.html')

@app.route('/cookies')
def acessarcookies():
    return render_template('cookies.html')

@app.route('/Buscar_Usuarios')
def buscar_usuarios():
    usuarios = Usuarios.query.all()
    return render_template('teste.html', usuarios=usuarios)


@app.route('/editar_usuario/<int:id>')
def editar_usuario(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar_usuario', id=id)))
    usuario = Usuarios.query.filter_by(id=id).first()
    form = FormularioCadastro()
    form.nome.data = usuario.nome
    form.nickname.data = usuario.nickname
    return render_template('editarusuarios.html', titulo='Editando Usuario', id=id, form=form)
#ROTA PARA DELETAR O CADASTRO DO USUARIO CONFORME A LESGISLAÇAO
@app.route('/atualizar_usuario', methods=['POST',])
def atualizar_usuario():
    form = FormularioCadastro(request.form)
     
    usuario = Usuarios.query.filter_by(id=request.form['id']).first()
    usuario.nome = form.nome.data
    usuario.nickname = form.nickname.data
    usuario.termosID = form.termosID.data
                                                
 
    db.session.add(usuario)
    db.session.commit()
        

    return redirect(url_for('buscar_usuarios'))

@app.route('/deletar_usuario/<int:id>')
def deletar_usuario(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Usuarios.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Usuario deletado com sucesso!')

    return redirect(url_for('buscar_usuarios'))


