import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.pokemon.usecases import GetPokemon
from app.pokemon import views as pokemon_view


GREETING = os.getenv("GREETING", default="World")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"Hello {GREETING}"}

app.include_router(
    pokemon_view.router,
    prefix="/pokemon",
    tags=["pokemon"],
    responses={404: {"description": "not found"}},
)

@app.get("/pokemon")
async def redirect_subpage():
    return RedirectResponse(
        "/pokemon",
    )

@app.get("/api/pokemon/{pokemon_id}")
def get_pokemon(pokemon_id):
    usecase = GetPokemon()
    return usecase.execute(pokemon_id)
