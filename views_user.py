from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario, FormularioCadastro
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/cadastrar')
def cadastrar():
    proxima = request.args.get('proxima')
    form = FormularioCadastro()
    #cadastro de usuarios
    #usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    #senha = check_password_hash(usuario.senha, form.senha.data)
    #if usuario and senha:
    #    session['usuario_cadastrado'] = usuario.nickname
    #    flash(usuario.nickname + ' cadastrado com sucesso!')
    return render_template('cadastrar.html', proxima=proxima, form=form)
    
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

#def logout():
#    session['usuario_cadastrado']
#    flash('Logout efetuado com sucesso!')
#    return redirect(url_for('index'))

@app.route('/LGPD')
def termosLGPD():
    return render_template('LGPD.html')