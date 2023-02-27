from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import Pessoa, Categoria, Produto
from sqlalchemy import or_

def RetornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapf"
    PORT = 3306
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSession() 

''' add um item na tabela
x = Pessoa(nome='danillo', user='dan', senha='1234')
session.add(x) # session.add_all([x, y])
#session.rollback() serve para limpar a session!
session.commit()
'''
def CadastrarCategoria():
    cat = input("Digite a categoria que deseja cadastrar: ")

    teste = session.query(Categoria).filter(Categoria.categoria == cat).all()
    if len(teste) > 0:
        print("A categoria que deseja cadastrar já existe!")
    else:
        x = Categoria(categoria=cat)
        session.add(x)
        session.commit()
        print("Categoria cadastrada com sucesso!")
#CadastrarCategoria()

def CadastrarProduto():
    produto = input("Digite o nome do produto que deseja cadastrar: ")
    catP = int(input("Digite o id da categoria do produto que deseja cadastrar: "))
    teste = session.query(Produto).filter(Produto.produto == produto).all()
    if len(teste) > 0:
        print("O produto que deseja cadastrar já existe!")
    else:
        x = Produto(produto=produto, idCategoria=catP)
        session.add(x)
        session.commit()
        print("Produto cadastrado com sucesso!")
#CadastrarProduto()

''' mostrar um item específico dentro da tabela
x = session.query(Pessoa).all()
#x = session.query(Pessoa).filter(Pessoa.nome == "danillo")
x = session.query(Pessoa).filter_by(nome = "danillo", user = "dan")
for i in x:
    print(i.id)
'''

def MostrarCategoria():
    cat = session.query(Categoria).all()
    for i in cat:
        print(f"Categoria({i.id}): {i.categoria}")
#MostrarCategoria()

def MostrarProduto():
    x = int(input("Digite o id do produto que deseja mostrar: "))
    produto = session.query(Produto).filter(Produto.id == x).all()
    if len(produto) <= 0:
        print("O produto que deseja não está cadastrado!")
    else:
        
        for i in produto:
            print(i.produto)
#MostrarProduto()


''' usar o operador OR dentro do banco de dados
x = session.query(Pessoa).filter(or_(Pessoa.nome == 'dani', Pessoa.nome == 'danillo')).all()

for i in x:
    print(i.senha)
'''

'''alterar um item dentro do banco de dados
x = session.query(Pessoa).filter(Pessoa.id == 1).all()
x[0].nome = "dani"
session.commit()
print(x[0].nome)
'''

def AlterarCategoria():
    catAlterar = int(input("Digite o id da categoria que deseja alterar: "))
    novaCat = input("Digite a nova categoria: ")

    tsId = session.query(Categoria).filter(Categoria.id == catAlterar).all()
    if len(tsId) <= 0:
        print("A categoria que deseja alterar não existe!")
    else:
        tsNc = session.query(Categoria).filter(Categoria.categoria == novaCat).all()
        if len(tsNc) > 0:
            print("A categoria para qual deseja alterar já existe!")
        else:
            tsId[0].categoria = novaCat
            session.commit()
            print("Categoria alterada com sucesso")
    
#AlterarCategoria()

def AlterarProduto():
    prodAlterar = int(input("Digite o id do produto que deseja alterar: "))
    novoProduto = input("Digite o novo produto: ")
    novaCatProduto = int(input("Digite o id da nova categoria do produto: "))

    tsId = session.query(Produto).filter(Produto.id == prodAlterar).all()
    if len(tsId) <= 0:
        print("O produto que deseja alterar não existe!")
    else:
        tsNp = session.query(Produto).filter(Produto.produto == novoProduto).all()
        if len(tsNp) > 0:
            print("O Produto que deseja alterar já existe!")
        else:
            tsIdCat = session.query(Produto).filter(Produto.idCategoria == novaCatProduto).all()
            if len(tsIdCat) <=0 :
                print("Categoria do produto não existe!")
            else:
                tsId[0].produto = novoProduto
                tsId[0].idCategoria = novaCatProduto
                session.commit()
                print("Produto alterado com sucesso!")

#AlterarProduto()

''' Deletar um item especifico de uma tabela
x = session.query(Pessoa).filter(Pessoa.id == 1).one() #vai trazer apenas um item da lista

session.delete(x)
session.commit() # precisa fazer para atualizar o banco de dados
'''

def DeletarCategoria():
    x = int(input("Digite o id da categoria que deseja remover: "))
    
    try:
        Del = session.query(Categoria).filter(Categoria.id == x).one()
        
        session.delete(Del)
        session.commit()
        print("Categoria removida com sucesso!")
    except:
        print("A categoria que deseja remover não existe!")
#DeletarCategoria()

def DeletarProduto():
    x = int(input("Digite o id do produto que deseja remover: "))
     
    try:
        Del = session.query(Produto).filter(Produto.id == x).one()

        session.delete(Del)
        session.commit()
        print("Produto removido com sucesso!")
    except:
        print("O produto que deseja remover não existe!")
#DeletarProduto()