/*Script pra ser utilizada dentro do MYSQL WORKBEACH*/
/*Não possui relação com o arquivo Preparabanco.py que é o arquivo de articulação entre o back-end e o scrpit sql dentro do banco de dados, mas pode substituir por este código*/
CREATE TABLE jogos (
      id int(11) NOT NULL AUTO_INCREMENT,
      nome varchar(50) NOT NULL,
      categoria varchar(40) NOT NULL,
      console varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
);
CREATE TABLE usuarios (
  id int(11) NOT NULL AUTO_INCREMENT,
  nome varchar(20) NOT NULL,
  nickname varchar(8) NOT NULL,
  endereco VARCHAR(100),
  telefone VARCHAR(20),
  email VARCHAR(100),
  senha varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE termos (
  id int(11) NOT NULL AUTO_INCREMENT,
  lgpd boolean,
  PRIMARY KEY (`id`)
);
CREATE TABLE historico (
  id int(11) NOT NULL AUTO_INCREMENT,
  termosID VARCHAR(30),
  termosID2 VARCHAR(30),
  data datetime,
  termo_id int(11),
  usuario_id int(11),
  PRIMARY KEY (id),
  FOREIGN KEY (termo_id) REFERENCES termos(id),
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
select * from historico;
select * from termos;
select * from usuarios;
DESCRIBE termos;
use jogoteca;
drop table termos;
ALTER TABLE usuarios ADD COLUMN termo_id INT(11);
ALTER TABLE termos ADD COLUMN historico_id INTEGER;
ALTER TABLE usuarios MODIFY COLUMN nome VARCHAR(100) NOT NULL;
ALTER TABLE termos ADD COLUMN versao VARCHAR(30);



ALTER TABLE historico MODIFY COLUMN data datetime DEFAULT CURRENT_TIMESTAMP;