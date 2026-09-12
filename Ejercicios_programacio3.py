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
def registrar(cantidad=1, producto):
 print(producto, cantidad)
# %%
