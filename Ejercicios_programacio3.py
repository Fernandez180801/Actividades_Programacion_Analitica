# %% Definir una función
def saludar():
 print("Hola")
saludar()

# %% Llamar a la función
def bienvenida():
 print("Bienvenido al curso")
bienvenida()

# %% Predice el orden de ejecución 
def uno():
 print("A")
print("B")
uno()
print("C")
      
# %% Corrige el orden
def saludar(nombre):
 print("Hola,", nombre)

saludar("Ana")
# %% Función con un parámetro 
def saludar(nombre):
 print("Hola,", nombre)
saludar("Ana")
# %% Función con dos parámetros 
def area(base, altura):
 return base * altura
print(area(3, 4))

# %% Completa la llamada
def area(base, altura):
 return base * altura
print(area(5.0, 5.0))
# %% Reutilizar la misma función
def con_iva(precio):
 return precio * 1.19
print(con_iva(1.500))
print(con_iva(1.000))
print(con_iva(150.000))

# %% Parámetro o argumento 
def doble(n):
 return n * 2
resultado = doble(5)

# %%  Argumentos por posición
def perfil(nombre, edad, ciudad):
 print(nombre, edad, ciudad)
perfil("ana",20,"bogota")

# %% Argumentos por nombre
def perfil(nombre, edad, ciudad):
 print(nombre, edad, ciudad)
perfil(edad=20, nombre="Ana", ciudad="Bogota")

# %% Valor por defecto
def saludar(nombre, saludo= "hola"):
 print(saludo, nombre)
saludar("Ana")

# %% Reemplazar el valor por defecto
def saludar(nombre, saludo="hola"):
 print(saludo, nombre)
saludar("luis", "buen dia" )

# %% Orden de los parámetros
def registrar(producto, cantidad=1):
    print(producto, cantidad)
# %% Una lista como argumento
def total(precios):
    suma = 0
    for p in precios:
        suma = suma + p
    return suma

print(total([1200, 950, 3400]))
# %% Devolver un valor
def doble(n):
 return n * 2
print(doble(5))

# %% Función sin return
def saludo(nombre):
 print("Hola,", nombre)
x = saludo("Ana")
print(x)
# %% print o return
def doble(n):
    return n * 2

total = doble(5) + 3
print(total)
# %% return dentro de una condición
def signo(n):
    if n < 0:
        return "negativo"
    return "positivo"

print(signo(-4))
print(signo(7))
# %% return termina la función
def prueba(n):
  if n > 0:
    return "positivo"
  print("linea intermedia")
  return "otro"
print(prueba(5))
# %% Devolver dos valores
def resumen(valores):
    return min(valores), max(valores)

menor, mayor = resumen([8, 3, 10, 5])
print(menor, mayor)
# %% Encadenar funciones
def con_iva(p):
    return p * 1.19

def redondear(valor):
    return round(valor, 2)

print(redondear(con_iva(1200)))
# %%
mensaje = "global"
def prueba():
 mensaje = "local"
 print(mensaje)
prueba()
print(mensaje)
# %% Evitar las variables globales 
iva = 0.19
def con_iva(precio):
 return precio * (1 + iva)
# %% No modificar el origina
def agregar(lista):
    nueva = lista + [3]
    return nueva

datos = [1, 2]
print(agregar(datos))
print(datos)
# %% Función que recibe una lista 
def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)

print(promedio([3.5, 4.2, 2.8]))
# %% Función que recibe un diccionario 
def describir(alumno):
    print(alumno["nombre"], alumno["nota"])

describir({"nombre": "Laura", "nota": 4.6})
# %%
def aprobados(estudiantes):
    resultado = []
    for e in estudiantes:
        if e["nota"] >= 3.0:
            resultado.append(e["nombre"])
    return resultado

datos = [{"nombre": "Ana", "nota": 4.2},
         {"nombre": "Luis", "nota": 2.8}]
print(aprobados(datos))
# %% Reporte de notas con funciones
def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)

def aprueba(prom, minimo=3.0):
    return prom >= minimo

def reporte(nombre, notas):
    prom = promedio(notas)
    print(nombre, round(prom, 2))
    if aprueba(prom):
        print("Aprobado")
    else:
        print("No aprobado")

reporte("Laura", [3.5, 4.2, 2.8])
# %%
