
with open(r'C:\Users\Jhoselyne\Documents\documentos\IndianHouses.csv', 'r', encoding='latin1') as file:
    lines = file.readlines()



area_values = []
bhk_values = []
bathroom_values = []
furnishing_values = []
locality_values = []
parking_values = []
price_values = []
status_values = []
transaction_values = []
type_values = []
per_sqft_values = []


for line in lines[1:]: 
    values = line.strip().split(',')
    area_values.append(float(values[0]))
    
    # Imputación de la columna "BHK"
    try:
        bhk_values.append(int(values[1]))
    except ValueError:
        bhk_values.append(0)  # O cualquier otro valor predeterminado que elijas
    
    # Imputación de la columna "Bathroom"
    try:
        bathroom_values.append(int(values[2]))
    except ValueError:
        bathroom_values.append(0)  # O cualquier otro valor predeterminado que elijas

    furnishing_values.append(values[3] if values[3] else "Valor_predeterminado")
    locality_values.append(values[4] if values[4] else "Valor_predeterminado")
    
    # Imputación de la columna "Parking"
    try:
        parking_values.append(int(values[5]))
    except ValueError:
        parking_values.append(0)  # O cualquier otro valor predeterminado que elijas
    
    # Imputación de la columna "Price"
    try:
        price_values.append(float(values[6]))
    except ValueError:
        price_values.append(0)  # O cualquier otro valor predeterminado que elijas

    status_values.append(values[7] if values[7] else "Valor_predeterminado")
    transaction_values.append(values[8] if values[8] else "Valor_predeterminado")
    type_values.append(values[9] if values[9] else "Valor_predeterminado")
    
    # Imputación de la columna "Per_Sqft"
    try:
        per_sqft_values.append(float(values[10]))
    except ValueError:
        per_sqft_values.append(0) 

# Función para calcular la media
def calcular_media(valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma / len(valores)

# Función para calcular la moda
def calcular_moda(valores):
    contador = {}
    for valor in valores:
        if valor in contador:
            contador[valor] += 1
        else:
            contador[valor] = 1
    moda = max(contador, key=contador.get)
    return moda

# Función para calcular cuartiles
def calcular_cuartiles(valores):
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    q1 = valores_ordenados[n // 4]
    q2 = valores_ordenados[n // 2]
    q3 = valores_ordenados[(3 * n) // 4]
    return q1, q2, q3

# Función para calcular percentiles
def calcular_percentiles(valores, percentiles):
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    resultados = {}
    for p in percentiles:
        posicion = int((p / 100) * (n - 1))
        resultados[f'Percentil_{p}'] = valores_ordenados[posicion]
    return resultados


media_area = calcular_media(area_values)
media_precio = calcular_media(price_values)
media_per_sqft = calcular_media(per_sqft_values)
moda_furnishing = calcular_moda(furnishing_values)
moda_status = calcular_moda(status_values)
moda_transaction = calcular_moda(transaction_values)
moda_type = calcular_moda(type_values)
moda_bathroom = calcular_moda(bathroom_values)

cuartiles_area = calcular_cuartiles(area_values)
cuartiles_precio = calcular_cuartiles(price_values)
cuartiles_per_sqft = calcular_cuartiles(per_sqft_values)
cuartiles_bhk = calcular_cuartiles(bhk_values)
cuartiles_bathroom = calcular_cuartiles(bathroom_values)
cuartiles_parking = calcular_cuartiles(parking_values)

percentiles = [10, 90]
percentiles_area = calcular_percentiles(area_values, percentiles)
percentiles_precio = calcular_percentiles(price_values, percentiles)
percentiles_per_sqft = calcular_percentiles(per_sqft_values, percentiles)
percentiles_bhk = calcular_percentiles(bhk_values, percentiles)
percentiles_bathroom = calcular_percentiles(bathroom_values, percentiles)
percentiles_parking = calcular_percentiles(parking_values, percentiles)


print("MEDIA")
print("Media de Área:", media_area)
print("Media de Precio:", media_precio)
print("Media de Per_Sqft:", media_per_sqft)

print("MODA")
print("Moda de Furnishing:", moda_furnishing)
print("Moda de Status:", moda_status)
print("Moda de Transaction:", moda_transaction)
print("Moda de Type:", moda_type)
print("Moda de Bathroom:", moda_bathroom)

print("CUARTILES")
print("Cuartiles de BHK:", cuartiles_bhk)
print("Cuartiles de Bathroom:", cuartiles_bathroom)
print("Cuartiles de Parking:", cuartiles_parking)
print("Cuartiles de Área:", cuartiles_area)
print("Cuartiles de Precio:", cuartiles_precio)
print("Cuartiles de Per_Sqft:", cuartiles_per_sqft)


print("PERCEINTILES")
for p in percentiles:
    print(f"Percentil {p} de Área:", percentiles_area[f'Percentil_{p}'])
    print(f"Percentil {p} de Precio:", percentiles_precio[f'Percentil_{p}'])
    print(f"Percentil {p} de Per_Sqft:", percentiles_per_sqft[f'Percentil_{p}'])
    print(f"Percentil {p} de BHK:", percentiles_bhk[f'Percentil_{p}'])
    print(f"Percentil {p} de Bathroom:", percentiles_bathroom[f'Percentil_{p}'])
    print(f"Percentil {p} de Parking:", percentiles_parking[f'Percentil_{p}'])
