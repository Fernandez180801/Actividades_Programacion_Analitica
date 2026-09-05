# %% Listas. Crear, recorrer, filtrar y acumular
notas = [4.5, 3.5, 2.8, 4.7, 3.9]
print(len(notas))
print(notas)
# %% Acceder por índice
temperaturas = [18, 20, 19, 21, 22]
print(temperaturas[0])
print(temperaturas[2])
print(temperaturas[4])
# %% Actualizar un elemento
ventas = [120, 80, 200, 50]
ventas[1] = 85
print(ventas)
# %% Agregar y extraer datos
notas = [3.5, 4.0, 2.8]
notas.append(4.6)
ultima = notas.pop(3,)
print(ultima)
print(notas)
# %% Calcular promedio 
notas = [4.2, 3.8, 5.0, 2.9]
total = 0
for nota in notas:
 total = total + nota
promedio = total / len(notas)
print(round(promedio, 2))
# %% Contar aprobados
notas = [4.2, 2.5, 3.0, 1.8, 4.7]
aprobados = 0
for nota in notas:
    if nota >= 3.0:
        aprobados = aprobados + 1
print(aprobados)


# %% Filtrar valores válidos
lecturas = [18, 200, 21, -99, 19, 22]
validas = []
for t in lecturas:
    if t >= -10 and t <= 50:
        validas.append(t)
print(validas)


# %% Comprensión de listas 

numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
print(cuadrados_pares)

# %% Lista Anidada
matriz = [[1, 2, 3], [4, 5, 6]]
total = 0
for fila in matriz:
    for valor in fila:
        total += valor
        print(total)
# %% Crear una tupla fija
ubicacion = (30, 20)
print(ubicacion)
print(type(ubicacion))

# %% Desempaquetar una tupla
registro = ("A01", "Laura", 4.6)
codigo, nombre, nota = registro
print(nombre)
print(nota) 
# %% Tupla de un solo elemento
codigo = ("A01",)
print(codigo)
print(type(codigo))

# %% Convertir lista a tupla 
columnas = ["fecha", "monto", "cliente"]
columnas_fijas = tuple(columnas)
print(columnas_fijas)
# %% Retorno múltiple
def resumen(valores):
 menor = min(valores)
 mayor = max(valores)
 return menor, mayor
minimo, maximo = resumen([8, 3, 10, 5])
print(minimo, maximo)

# %% Reconocer inmutabilidad
%% porque la tupla es una estructura de datos inmutable, 
%% esto quiere decir que no es modificable 

# %% Tupla como clave
lecturas = {}
coordenada = (4.65, -74.05)
lecturas[coordenada] = 18.5
print(lecturas[(4.65, -74.05)])

# %% Combinar listas con zip
nombres = ["Ana", "Luis", "Marta"]
notas = [4.2, 3.8, 5.0]
pares = list(zip(nombres, notas))
print(pares)

# %% Crear un diccionario 
estudiante = {
 "codigo": "A01",
 "nombre" : "Laura",
 "nota": 4.6
}
print(estudiante)

# %% Acceso seguro con get()
cliente = {"nombre": "Carlos", "puntaje": 720}
saldo = cliente.get ("saldo", 0)
print(saldo)
# %% Actualizar valores 
producto = {"codigo": "P01", "stock": 8}
producto["stock"] = producto["stock"] - 3
print(producto["stock"])

# %% Recorrer pares clave-valor
producto = {"codigo": "P01", "precio": 12000, "stock": 8}
for clave, valor in producto.items():
 print(clave, valor)
# %% Contar por categoría
tipos = ["Debito", "Credito", "Debito", "Debito", "Credito"]
conteo = {}
for tipo in tipos:
 conteo[tipo] = conteo.get(tipo, 0) + 1
print(conteo)
# %% Diccionario anidado
grupo = {
 "A01": {"nombre": "Laura", "nota": 4.6},
 "A02": {"nombre": "Luis", "nota": 3.8}
} 
print(grupo["A01"]["nota"])
# %% Lista de diccionarios
transacciones = [
 {"id": "T01", "monto": 120000},
 {"id": "T02", "monto": 85000},
 {"id": "T03", "monto": 210000}
]
total = 0
for t in transacciones:
 total += t["monto"]
print(total)

# %% Buscar por código
estudiantes = [
 {"codigo": "A01", "nombre": "Laura"},
 {"codigo": "A02", "nombre": "Luis"}
]
buscado = "A02"
resultado = None
for e in estudiantes:
    if e["codigo"] == buscado:
        resultado = e["nombre"]
        print(resultado)

# %% Filtrar diccionarios
estudiantes = [
 {"nombre": "Ana", "nota": 4.2},
 {"nombre": "Luis", "nota": 2.8},
 {"nombre": "Marta", "nota": 3.5}
]
aprobados = []
for e in estudiantes:
    if e["nota"] >= 3.0:
        aprobados.append(e["nombre"])
        print(aprobados)

# %% Agrupar por estado
clientes = [
 {"nombre": "Ana", "riesgo": "bajo"},
 {"nombre": "Luis", "riesgo": "alto"},
 {"nombre": "Marta", "riesgo": "bajo"}
]
grupo = {}
for c in clientes:
 riesgo = c["riesgo"]
 if riesgo not in grupo:
     grupo[riesgo] = grupo[nombre]
     grupo[riesgo].append(c[grupos])
     print(grupo)

# %%
