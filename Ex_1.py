# Variables y tipos de datos

# Asignación de valores a variables
# Uso input para pedir al usuario los valores asignados, el texto entre comillas dentro del paréntesis
# es lo que se muestra al usuario al momento de pedir el valor
nombre = input("Ingresa el nombre: ") 
# Se usa int para convertir el input del usuario que es un string(cadena de caracteres) a un integral
# para su futuro uso en el if de linea 
edad = int(input("Ingresa la edad: "))
altura = input("Ingresa la altura: ")

# Para obtener el valor en True/False como está originalmente el código y no tener que modificar de más
# añadí una nueva variable con el input y uso un if else para asignar las posibles respuestas del 
# usuario a un True False y eso lo meto a la variable original
# También agregué una condicional or por si alguien no usa mayúsculas

estudiante = input("¿Es estudiante? (Si//No): ")
if estudiante == 'Si' or estudiante  == 'si':
    es_estudiante = True
else:
    es_estudiante = False

# Imprimir el contenido de las variables
print("Mi nombre es", nombre)
print("Tengo", edad, "años")
print("Mi altura es", altura, "metros")
print("¿Soy estudiante?", es_estudiante)

# Estructuras de control: condicionales

if edad >= 18:  # Si la edad es mayor o igual a 18
    print("Soy mayor de edad")
else:
    print("Soy menor de edad")

# Estructuras de control: bucles

# Bucle while
contador = 0
while contador < 5:
    print("El contador es", contador)
    contador += 1

# Bucle for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta comer", fruta)

# Funciones

# Definición de una función
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Llamada a la función
base_rectangulo = 4
altura_rectangulo = 6
area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
print("El área del rectángulo es:", area_rectangulo)
A=12
B=23
Area2 = calcular_area_rectangulo(A, B)
print("El área del rectángulo es:", Area2)

# Módulos

# Importar el módulo math
import math

# Utilizar una función del módulo math
raiz_cuadrada = math.sqrt(25)
print("La raíz cuadrada de 25 es:", raiz_cuadrada)