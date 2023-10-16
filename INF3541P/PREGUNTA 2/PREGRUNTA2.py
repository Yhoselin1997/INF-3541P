import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Users\Jhoselyne\Documents\documentos\IndianHouses.csv', encoding='latin1')

# Calcular la media (promedio) para las columnas "Area", "Price" y "Per_Sqft"
media_area = df['Area'].mean()
media_precio = df['Price'].mean()
media_per_Sqft = df['Per_Sqft'].mean()

# Calcular la moda para las columnas categóricas
moda_furnishing = df['Furnishing'].mode()[0]
moda_status = df['Status'].mode()[0]
moda_transaction = df['Transaction'].mode()[0]
moda_type = df['Type'].mode()[0]

# Calcular la moda y los cuartiles 
moda_bathroom = df['Bathroom'].mode()[0]
cuartiles_bhk = np.percentile(df['BHK'].dropna(), [25, 50, 75])
cuartiles_bathroom = np.percentile(df['Bathroom'].dropna(), [25, 50, 75])
cuartiles_parking = np.percentile(df['Parking'].dropna(), [25, 50, 75])
cuartiles_area = np.percentile(df['Area'].dropna(), [25, 50, 75])  
cuartiles_precio = np.percentile(df['Price'].dropna(), [25, 50, 75]) 
cuartiles_per_sqft = np.percentile(df['Per_Sqft'].dropna(), [25, 50, 75])

# Calcular percentiles 
percentil_10_bhk = np.percentile(df['BHK'].dropna(), 10)
percentil_90_bhk = np.percentile(df['BHK'].dropna(), 90)
percentil_10_bathroom = np.percentile(df['Bathroom'].dropna(), 10)
percentil_90_bathroom = np.percentile(df['Bathroom'].dropna(), 90)
percentil_10_parking = np.percentile(df['Parking'].dropna(), 10)
percentil_90_parking = np.percentile(df['Parking'].dropna(), 90)
percentil_10_area = np.percentile(df['Area'].dropna(), 10) 
percentil_90_area = np.percentile(df['Area'].dropna(), 90)
percentil_10_precio = np.percentile(df['Price'].dropna(), 10)  
percentil_90_precio = np.percentile(df['Price'].dropna(), 90)
percentil_10_per_sqft = np.percentile(df['Per_Sqft'].dropna(), 10)
percentil_90_per_sqft = np.percentile(df['Per_Sqft'].dropna(), 90)


print("MEDIA")
print("Media de Área:", media_area)
print("Media de Precio:", media_precio)
print("Media de Per_Sqft:", media_per_Sqft)

print("MODA")
print("Moda de Furnishing:", moda_furnishing)
print("Moda de Status:", moda_status)
print("Moda de Transaction:", moda_transaction)
print("Moda de Type:", moda_type)
print("Moda de bathroom:", moda_bathroom)

print("CUARTILES")
print("Cuartiles de BHK:", cuartiles_bhk)
print("Cuartiles de Bathroom:", cuartiles_bathroom)
print("Cuartiles de Parking:", cuartiles_parking)
print("Cuartiles de Área:", cuartiles_area)
print("Cuartiles de Precio:", cuartiles_precio)  
print("Cuartiles de Per_Sqft:", cuartiles_per_sqft)

print("PERCENTILES")
print("Percentil 10 de BHK:", percentil_10_bhk)
print("Percentil 90 de BHK:", percentil_90_bhk)
print("Percentil 10 de Bathroom:", percentil_10_bathroom)
print("Percentil 90 de Bathroom:", percentil_90_bathroom)
print("Percentil 10 de Parking:", percentil_10_parking)
print("Percentil 90 de Parking:", percentil_90_parking)
print("Percentil 10 de Área:", percentil_10_area)  # Percentiles para "Area"
print("Percentil 90 de Área:", percentil_90_area)
print("Percentil 10 de Precio:", percentil_10_precio)  # Percentiles para "Price"
print("Percentil 90 de Precio:", percentil_90_precio)
print("Percentil 10 de Per_Sqft:", percentil_10_per_sqft)
print("Percentil 90 de Per_Sqft:", percentil_90_per_sqft)
