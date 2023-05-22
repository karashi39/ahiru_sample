import pathlib

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .usecases import GetPokemon

PATH_TEMPLATES = str(
    pathlib.Path(__file__).resolve() \
        .parent.parent / "templates"
)
templates = Jinja2Templates(directory=PATH_TEMPLATES)

router = APIRouter()

@router.get("/{pokemon_id}", response_class=HTMLResponse)
async def site_root(
    request: Request,
):
    pokemon_id = request.scope["path_params"].get("pokemon_id")
    pokemon = GetPokemon.execute(pokemon_id)
    return templates.TemplateResponse(
        "pokemon/index.html",
        context={
            "request": request,
            "pokemon": pokemon,
        }
    )
