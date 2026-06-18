import sqlite3

## Manipulação de dados no banco.
try: 
    def data_insertion():
        with sqlite3.connect('corretorasbr.db') as conn:
         cursor = conn.cursor()
         cursor.execute("""INSERT INTO CORRETORAS (CORRETORA_ID, NOME_COMERCIAL, EMAIL, TELEFONE) VALUES (?, ?, ?, ?), ()        
""")
        conn.commit()
        print("Inserções OK!")
except sqlite3.IntegrityError as e:
    print("Erro na inserção de dados, verifique a fonte de informações e o código atual.")