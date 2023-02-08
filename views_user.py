from jogoteca import app, db 
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario, FormularioCadastro
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
        nickname = form.nickname.data
        senha = generate_password_hash(form.senha.data).decode('utf-8')
        novo_usuario = Usuarios(nome = nome, nickname = nickname, senha = senha)
        db.session.add(novo_usuario)
        db.session.commit()
        flash(nickname + ' cadastrado com sucesso!')
        return redirect(url_for('index'))
    else: 
        flash(nickname + 'Usuario ja cadastrado!')
        return redirect(url_for('novo_usuario'))
    
#criaçao de uma rota para completar o cadastro do usuario no site (se houver necessidade)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    elif senha:
        flash('Senha não cadastrada')
        return redirect(url_for('login'))
#aumentar o tamanho do laço para usar os itens abaixo, nao estao retornando a pagina de login em caso de erro
    elif usuario:
        flash('Usuario não cadastrado.')
        return redirect(url_for('login'))
    else:
        flash('Usuario e senha não cadastradas')
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

#@app.route('Acesso_Restrito')
#def usuarios():
#    return redirect(url_for('usuarios.html'))

#ROTA PARA DELETAR O CADASTRO DO USUARIO CONFORME A LESGISLAÇAO
#@app.route('/deletar/<int:id>')
#def deletar(id):
#    if 'usuario_logado' not in session or session['usuario_logado'] == None:
#        return redirect(url_for('login'))
#
#    Usuarios.query.filter_by(id=id).delete()
#    db.session.commit()
#    flash('Jogo deletado com sucesso!')
#
#    return redirect(url_for('index'))

#@app.route('/editar/<int:id>')
#def editar(id):
    #if 'usuario_logado' not in session or session['usuario_logado'] == None:
        #return redirect(url_for('login', proxima=url_for('editar', id=id)))
    #jogo = Jogos.query.filter_by(id=id).first()
    #form = FormularioJogo()
    #form.nome.data = jogo.nome
    #form.categoria.data = jogo.categoria
    #form.console.data = jogo.console
    #capa_jogo = recupera_imagem(id)
    #return render_template('editar.html', titulo='Editando Jogo', id=id, capa_jogo=capa_jogo, form=form)

#@app.route('/atualizar', methods=['POST',])
#def atualizar():
    #form = FormularioJogo(request.form)

    #if form.validate_on_submit():
        #jogo = Jogos.query.filter_by(id=request.form['id']).first()
        #jogo.nome = form.nome.data
        #jogo.categoria = form.categoria.data
        #jogo.console = form.console.data

        #db.session.add(jogo)
        #db.session.commit()

        #arquivo = request.files['arquivo']
        #upload_path = app.config['UPLOAD_PATH']
        #timestamp = time.time()
        #deleta_arquivo(id)
        #arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')

    #return redirect(url_for('index'))

#@app.route('/deletar/<int:id>')
#def deletar(id):
    #if 'usuario_logado' not in session or session['usuario_logado'] == None:
        #return redirect(url_for('login'))

    #Jogos.query.filter_by(id=id).delete()
    #db.session.commit()
    #flash('Jogo deletado com sucesso!')

    #return redirect(url_for('index'))