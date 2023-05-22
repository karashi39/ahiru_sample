import os

from fastapi import FastAPI

from app.pokemon.usecases import GetPokemon


GREETING = os.getenv("GREETING", default="World")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"Hello {GREETING}"}

@app.get("/api/pokemon/{pokemon_id}")
def get_pokemon(pokemon_id):
    usecase = GetPokemon()
    return usecase.execute(pokemon_id)
