# API de Catálogo de Filmes 🎬

## 📖 Sobre o Projeto

Esta é uma API RESTful desenvolvida como parte do meu aprendizado contínuo em desenvolvimento back-end. O objetivo foi construir um CRUD (Create, Read, Update, Delete) completo para gerenciar um catálogo de filmes, aplicando conceitos modernos de desenvolvimento de APIs com Python.

O projeto utiliza um banco de dados NoSQL (MongoDB) hospedado na nuvem (Atlas), com dados do dataset `sample_mflix`.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework:** FastAPI
- **Servidor:** Uvicorn
- **Banco de Dados:** MongoDB (com PyMongo)
- **Validação de Dados:** Pydantic
- **Ambiente:** Ambiente virtual Python (`venv`)

---

## 🚀 Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

**1. Clone o Repositório:**
```bash
git clone [https://github.com/seu-usuario/fastapi-movie-api.git](https://github.com/seu-usuario/fastapi-movie-api.git)
cd fastapi-movie-api
```

**2. Crie e Ative o Ambiente Virtual:**
```bash
# Criar o ambiente
python -m venv .venv

# Ativar no Windows
.\.venv\Scripts\Activate
```

**3. Instale as Dependências:**
```bash
pip install -r requirements.txt
```
*(Nós ainda não criamos este arquivo, vamos fazer isso no próximo passo!)*

**4. Configure as Variáveis de Ambiente:**
É necessário criar uma conexão com um cluster do MongoDB Atlas e obter a sua Connection String.

**5. Rode a Aplicação:**
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`. A documentação interativa (Swagger UI) pode ser acessada em `http://127.0.0.1:8000/docs`.

---

## Endpoints da API

A API possui os seguintes endpoints:

- `GET /movies`: Lista os primeiros 20 filmes do catálogo.
- `GET /movies/{id}`: Busca um filme específico pelo seu `_id`.
- `POST /movies`: Adiciona um novo filme ao catálogo.
- `PUT /movies/{id}`: Atualiza um filme existente.
- `DELETE /movies/{id}`: Deleta um filme do catálogo.