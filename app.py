from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Modello singolo frutto
class Fruit(BaseModel):
    name: str

# Modello contenitore di più frutti
class Fruits(BaseModel):
    fruits: List[Fruit]

app = FastAPI()

# Origini permesse (CORS)
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Database temporaneo (in memoria)
memory_db = {"fruits": []}

# Endpoint GET
@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])

# Endpoint POST
@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit

# ✅ Solo avvia uvicorn se esegui direttamente app.py
if __name__ == "__main__":
    import uvicorn  # Import qui, così pytest non richiede uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)


