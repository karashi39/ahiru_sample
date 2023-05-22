from ..utils.rest import get

class GetPokemon:
    @classmethod
    def execute(cls, pokemon_id: str):
        url = f"https://pokeapi.co/api/v2/pokemon-form/{pokemon_id}"
        pokemon = get(url)
        return {
            "pokemon_id": pokemon.get("id"),
            "name": pokemon.get("name"),
        }
