from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_read_main_should_return_status_200():

    response = client.get("/")

    assert response.status_code == 200

def test_read_main_should_return_json():
    response = client.get("/")
    
    assert response.json() == {"message": "Hello World"}
    
def test_get_movie_by_id_should_return_200_and_correct_movie():
    known_id = "573a1390f29313caabcd42e8"
    
    response = client.get(f"/movies/{known_id}")
    
    assert response.status_code == 200
    
    assert response.json()["title"] == "The Great Train Robbery"
    
def test_get_movie_by_id_with_invalid_id_should_return_400():
    invalid_id = "um_id_invalido"
    
    response = client.get(f"/movies/{invalid_id}")
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid MongoDB ObjectId"}
    
def test_get_movie_by_id_with_non_existent_id_should_return_404():
    
    non_existent_id = "6054ba452814a8e83f4e28f3"
    
    response = client.get(f"/movies/{non_existent_id}")
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}
    
    #  --- Teste para o endpoint POST /movies ---
def test_create_movie_should_return_201_and_the_movie():
    #1. Define os dados do filme que será criado
    
    new_movie_data = {
        "title": "O teste de Nicolas",
        "year": 2025
    }
    
    # 2. Fazer a requisição POST para o endpoint /movies 
    response =  client.post("/movies", json=new_movie_data)
    
    # 3. Verificar se a resposta da API está correta
    assert response.status_code == 201 #201 significa "Created"
    

    created_movie = response.json()

    # verifica se os dados retornados batem com o que foi enviado
    assert created_movie["title"] == new_movie_data["title"]
    assert created_movie["year"] == new_movie_data["year"]
        
    #verifica se o mongodb gerou um id para o filme
    assert "_id" in created_movie
    
    # 4. Limpeza (Cleanup): Apaga o filme de teste que criamos
    movie_id = created_movie["_id"]
    client.delete(f"/movies/{movie_id}")
    
    
    # --- Testes para o endpoint PUT /movies/{id}
def test_update_movie_should_return_200_and_updated_movie():
        
    initial_movie_data = {"title": "Filme Original","year": 2000}
    response_create = client.post("/movies",json=initial_movie_data)
    assert response_create.status_code == 201
    movie_id = response_create.json()["_id"]
    
    # --- Ação: Atualizar o filme que acabou de sercriado
    updated_movie_data = {"title": "Filme Editado","year": 2001}
    response_update = client.put(f"/movies/{movie_id}", json = updated_movie_data)
        
    # Verificação: Checar se a atualização funcionou
        
    assert response_update.status_code == 200
    updated_movie = response_update.json()
    assert updated_movie["title"] == updated_movie_data["title"]
    assert updated_movie["year"] == updated_movie_data["year"]
    
    # limpeza (Cleanup): Apagar o filem de teste ---
    client.delete(f"/movies/{movie_id}")

def test_update_movie_with_non_existent_id_should_return_404():
    non_existent_id = "6054ba452814a8e83f4e28f3"
    movie_data = {"title": "Filme Fantasma", "year": 2025}
    
    response = client.put(f"/movies/{non_existent_id}", json = movie_data)
    
    assert response.status_code == 404
    assert response.json() == {"detail": f"Movie with ID {non_existent_id} not found"}
    
    
def test_delete_movie_should_return_200_and_success_message():
    movie_data = {'title': "Filme TEemporário", "year": 2024}
    response_create = client.post("/movies", json=movie_data)
    
    assert response_create.status_code == 201
    movie_id = response_create.json()["_id"]
    
    response_delete = client.delete(f"/movies/{movie_id}")
    
    assert response_delete.status_code == 200
    assert response_delete.json() =={"message": "Movie successfully deleted"}
    
    response_get = client.get(f"/movies/{movie_id}")
    assert response_get.status_code == 404 # Esperamos um erro "Not Found"

def test_delete_movie_with_non_existent_id_should_return_404():
    non_existent_id = "6054ba452814a8e83f4e28f3"
    
    response = client.delete(f"/movies/{non_existent_id}")
    
    assert response.status_code == 404
    assert response.json() == {"detail": f"Movie with ID {non_existent_id} not found"}
    