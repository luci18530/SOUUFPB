# SOUUFPB
Projeto de Engenharia de Software. O SouUFPB tem o objetivo de auxiliar os estudantes pré-universitários e universitários na escolha do curso na instituição.

Link do figma: https://www.figma.com/file/Z7iByvp71rHlWvBPBm1WhV/SouUFPB?type=design&node-id=0%3A1&mode=design&t=nHB8utxMlM3Xhkut-1

## Instruções para rodar o projeto (Windows)

### Download do PostgreSQL
Link para download: https://www.postgresql.org/download/

Na instalação: configurar senha, porta, etc. conforme DATABASES em "settings.py", ou alterar o arquivo de configuração para corresponder aos valores definidos.

### Acessar a pasta do PostgreSQL e entrar com usuário 'postgres' (utillizar a senha definida na instalação)
```
cd C:\Program Files\PostgreSQL\16\bin 
psql -U postgres
```

### Criar banco de dados 'souufpb' e, conectado a ele, ativar a extensão 'unaccent'
```
CREATE DATABASE souufpb;
\c souufpb
CREATE EXTENSION unaccent;
```

### Clonar repositório na pasta em que deseja armazenar os arquivos do projeto
```
git clone https://github.com/luci18530/SOUUFPB.git
cd SOUUFPB/souUfpb
```

### Criar ambiente virtual
```
python -m venv .venv
.venv\Scripts\activate
```

### Instalar dependências
```
pip install django
pip install psycopg2-binary
pip install django-widget-tweaks
```

### Criar as tabelas do banco de dados, preencher com as informações e rodar o projeto
```
py manage.py migrate
py manage.py fill_database
py manage.py runserver
```
