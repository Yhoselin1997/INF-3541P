import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Importar el conjunto de datos
df = pd.read_csv(r'C:\Users\Jhoselyne\Documents\documentos\IndianHouses.csv', encoding='latin1')

# Limpieza de datos
# Eliminar registros duplicados
df = df.drop_duplicates()

# Corregir errores ortográficos
df["Locality"] = df["Locality"].replace("Rohini Sector 24", "Rohini Sec 24")

# Eliminar valores atípicos
df = df.drop(df[df["Price"] > 10000000].index)

# Estandarización de datos
# Convertir la columna "Area" a una escala de 0 a 1
df["Area"] = df["Area"] / df["Area"].max()

# Codificación de datos categóricos
# Codificar la columna "Status"
le = LabelEncoder()
df["Status"] = le.fit_transform(df["Status"])

# Imprimir los resultados de las técnicas
print("**Resultados de las técnicas de preprocesamiento:**")
print("* Número de registros duplicados:", df.shape[0] - df.drop_duplicates().shape[0])
print("* Número de registros con errores ortográficos:", df.shape[0] - df.replace("Rohini Sector 24", "Rohini Sec 24").shape[0])
print("* Número de valores atípicos:", df.shape[0] - df.drop(df[df["Price"] > 10000000].index).shape[0])
print("* Rango de datos de la columna 'Area':", df["Area"].min(), "a", df["Area"].max())
print("* Códigos de la columna 'Status':", le.classes_)

# Guardar el conjunto de datos preprocesado
df.to_csv("data_preprocessed.csv")
