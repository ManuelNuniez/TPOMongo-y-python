
from conn import db, client

def parte_uno():
    print("\nListando todas las bases de datos")
    print(client.list_database_names())

    # Eliminar base de datos de pruebas
    client.drop_database('baseDeDatos')

    print("\nCreando base de datos 'baseDeDatos'")
    test_db = client['baseDeDatos']

    print("\nCreando coleccion 'coleccion'")
    test_db.create_collection('coleccion')


def parte_dos():
    response = list(db.recetas.find())
    print(response)

def main():
    #parte_uno()
    parte_dos()
