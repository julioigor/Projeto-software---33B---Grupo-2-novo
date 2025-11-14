🇵🇹 README — Projeto Django + SQLite + API de Companhias

Este projeto utiliza Django e SQLite para criar uma API simples que permite:

Criar uma companhia

Consultar uma companhia

Gerenciar todas as tabelas via Django Admin

Trabalhar com modelos baseados em UUID

Usar uma base de dados SQLite incluída no repositório

📦 1. Requisitos

Python 3.10+ instalado

pip atualizado

Virtualenv recomendado

🛠 2. Instalação
macOS / Linux
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install django

Windows (PowerShell)
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install django

🚀 3. Inicializar o projeto (já feito)

O projeto contém:

backend/
 ├── backend/
 ├── core/
 ├── db.sqlite3
 ├── manage.py
 └── README.md

🧩 4. Modelos existentes

O projeto inclui modelos para:

Companhia

Usuario

Servico

Localizacao

Problema

Com chaves primárias em UUID e timestamps automáticos.

🔧 5. Migrações (caso necessário)
python manage.py makemigrations
python manage.py migrate

🔐 6. Criar um superusuário (para acessar o Admin)
python manage.py createsuperuser

🖥 7. Executar o servidor Django
python manage.py runserver


Acesse:

👉 Django Admin:
http://127.0.0.1:8000/admin

🌐 8. Rotas da API
➤ Criar uma companhia

POST /companhias/

Exemplo de JSON:

{
  "nome": "JUWA",
  "cnpj": "12345678900011",
  "endereco": "São Paulo"
}

➤ Obter uma companhia

GET /companhias/<uuid>/

Exemplo:

http://127.0.0.1:8000/companhias/5c2b1ac0-55f4-4f11-a0c2-eaa5a606ed43/

🗂 9. Estrutura de diretórios
backend/
 ├── backend/
 │     ├── settings.py
 │     ├── urls.py
 │     └── wsgi.py
 ├── core/
 │     ├── models.py
 │     ├── views.py
 │     ├── admin.py
 │     ├── urls.py
 │     └── migrations/
 ├── db.sqlite3
 ├── manage.py
 └── README.md

🛠 10. Comandos úteis

Criar app:

python manage.py startapp core


Ver rotas:

python manage.py show_urls


Executar shell Django:

python manage.py shell

🇬🇧 README — Django + SQLite + Companies API

This project uses Django and SQLite to build a simple API that allows:

Creating a company

Retrieving a company

Managing all tables through Django Admin

Using UUID-based primary keys

Including the SQLite DB directly in the repository

📦 1. Requirements

Python 3.10+ installed

Up-to-date pip

Virtualenv recommended

🛠 2. Installation
macOS / Linux
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install django

Windows (PowerShell)
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install django

🚀 3. Project Structure
backend/
 ├── backend/
 ├── core/
 ├── db.sqlite3
 ├── manage.py
 └── README.md

🧩 4. Available Models

The project includes models for:

Company

User

Service

Location

Problem

All using UUID primary keys and automatic timestamps.

🔧 5. Database Migrations

(if needed)

python manage.py makemigrations
python manage.py migrate

🔐 6. Create a Superuser (Admin Access)
python manage.py createsuperuser

🖥 7. Start Django Server
python manage.py runserver


Admin Panel:

👉 http://127.0.0.1:8000/admin

🌐 8. API Routes
➤ Create a Company

POST /companhias/

Body example:

{
  "nome": "JUWA",
  "cnpj": "12345678900011",
  "endereco": "Paris"
}

➤ Get a Company

GET /companhias/<uuid>/

Example:

http://127.0.0.1:8000/companhias/5c2b1ac0-55f4-4f11-a0c2-eaa5a606ed43/

🗂 9. Directory Structure
backend/
 ├── backend/
 │     ├── settings.py
 │     ├── urls.py
 │     └── wsgi.py
 ├── core/
 │     ├── models.py
 │     ├── views.py
 │     ├── admin.py
 │     ├── urls.py
 │     └── migrations/
 ├── db.sqlite3
 ├── manage.py
 └── README.md

🛠 10. Useful Commands

Create a new app:

python manage.py startapp core


List all routes:

python manage.py show_urls


Open Django shell:

python manage.py shell