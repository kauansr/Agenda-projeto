# Agenda-projeto
Uma agenda feita com python utilizando o framework django

## Como usar Windows CMD?
- Clone o projeto usando o comando: git clone https://github.com/kauansr/Agenda-projeto.git
- Abra o projeto em seu editor de codigo
- Utilize o comando: python -m venv venv, para criar seu ambiente virtual
- Entre no ambiente venv\scripts\activate.bat
- Instale os recursos que cujo nome estão disponiveis em requirements.txt
- Faca as migracoes usando o comando: python manage.py makemigrations, e depois, python manage.py migrate
- Talvez seja necessario fazer alteracoes na area do admin entao crie um superuser e as faca
- Para rodar a agenda use o comando: python manage.py runserver

## Como fazer o superuser ?
- Antes de rodar o site, use o comando: python manage.py createsuperuser, coloque as informacoes lá
- Rode o site com python manage.py runserver e acesse /admin