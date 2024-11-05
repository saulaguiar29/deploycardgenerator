import sqlite3

def dict_factory(cursor, row):
 fields = []
 # Extract column names from cursor description
 for column in cursor.description:
    fields.append(column[0])

 # Create a dictionary where keys are column names and values are row values
 result_dict = {}
 for i in range(len(fields)):
    result_dict[fields[i]] = row[i]

 return result_dict

class PokemonDB:
    def __init__(self,filename):
        #connect to DB file
        self.connection = sqlite3.connect(filename)
        self.connection.row_factory = dict_factory
        #use the connection instance to perform db operations
        #create a cursor instance for the connection
        self.cursor = self.connection.cursor()

    def getPokemons(self):
        #now that we have an access point we can fetch all or one
        #ONLY applicable use of fetch is following a SELECT query
        self.cursor.execute("SELECT * FROM pokemons")
        pokemons = self.cursor.fetchall()
        return pokemons
    
    def getPokemon(self,pokemon_id):
        data = [pokemon_id]
        self.cursor.execute("SELECT * FROM pokemons WHERE id = ?",data)
        pokemons = self.cursor.fetchone()
        return pokemons
    
    
    def createPokemon(self,name,hp,element,move,description):
        data = [name,hp,element,move,description]
        #add a new rollercoaster to our db
        self.cursor.execute("INSERT INTO pokemons(name,hp,element,move,description)VALUES(?,?,?,?,?)", data)
        self.connection.commit()

    def updatePokemon(self,pokemon_id,name,hp,element,move,description):
       data = [name,hp,element,move,description,pokemon_id]
       self.cursor.execute("UPDATE pokemons SET name = ?, hp = ?, element = ?, move = ?, description = ? WHERE id = ?",data)
       self.connection.commit()
    
    def deletePokemon(self, pokemon_id):
       data = [pokemon_id]
       self.cursor.execute("DELETE From pokemons WHERE id = ?", data)
       self.connection.commit()
