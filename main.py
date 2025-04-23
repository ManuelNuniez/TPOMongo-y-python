
from conn import db, client

def parte_uno():
    print("\nListando todas las bases de datos")
    print(client.list_database_names())
    print("\nListando todas las Colecciones")
    print(db.list_collection_names())

    # Eliminar base de datos de pruebas
    client.drop_database('baseDeDatos')
    
    # Creamos Nueva BD de prueba:

    print("\nCreando base de datos 'baseDeDatos'")
    test_db = client['baseDeDatos']

    print("\nCreando coleccion 'coleccion'")
    test_db.create_collection('coleccion')


# MostrarDocumentos
def MostrarTodosLosDocumentos():
    response = list(db.recetas.find())
    for doc in response:
        print(doc["_id"], "-", doc["nombre"])


def filters():

    # 1. Recetas para el desayuno
    print("\n1. Recetas para el desayuno:")
    response = db.recetas.find({
        "categoria": "Desayuno"
        })
    for recipe in response:
        print(recipe["nombre"])

    # 2. Recetas que usen huevos
    print("\n2. Recetas que usen huevos:")
    response = db.recetas.find({
        "ingredientes.nombre": {"$regex": "^Huevo"}
        })
    for recipe in response:
        print(recipe["nombre"])

    # 3. Una receta fria
    print("\n3. Una receta fria:")
    recipe = db.recetas.find_one({
        "etiquetas": {
            "$elemMatch": {
                "tipo": "temp",
                "valor": "frio"
            }
        }
    })
    print(recipe["nombre"])
    
    # 4. Recetas vegetarianas, pero no veganas
    print("\n4. Recetas vegetarianas:")
    response = db.recetas.aggregate([
        {
            "$match": {
                "$and": [
                    {
                        "caracteristicas.tipo": "vegetariano",
                        "caracteristicas.valor": True
                    },
                    {
                        "caracteristicas.tipo": "vegan",
                        "caracteristicas.valor": False
                    }
                ]
            }
        }
    ])
    for recipe in response:
        print(recipe["nombre"])

    # 5. Cantidad de recetas que no usen cebolla
    print("\n5. Cantidad de recetas que no usen cebolla:")

    response = list(db.recetas.aggregate([
        {
            "$match": {
                "ingredientes.nombre": {
                    "$not": {"$regex": "cebolla", "$options": "i"}
                }
            }
        },
        {"$count": "total_sin_cebolla"}
    ]))

    if response:
        print("Cantidad de recetas:", response[0]["total_sin_cebolla"])
    else:
        print("No se encontraron recetas sin cebolla.")

    print("\nRecetas sin cebolla:")
    recetas_sin_cebolla = db.recetas.find({
        "ingredientes.nombre": {
            "$not": {"$regex": "cebolla", "$options": "i"}
        }
    })

    for receta in recetas_sin_cebolla:
        print("-", receta["nombre"])

    # 6. Recetas de dificutad media
    print("\n6. Recetas que sean de dificultad media:")
    response = db.recetas.find({
        "dificultad": "Media"
        })
    for recipe in response:
        print(recipe["nombre"])

    # 7. Recetas que tengan un tiempo de cocción menor a 30 min
    print("\n7. Recetas que tengan un tiempo de cocción menor a 30 minutos:")
    response = db.recetas.find({
        "tiempo_preparación": {"$lt": 30}
        })
    for recipe in response:
        print(recipe["nombre"], "-->", recipe["tiempo_preparación"], "minuto/s")


def queries():
    # 1. Recetas que tengan un tiempo de cocción menor a 30 minutos
    response = db.recetas.find({
        "tiempo_preparación": {"$lt": 30}
    })
    for recipe in response:
        print(recipe["nombre"], "-->", recipe["tiempo_preparación"], "minuto/s")

    print()

    # 2. Recetas que sean de dificultad media
    response = db.recetas.find({
        "dificultad": "Media"
    })
    for recipe in response:
        print(recipe["nombre"])

    print()

    # 3. Recetas que usen huevos
    response = db.recetas.find({
        "ingredientes.nombre": {"$regex": "^Huevo"}
    })
    for recipe in response:
        print(recipe["nombre"])

    print()

    # 4. Recetas para el desayuno
    response = db.recetas.find({
        "categoria": "Desayuno"
    })
    for recipe in response:
        print(recipe["nombre"])

    print()

    # 5. Recetas con la tag vegana
    response = db.recetas.find({
        "etiquetas.tipo": "vegana"
    })
    for recipe in response:
        print(recipe["nombre"])

def main():
    parte_uno()
    MostrarTodosLosDocumentos()
    filters()
    queries()
