# Card Creator

## Resource
**Pokemon**

**Attributes:**
- **name** (string)
- **hp** (integer)
- **element** (string)
- **move** (string)
- **description** (string)


## Schema
```sql
CREATE TABLE pokemons (
    id INTEGER PRIMARY KEY,
    name TEXT,
    hp INTEGER,
    element TEXT,
    move TEXT,
    description TEXT
);
```
### REST Endpoints
| **Name**                          | **Method** | **Path**                  |
|-----------------------------------|------------|---------------------------|
| Retrieve Pokémon collection        | `GET`      | `/pokemons`               |
| Retrieve Pokémon member            | `GET`      | `/pokemons/<id>`          |
| Create Pokémon member              | `POST`     | `/pokemons`               |
| Update Pokémon member              | `PUT`      | `/pokemons/<id>`          |
| Delete Pokémon member              | `DELETE`   | `/pokemons/<id>`          |
