
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
    print("\n1. Recetas para el desayuno:")
    response = db.recetas.find({
        "categoria": "Desayuno"
        })
    for recipe in response:
        print(recipe["nombre"])

    print("\n2. Recetas que usen huevos:")
    response = db.recetas.find({
        "ingredientes.nombre": {"$regex": "^Huevo"}
        })
    for recipe in response:
        print(recipe["nombre"])

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

    # print("\n4. Recetas para más de 5 personas:")                     #TODO: Funciona, pero no todas las recetas en rendimiento usan Porción como unidad        
    # response = db.recetas.find({
    # "rendimiento": {
    #     "$elemMatch": {               
    #         "$or": [
    #             {"unidad": "Porción", "cantidad": {"$gt": 5}}
    #         ]
    #     }
    # }
    # })
    # for recipe in response:
    #     print(recipe["nombre"], "=",recipe["rendimiento"][0]["cantidad"], "persona/s")

    # print("\n5. Cantidad de recetas que no usen cebolla:")
    # response = list(db.recetas.aggregate([
    #     {
    #     "$match": {
    #         "ingredientes.nombre": {
    #             "$not": {"$regex": "cebolla", "$options": "i"}
    #         }
    #     }                                                 #TODO: No funciona, hay que cambiarlo
    #     },
    #     {"$count": "total_sin_cebolla"}
    # ]))
    # print("Cantidad de recetas:", response["count"])

    print("\n6. Recetas que sean de dificultad media:")
    response = db.recetas.find({
        "dificultad": "Media"
        })
    for recipe in response:
        print(recipe["nombre"])

    print("\n7. Recetas que tengan un tiempo de cocción menor a 30 minutos:")
    response = db.recetas.find({
        "tiempo_preparación": {"$lt": 30}
        })
    for recipe in response:
        print(recipe["nombre"], "-->", recipe["tiempo_preparación"], "minuto/s")

def main():
    #parte_uno()
    #MostrarTodosLosDocumentos()
    filters()
