# Backend – Como rodar / How to run

## 🇧🇷 Como rodar o backend (Django)

### 1. Ir até a pasta do backend

No terminal, vá até a pasta onde está o `manage.py`:

```bash
cd /caminho/para/seu/projeto/backend
```

### 2. Ativar o ambiente virtual (se existir)
Se você criou um .venv:
```bash
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```
Se ainda não existe, você pode criar rapidamente:

```bash
python -m venv .venv
source .venv/bin/activate
pip install django django-cors-headers
```
### 3. Aplicar migrações (primeira vez)
```bash
python manage.py migrate
```

### 4. Rodar o servidor de desenvolvimento
```bash
python manage.py runserver
```

O backend estará disponível em:

http://localhost:8000/
A API estará em URLs como:

http://localhost:8000/api/login/

http://localhost:8000/api/problemas/

http://localhost:8000/api/problemas/<id>/

## 🇬🇧 How to run the backend (Django)
 
### 1. Go to the backend folder
In the terminal, go to the folder where manage.py is located:

```bash
cd /path/to/your/project/backend
```
### 2. Activate the virtual environment (if it exists)
If you created a .venv:

```bash
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```
If it doesn’t exist yet, you can quickly create it:

```bash
python -m venv .venv
source .venv/bin/activate
pip install django django-cors-headers
```

### 3. Apply migrations (first time)
```bash
python manage.py migrate
```

### 4. Run the development server
```bash
python manage.py runserver
```
The backend will be available at:

http://localhost:8000/
The API will respond on URLs such as:

http://localhost:8000/api/login/

http://localhost:8000/api/problemas/

http://localhost:8000/api/problemas/<id>/