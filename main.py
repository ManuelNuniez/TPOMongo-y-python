
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
        print(doc)

# def main():
#     #parte_uno()
#     parte_dos()

def filters():
    print("\n1.Recetas que usen 'leche'")
    response = list(db.recetas.find({"ingredientes.nombre": "Leche"}))
    for recipe in response:
        print(recipe["nombre"])
    
    print("\n2.Recetas con un tiempo de coccion menor a 30 minutos")
    response = list(db.recetas.find({"tiempo_coccion": {"$lt": 30}}))
    for recipe in response:
        print(recipe["nombre"], "-->" ,recipe["tiempo_coccion"], "minuto/s")
    
    print("\n3.Recetas que sean de la categoria 'Sopas'")
    response = list(db.recetas.find({"categoria": "Sopas"}))
    for recipe in response:
        print(recipe["nombre"])
    
    print("\n4.Recetas para mas de 5 personas")
    response = list(db.recetas.find({"rendimiento.cantidad": {"$gt": 5}}))
    for recipe in response:
        print(recipe["nombre"])

    print("\n5.Recetas que sean de dificultad 'Media'")
    response = list(db.recetas.find({"dificultad": "Medio"}))
    for recipe in response:
        print(recipe["nombre"])

    # print("\n6.Recetas que no usen 'cebolla'")
    # response = list(db.recetas.find({"ingredientes.nombre": {"$ne": "Cebolla"}}))
    # for recipe in response:
    #     print(recipe["nombre"])
    

#parte_uno()
#MostrarTodosLosDocumentos()
filters()