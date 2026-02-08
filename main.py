from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

'''
ARMAZENAMENTO E COLETA DE INFORMAÇÕES DE UM DATABASE
BASE DAS INFORMAÇÕES: https://www.megaleiloes.com.br

POST:
    - NOME
    - LOCAL
    - CATEGORIA
    - LEILOEIRO
    - VALOR INICIAL
    - CÓDIGO DO LOTE
'''

# DEFINIÇÃO DO MODELO DE DADOS PARA VALIDAÇÃO DA API
class info(BaseModel):
    nome: str
    local: str
    categoria: str
    leiloeiro: str
    valor_init: str
    codigo_do_lote: int

# CONFIGURAÇÃO DA CONEXÃO COM O MONGODB E ACESSO À COLEÇÃO
con = MongoClient("mongodb://localhost:27017/")
db = con.get_database("info_leiloes")
col = db.get_collection("dados")
app = FastAPI()

@app.get("/")
def home():
    return {"data":"Server online", "code":200}

# ENDPOINT PARA RECUPERAR TODOS OS DADOS ARMAZENADOS
@app.get("/leilões")
def get_info():
    dados = list(col.find())

    # TRATAMENTO DO ID DO MONGODB PARA FORMATO JSON
    for item in dados:
        item["_id"] = str(item["_id"])
    try:
        return {"data": dados, "code": 200}
    except Exception as e:
        return {"Error": e, "code": 500}

# ENDPOINT PARA RECEBER E SALVAR NOVOS LEILÕES
@app.post("/leilões")
def post_info(inputs: info):
    dados = {
        "nome":inputs.nome,
        "local":inputs.local,
        "categoria":inputs.categoria,
        "leiloeiro":inputs.leiloeiro,
        "valor inicial":inputs.valor_init,
        "codigo do lote":inputs.codigo_do_lote
    }
    try:
        col.insert_one(dados)
        return {"nome":inputs.nome, "code":200}
    except Exception as e:
        return {"Error":str(e), "code":400}

if __name__ ==  "__main__":
    # EXECUÇÃO DO SERVIDOR ASGI NA PORTA 8001
    uvicorn.run(app, port=8001)
