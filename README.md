# SOUUFPB
Projeto de Engenharia de Software. O SouUFPB tem o objetivo de auxiliar os estudantes pré-universitários e universitários na escolha do curso na instituição.

Link do figma: https://www.figma.com/file/Z7iByvp71rHlWvBPBm1WhV/SouUFPB?type=design&node-id=0%3A1&mode=design&t=nHB8utxMlM3Xhkut-1

# Instruções para rodar o projeto (Windows)
```
git clone https://github.com/luci18530/SOUUFPB.git
cd SOUUFPB/souUfpb

python -m venv .venv
.venv\Scripts\activate

pip install django
pip install psycopg2-binary
pip install django-widget-tweaks

py manage.py migrate
py manage.py fill_database
py manage.py runserver
```
