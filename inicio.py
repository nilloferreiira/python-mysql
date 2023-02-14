import pymysql.cursors

con = pymysql.Connection(
    host="localhost",
    user="root",
    password="",
    port=3306,
    db="aulapf",
    charset="utf8mb4",
    cursorclass = pymysql.cursors.DictCursor)

def criarTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"create table {nomeTabela}(nome varchar(50))")
            print("Tabela criada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
#criarTabela('teste1')

def removerTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
            print("Tabela removida com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
#removerTabela('teste1')

def inserirValores():
    nome = input("Digite seu nome: ")
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste values('{nome}')")
        print("Valor inserido com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
#inserirValores()

def mostrarValores():
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM teste")
            resultado = cursor.fetchall()
            for i in resultado:
                print(i)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
#mostrarValores()

def alterarValores():
    nomeAlterar = input("Digite o nome que deseja alterar: ")
    nomeAlterado = input("Digite o nome para qual deseja alterar: ")
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE teste SET nome = '{nomeAlterado}' WHERE nome = '{nomeAlterar}'")
        print("Update feito!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
#alterarValores()

def deletarValores():
    delValue = input("Digite o valor que deseja remover: ")
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM teste WHERE nome = '{delValue}'")
        print("Valor removido com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
#deletarValores()

con.commit()
con.close()