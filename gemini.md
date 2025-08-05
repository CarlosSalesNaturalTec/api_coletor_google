Aplicação em Python + FastAPI para coletar dados de uma API do Google CSE e armazená-los em um banco de dados NoSQL.

Nome da aplicação: api_coletor_google

Hospedagem da aplicação: Google Cloud Run

Etapas para construção:
1 - Montar servidor em Python + FastAPI.
2 - Conectar-se com banco Firestore também hospedado na GCP.
3 - Obter no firestore a lista dos termos a serem pesquisados.
4 - Executar consulta dos termos junto à API Google CSE.
5 - Normalizar e filtrar os resultados obtidos.
6 - Salvar resultados no banco.
