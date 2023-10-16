import pandas as pd

df = pd.read_csv(r'C:\Users\Jhoselyne\Documents\documentos\IndianHouses.csv', encoding='latin1')

# Función para etiquetar simple
def etiquetar_simple(row):
    return row['Status']  

# Función para etiquetar binario
def etiquetar_binario(row):
    if row['Status'] == "Ready_to_move":
        return 1
    elif row['Status'] == "Almost_ready":
        return 0  

df['Etiqueta_Simple'] = df.apply(etiquetar_simple, axis=1)


df['Etiqueta_Binaria'] = df.apply(etiquetar_binario, axis=1)


print(df[['Status', 'Etiqueta_Simple', 'Etiqueta_Binaria']])
