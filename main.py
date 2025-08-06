from fastapi import FastAPI, Depends, HTTPException
from google.cloud.firestore_v1.client import Client
from database import get_db
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = FastAPI()

# Chave de API do Google e ID do Mecanismo de Pesquisa Personalizado
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CUSTOM_SEARCH_ENGINE_ID = os.getenv("CUSTOM_SEARCH_ENGINE_ID")

@app.get("/")
def read_root():
    return {"message": "api_coletor_google no ar!"}

@app.post("/coletar-dados")
def coletar_dados(db: Client = Depends(get_db)):
    try:
        # Obter termos de pesquisa do Firestore
        termos_ref = db.collection("termos_pesquisa")
        termos_docs = termos_ref.stream()
        termos = [doc.to_dict().get("termos") for doc in termos_docs]

        if not termos:
            raise HTTPException(status_code=404, detail="Nenhum termo de pesquisa encontrado no Firestore.")

        resultados_finais = []

        # Consultar a API do Google CSE para cada conjunto de termos
        for termo in termos:
            if termo and isinstance(termo, list):
                query_string = " ".join(termo)                
                search_url = "https://www.googleapis.com/customsearch/v1"
                params = {
                    "key": GOOGLE_API_KEY,
                    "cx": CUSTOM_SEARCH_ENGINE_ID,
                    "q": query_string
                }
                response = requests.get(search_url, params=params)
                response.raise_for_status()  # Lança exceção para respostas de erro
                resultados = response.json().get("items", [])

                # Salvar resultados no Firestore
                for resultado in resultados:
                    # Aqui você pode normalizar e filtrar os dados conforme necessário
                    db.collection("resultados_pesquisa").add(resultado)
                resultados_finais.extend(resultados)

        return {"message": "Dados coletados e salvos com sucesso!", "resultados": len(resultados_finais)}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar a API do Google: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro: {e}")