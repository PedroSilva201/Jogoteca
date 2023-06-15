import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
      )
      #Os dados de host, user e password podem variar de maquina pra maquina conforme necessidade dos porgramadores
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()#como coletar dados do radio-button em python para o banco de dados mysql

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute("CREATE DATABASE `jogoteca`;")

cursor.execute("USE `jogoteca`;")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
      CREATE TABLE `jogos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `senha` varchar(100) NOT NULL,
      `lgpd` boolean NOT NULL,
      `termos_id` INT.
      PRIMARY KEY (`id`)
      FOREIGN KEY (termos_id) REFERENCES termos(id)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')
#CREATE TABLE usuarios (
#      id int(11) NOT NULL AUTO_INCREMENT,
#      nome varchar(20) NOT NULL,
#      nickname varchar(8) NOT NULL,
#      senha varchar(100) NOT NULL,
#      lgpd boolean NOT NULL,
#      termosID varchar(12) not null,
#      PRIMARY KEY (`id`)
#      );
# criado em 31/05/2023 (rascunho)

#Ao criar registros na tabela "usuarios", você pode preencher o campo termos_id com o valor do id correspondente na tabela "termos" para estabelecer a interligação entre os registros das duas tabelas.
TABLES['Termos'] = ('''
      CREATE TABLE `termos`(
      `id` int NOT NULL AUTO_INCREMENT,
      `criacao` DATETIME DEFAULT CURRENT_TIMESTAMP,
      `versao` varchar(12) NOT NULL,
      `aceite` bool NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')
#CREATE TABLE termos(
#     id int NOT NULL AUTO_INCREMENT,
#      criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
#      versao varchar(12) NOT NULL,
#      aceite bool NOT NULL,
#      PRIMARY KEY (`id`));
# criado em 31/05/2023 (rascunho)
for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha, LGPD) VALUES (%s, %s, %s)'
usuarios = [
      ("Administrador", "ADM", generate_password_hash("administracao").decode('utf-8'),("Sim")),
      ("Ferreira Ferraz", "FF", generate_password_hash("poa").decode('utf-8'),("Sim")),
      ("Estagiario", "ES", generate_password_hash("trainner").decode('utf-8'),("Sim")),
      ("Julia Juliana", "JJ", generate_password_hash("ruiva").decode('utf-8'),("Sim"))
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Valorant', 'FPS', 'PC'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# inserindo termos

termos_sql = 'INSERT INTO termos (criacao, versao, aceite) VALUES (%s, %s, %s)'
termos = [
      ('15/02/2023 19:25', '1.0.0', 'Sim'),
      ('15/02/2023 19:30', '1.0.0', 'Sim'),
]
cursor.executemany(termos_sql, termos)

cursor.execute('select * from jogoteca.termos')
print(' -------------  Termos:  -------------')
for termos in cursor.fetchall():
    print(termos[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()