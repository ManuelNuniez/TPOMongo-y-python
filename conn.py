from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

client = MongoClient("mongodb://localhost:27017", server_api=ServerApi('1'))

def connect(database_name="recetasDeCocina"):
    try:
        db = client[database_name]
        return db
    except ConnectionFailure as e:
        print(f"Error de conexión: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

db = connect()
