# affiliate-orchestrator

Sistema automatizado para gerar conteúdo afiliado com:

- geração de keywords via Google Suggest
- clusterização de conteúdo
- scraping de produtos da Amazon
- inserção de links afiliados
- geração de artigos com IA
- criação de Pillar + Supporting Articles
- publicação automática no WordPress (modo revisão)

---

# Requisitos

Python 3.11+

Verifique:

python --version

---

# Instalação

Clone o projeto:

git clone https://github.com/yourrepo/affiliate-orchestrator

Entre na pasta:

cd affiliate-orchestrator

Crie ambiente virtual:

python -m venv venv

Ative:

Linux/Mac

source venv/bin/activate

Windows

venv\Scripts\activate

Instale dependências:

pip install -r requirements.txt

---

# Configuração

Edite:

config/settings.py

Defina:

OPENAI_API_KEY
WORDPRESS_URL
WORDPRESS_USER
WORDPRESS_APP_PASSWORD
AMAZON_AFFILIATE_TAG

---

# Executar

python main.py

## Build do container
`docker compose build`

## Executar o orchestrator
`docker compose build`

## Executar manualmente
`docker compose run orchestrator python main.py`

## Rodar em background
`docker compose up -d`

## Logs
`docker compose logs -f`

## Rodar com cron
`0 3 * * * docker compose run orchestrator`

---

# O que o sistema faz

1 gera 500 keywords
2 cria clusters
3 encontra produtos na Amazon
4 gera artigos com IA
5 cria tabela comparativa
6 adiciona links afiliados
7 publica posts no WordPress em revisão

---

# Exemplo de execução

Seed keyword:

air fryer

Resultado:

500 keywords
clusters criados
produtos encontrados na Amazon
100 posts gerados
100 posts enviados para WordPress (pending review)

---

# Aviso

O scraping da Amazon deve respeitar limites de requisição.

Recomendado:

sleep 2-5 segundos entre requests