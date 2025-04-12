
from conn import db, client

def parte_uno():
    print("\nListando todas las bases de datos")
    print(client.list_database_names())
    print("\nListando todas las Colecciones")
    print(db.list_collection_names())

    # Creamos Nueva BD de prueba:

    print("\nCreando base de datos 'baseDeDatos'")
    test_db = client['baseDeDatos']

    print("\nCreando coleccion 'coleccion'")
    test_db.create_collection('coleccion')

    # Eliminar base de datos de pruebas
    client.drop_database('baseDeDatos')

# MostrarDocumentos
def MostrarTodosLosDocumentos():
    response = list(db.recetas.find())
    for doc in response:
        print(doc)

# def main():
#     #parte_uno()
#     parte_dos()

#parte_uno()
MostrarTodosLosDocumentos()