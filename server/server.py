from flask import Flask, request
from pokemons import PokemonDB
app = Flask(__name__)

@app.route("/pokemons/<int:pokemon_id>", methods=["OPTIONS"])
def handle_cors_options(pokemon_id):
    return "", 204, {
        "Access-Control-Allow-Origin": "*", 
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",  
        "Access-Control-Allow-Headers": "Content-Type"  
    }

@app.route("/pokemons", methods=["GET"])
def retrieve_pokemons():
    db = PokemonDB("pokemons_db.db")
    pokemons = db.getPokemons()
    return pokemons, 200, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }
@app.route("/pokemons/<int:pokemon_id>", methods=["GET"])
def retrieve_pokemon(pokemon_id):
    db = PokemonDB("pokemons_db.db")
    pokemon = db.getPokemon(pokemon_id)
    if pokemon:
        return pokemon, 200, {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
    }
    else:

        return f"Pokemon with {pokemon_id} not found", 404, {"Access-Control-Allow-Origin" : "*"}

@app.route("/pokemons", methods=["POST"])
def create_pokemon():
    print("The request data is: ", request.form)
    name = request.form["name"]
    hp = request.form["hp"]
    element = request.form["element"]
    move = request.form["move"]
    description = request.form["description"]
    db = PokemonDB("pokemons_db.db")
    db.createPokemon(name,hp,element,move,description)
    return "Created", 201, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

@app.route("/pokemons/<int:pokemon_id>",methods=["PUT"])
def update_pokemon(pokemon_id):
    print("update pokemon with ID", pokemon_id)
    db = PokemonDB("pokemons_db.db")
    pokemon = db.getPokemon(pokemon_id)
    if pokemon:
        name =request.form["name"]
        hp = request.form["hp"]
        element = request.form["element"]
        move = request.form["move"]
        description = request.form["description"]
        db.updatePokemon(pokemon_id,name,hp,element,move,description)
        return "Updated", 200, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    else:
        return f"Pokemon with {pokemon_id} not found", 404, {"Access-Control-Allow-Origin" : "*"}
    
@app.route("/pokemons/<int:pokemon_id>", methods=["DELETE"])
def delete_pokemon(pokemon_id):
    print("delete pokemon with ID", pokemon_id)
    db = PokemonDB("pokemons_db.db")
    pokemon = db.getPokemon(pokemon_id)
    if pokemon:
        db.deletePokemon(pokemon_id)
        return "Deleted", 200, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    else:
        return f"Pokemon with ID {pokemon_id} not found", 404, {"Access-Control-Allow-Origin": "*"}
    

def run():
    app.run(port=8080, host='0.0.0.0')

if __name__ == "__main__":
    run()  
    # comment