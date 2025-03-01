import requests
import json


def get_pokemon_details(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    response = requests.get(url)

    if response.status_code != 200:
        print(json.dumps({"error": "Pokémon not found"}))
        return

    data = response.json()
    
    pokemon_info = {
        "name": data["name"],
        "base_experience": data["base_experience"],
        "height": data["height"],
        "weight": data["weight"],
        "abilities": [ability["ability"]["name"] for ability in data["abilities"]]
    }

    print(json.dumps(pokemon_info, indent=4))

# pokemon_name=input("Enter pokemon name")
# get_pokemon_details(pokemon_name)

if __name__ == "__main__":
    pokemon_name = input("Enter Pokémon name: ").strip()

    if not pokemon_name:
        print(json.dumps({"error": "No Pokémon name provided"}))
    else:
        get_pokemon_details(pokemon_name)
