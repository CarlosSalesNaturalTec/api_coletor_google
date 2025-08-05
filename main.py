from fastapi import FastAPI, Depends
from google.cloud.firestore_v1.client import Client
from database import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "api_coletor_google no ar!"}

@app.get("/test-firestore")
def test_firestore(db: Client = Depends(get_db)):
    # O nome da coleção é "termos_pesquisa"
    collection_ref = db.collection("termos_pesquisa")
    # Obter todos os documentos da coleção
    docs = collection_ref.stream()
    # Converter os documentos para uma lista de dicionários
    data = [doc.to_dict() for doc in docs]
    return {"data": data}
