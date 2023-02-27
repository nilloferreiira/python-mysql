from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "aulapf"
PORT = 3306

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    user = Column(String(20))
    senha = Column(String(10))

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True)
    categoria = Column(String(50))

class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True)
    produto = Column(String(50))  
    idCategoria = Column(Integer, ForeignKey('categoria.id'))
    
Base.metadata.create_all(engine)