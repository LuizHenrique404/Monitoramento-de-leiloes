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

class info(BaseModel):
    nome: str
    local: str
    categoria: str
    leiloeiro: str
    valor_init: str
    codigo_do_lote: int

con = MongoClient("mongodb://localhost:27017/")
db = con.get_database("info_leiloes")
col = db.get_collection("dados")
app = FastAPI()

@app.get("/")
def home():
    return {"data":"Server online", "code":200}

@app.get("/leilões")
def get_info():
    dados = list(col.find())

    for item in dados:
        item["_id"] = str(item["_id"])
    try:
        return {"data": dados, "code": 200}
    except Exception as e:
        return {"Error": e, "code": 500}

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
    uvicorn.run(app, port=8001)