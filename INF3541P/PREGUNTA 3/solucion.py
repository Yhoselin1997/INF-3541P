import csv

archivo_csv = r'C:\Users\Jhoselyne\Documents\documentos\IndianHouses.csv'

conjunto_de_datos = {}

with open(archivo_csv, 'r', encoding='latin1') as archivo:
    lector_csv = csv.reader(archivo)
    encabezados = next(lector_csv)  
    for encabezado in encabezados:
        conjunto_de_datos[encabezado] = []  

    for fila in lector_csv:
        for i, valor in enumerate(fila):
            conjunto_de_datos[encabezados[i]].append(valor)

# Función para imputar valores faltantes en una columna numérica con la media
def imputar_media(columna):
    valores_validos = [valor for valor in columna if valor != '']  
    if len(valores_validos) == 0:
      
        return columna
    media = sum(float(valor) for valor in valores_validos) / len(valores_validos)
    return [media if valor == '' else valor for valor in columna]

# Función para imputar valores faltantes en una columna categórica con la moda
def imputar_moda(columna):
    valores_validos = [valor for valor in columna if valor != '']  
    if len(valores_validos) == 0:
       
        return columna
    moda = max(set(valores_validos), key=valores_validos.count)
    return [moda if valor == '' else valor for valor in columna]

# Realizar la imputación de valores faltantes en cada columna según su tipo
for columna, valores in conjunto_de_datos.items():
    if all(valor == '' for valor in valores):
       
        continue
    if isinstance(valores[0], (int, float)):
        # Imputar columnas numéricas con la media
        conjunto_de_datos[columna] = imputar_media(valores)
    elif isinstance(valores[0], str):
        # Imputar columnas categóricas con la moda
        conjunto_de_datos[columna] = imputar_moda(valores)

for columna, valores in conjunto_de_datos.items():
    print("RESULTADO FINAL CON LOS VALORES IMPUTADOS")
    print(f"{columna}: {valores}")
