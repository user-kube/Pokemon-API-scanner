import requests
import sys
import json

def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_details = {
            'name': data['name'],
            'base_experience': data['base_experience'],
            'height': data['height'],
            'weight': data['weight'],
            'abilities': [ability['ability']['name'] for ability in data['abilities']]
        }
        return pokemon_details
    else:
        return {'error': 'Pokémon not found'}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python pokemon_info.py <pokemon_name>")
        sys.exit(1)
    
    pokemon_name = sys.argv[1]
    pokemon_data = get_pokemon_data(pokemon_name)
    print(json.dumps(pokemon_data, indent=4))
