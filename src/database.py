#Bibliotecas
import sqlite3

# Parte 1 - Criação do banco de dados
# Nessa fase, para fins de aprendizado vamos utilizar a biblioteca sqlite3
# do python, para as operações de criação e manipulação do banco de dados.

## Criação e conexão
# O .connect() cria nosso banco caso não exista e estabelece uma conexão segura,
# ele apenas estabelecerá apenas se o banco já exista. 
conn = sqlite3.connect("corretorasbr.db")

# Criamos aqui nosso cursor (com o auxílio do método .cursor()) que será o mensageiro 
# responsável por enviar nossos comandos ao banco.
cursor = conn.cursor()

# Aqui usamos o método .commit() que salvará toda ação e modificação realizada dentro do banco.
conn.commit()
print("Banco de dados de CEP's nacionais criado com sucesso!")


## Criação da tabela Corretoras 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS CORRETORAS(
        CORRETORA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME_COMERCIAL VARCHAR(30) NOT NULL,
        EMAIL VARCHAR(30) NOT NULL,
        TELEFONE VARCHAR(30) NOT NULL       
               )
""")

# o método .close() fecha de forma segura nossa conexão para evitar vazamento de dados e
# desperdício de memória.
conn.close()