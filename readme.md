# api_coletor_google

Aplicação em Python + FastAPI para coletar dados de uma API do Google CSE e armazená-los em um banco de dados NoSQL.

## Para testar localmente: 

$ uvicorn main:app --reload

Acesse no navegador: http://127.0.0.1:8000

## Obter credencial de acesso ao banco de dados

* Console do Google Cloud Platform
* IAM e Administrador
* Contas de Serviço 
* Default compute service account  (Caso não exista, é necessário subir algum deploy de aplicativo que o próprio sistema cria a conta)
* Clicar em ... Ações / Gerenciar Chaves
* Adicionar chave / criar nova chave / JSON 
* Será realizado um download automático do arquivo JSON
* Salvar arquivo JSON com credencial