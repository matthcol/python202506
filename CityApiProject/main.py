from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class City(BaseModel):
    name: str
    population: int | None = None
    zipcode: str | None = None

@app.get("/api/city", response_model=list[City])
def get_cities():
    return [
        City(name="Pau"),
        City(name="Toulouse", population=500_000, zipcode="31000")
    ]

@app.post("/api/city", response_model=City)
def add_city(city: City):
    print("add:", city)
    return city
