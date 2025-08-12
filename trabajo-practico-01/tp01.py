# PROGRAMACION 1
# Alumno: Martin Vazquez
# Comisión: 8
# Práctico 1: Estructuras secuenciales

# ============================================= Ejercicio 01 =============================================
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


# ============================================= Ejercicio 02 =============================================
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre 
# ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f...) para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


# ============================================= Ejercicio 03 =============================================
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por 
# pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y 
# “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será 
# más sencillo si utilizas print(f...) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# ============================================= Ejercicio 04 =============================================
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla 
# su área y su perímetro.

import math

radio = float(input("Ingrese el radio de un circulo: "))
area = math.pi * radio ** 2
perimetro = 2 + math.pi * radio

print(f"El círculo de radio {radio} tiene:\n\tperímetro = {perimetro}\n\tárea = {area}")


# ============================================= Ejercicio 05 =============================================
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla 
# a cuántas horas equivale.

segundos_ingresados = int(input("Ingrese la cantidad de segundos: "))

# el operador // es la division entera (redondea hacia abajo, trunca)
horas = segundos_ingresados // (60 * 60)
minutos = (segundos_ingresados % (60 * 60)) // 60
segundos = segundos_ingresados % 60

print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos")


# ============================================= Ejercicio 06 =============================================
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla 
# de multiplicar de dicho número.

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1,11):
    print(f"{i} * {numero} = {i * numero}")


# ============================================= Ejercicio 07 =============================================
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el 
# resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingrese un número distinto de cero: "))
numero2 = int(input("Ingrese otro número distinto de cero: "))

print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} / {numero2} = {numero1 / numero2}")
print(f"{numero1} * {numero2} = {numero1 * numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")


# ============================================= Ejercicio 08 =============================================
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa 
# corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# IMC = peso en kg / (altura en m)2

altura = float(input("Ingrese su altura (mt): "))
peso = float(input("Ingrese su peso (kg): "))

imc = peso / altura ** 2

print(f"Su Indice de Masa Corporal es: {imc}")


# ============================================= Ejercicio 09 =============================================
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su 
# equivalente en grados Fahrenheit. Tener en cuenta la siguiente  equivalencia:
# Temperatura en Fahrenheit = (9/5) * Temperatura en Celsius + 32

celsius = float(input("Ingrese una temperatura en grados celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"{celsius}°C = {fahrenheit}°F")


# ============================================= Ejercicio 10 =============================================
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese otro número: "))

promedio = (numero1 + numero2 + numero3) /3

print(f"El promedio de los los números {numero1}, {numero2} y {numero3} es {promedio}")

