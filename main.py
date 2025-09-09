from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel

app = FastAPI()


MONGO_URI = "mongodb+srv://dio:dio@cluster0.zjgafy9.mongodb.net/"


client = MongoClient(MONGO_URI)


db = client.sample_mflix
collection = db.movies

@app.get("/movies")
def get_movies():
    movies = collection.find().limit(20)
    
    
    result = []
    for movie in movies:
        movie["_id"] = str(movie["_id"])
        result.append(movie)
        
    return result

@app.get("/movies/{id}")
def get_movie_by_id(id: str):
    try:
        movie_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid MongoDB ObjectID")
    
    movie = collection.find_one({"_id": movie_id})
    
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    movie["_id"] = str(movie['_id'])
    
    return movie

class Movie(BaseModel):
    title: str
    year: str
    
@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    
    movie_dict = movie.dict()
    
    result = collection.insert_one(movie_dict)
    
    new_movie = collection.find_one({"_id": result.inserted_id})
    
    new_movie["_id"] = str(new_movie["_id"])
    
    return new_movie

@app.put("/movies/{id}")
def update_movie(id: str, movie: Movie):
    
    try:
        movie_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid MongoDB ObjectId")
    
    movie_dict = movie.dict()
    
    result = collection.replace_one({"_id": movie_id}, movie_dict)
    
    if result.matched_count == 0:
        raise HTTPException(status_code = 404, detail=f"Movie with ID {id} not found")
    
    return{**movie_dict, "_id": id}

@app.delete("/movies/{id}")
def delete_movie(id: str):
    
    try:
        movie_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code= 400, detail="Invalide MongoDB ObjectID")
    
    result = collection.delete_one({"_id": movie_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f'Movie with Id {id} not found')
    
    return {"message": "Movie successfully deleted"}