import pandas as pd
from conn import db

recetas = db.recetas.find()
df = pd.DataFrame(recetas)
df.to_csv("recetasDeCocina.csv", index=False)
