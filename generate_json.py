from faker import Faker
import json
import random

faker = Faker(locale = ['es_AR', 'es_CL', 'es_CO', 'es_ES', 'pt_BR'])

DATASET_LEN = 100
COMIDAS = ['Sopa', 'Ensalada', 'Salsa', 'Sandwich', 'Postre']
CATEGORIAS = ['Desayuno', 'Almuerzo', 'Merienda', 'Cena']
DIFICULTADES = ['Fácil', 'Medio', 'Difícil']
ETIQUETAS = ['Horno', 'Sartén', 'Microondas', 'Licuadora', 'Panificado', 'Pasta']
CARACTERISTICAS = ['Dulce', 'Salado', 'Frio', 'Caliente', 'Dulce', 'APPC', 'vegan', 'veggie']

recetas = [{
    "nombre": random.choice(COMIDAS) + ' ' + faker.city(),
    "descripción": faker.text(100),
    "categoria": random.choice(CATEGORIAS),
    "tiempo_preparación": random.randint(5, 180),
    "dificultad": random.choice(DIFICULTADES),
    "instrucciones": faker.text(200),
    "imagen": faker.image_url(),
    "ingredientes": [
        { "nombre": "Huevos", "cantidad": random.randint(1, 3), "unidad": "Unidad/es" },
        { "nombre": "Harina", "cantidad": random.randint(100, 500), "unidad": "g" },
        { "nombre": "Agua", "cantidad": random.randint(100, 500), "unidad": "ml" },
    ],
    "rendimiento": [
        { "cantidad": random.randint(1, 3), "unidad": "Porción/es" },
        { "cantidad": random.randint(100, 500), "unidad": "g", "texto": str(random.randint(100, 500)) + 'g' }
    ],
    "etiquetas": [
        { "tipo": random.choice(ETIQUETAS), "valor": faker.null_boolean() },
        { "tipo": random.choice(ETIQUETAS), "valor": faker.null_boolean(), "texto": faker.text(20) }
    ],
    "caracteristicas": [
        { "tipo": random.choice(CARACTERISTICAS), "valor": faker.null_boolean(), "texto": faker.text(20) },
        { "tipo": random.choice(CARACTERISTICAS), "valor": faker.null_boolean(), "texto": faker.text(20) }
    ]
} for _ in range(DATASET_LEN)]

with open('recetasDeCocina.json', "w", encoding="utf-8") as file:
    file.write(json.dumps(recetas))
