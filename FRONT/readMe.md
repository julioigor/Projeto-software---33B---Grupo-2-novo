# Frontend – Como rodar / How to run

## 🇧🇷 Como rodar o frontend

### 1. Ir até a pasta do frontend

No terminal:

```bash
cd /caminho/para/seu/projeto/FRONT
```
(onde estão landing.html, Connexion.html, dashboard.html, etc.)


### 2. Iniciar um servidor HTTP simples

```bash
python -m http.server 5500
```
### 3. Abrir no navegador
Landing page:
http://localhost:5500/landing.html

Página de login:
http://localhost:5500/Connexion.html

Certifique-se de que o backend está rodando em http://localhost:8000
e que o arquivo env.js aponta para API_BASE_URL: "http://localhost:8000/api".


## 🇬🇧 How to run the frontend
### 1. Go to the frontend folder
In the terminal:



```bash
cd /path/to/your/project/FRONT
```
(where you have landing.html, Connexion.html, dashboard.html, etc.)

### 2. Start a simple HTTP server


```bash
python -m http.server 5500
```

### 3. Open in the browser
Landing page:
http://localhost:5500/landing.html

Login page:
http://localhost:5500/Connexion.html

Make sure the backend is running at http://localhost:8000
and that env.js points to API_BASE_URL: "http://localhost:8000/api".