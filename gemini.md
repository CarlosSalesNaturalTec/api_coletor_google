Aplicação em Python + FastAPI para coletar dados de uma API do Google CSE e armazená-los em um banco de dados NoSQL.

Nome da aplicação: api_coletor_google

Hospedagem da aplicação: Google Cloud Run

Ambiente de desenvolvimento: Windows

Instruções Detalhadas:

1 - Montar servidor em Python + FastAPI.
2 - Conectar-se com banco Firestore também hospedado na GCP. Utilize .ENV para credenciais. Faça a conexão com o banco de maneira que possa ser reaproveitada pelo código em outras etapas.
3 - Obter no firestore a lista dos termos a serem pesquisados e executar consulta dos termos junto à API Google CSE.
4 - Normalizar e filtrar os resultados obtidos.
5 - Salvar resultados no banco.

