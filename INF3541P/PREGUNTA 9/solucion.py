
data = []

with open(r'C:\Users\Jhoselyne\Documents\documentos\Iris.csv', 'r', encoding='latin1') as file:
    lines = file.readlines()
    for line in lines[1:]: 
        data.append(line.strip().split(','))


X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Establecer la proporción de entrenamiento y prueba (80% entrenamiento, 20% prueba)
train_size = 0.8
test_size = 0.2

# Calcular los índices de división
total_samples = len(X)
train_samples = int(total_samples * train_size)
test_samples = total_samples - train_samples

# Dividir el conjunto de datos en entrenamiento y prueba
X_train = X[:train_samples]
X_test = X[train_samples:]
y_train = y[:train_samples]
y_test = y[train_samples:]


print("Forma de X_train:", len(X_train))
print("Forma de X_test:", len(X_test))
print("Forma de y_train:", len(y_train))
print("Forma de y_test:", len(y_test))
