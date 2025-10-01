# Alumno: Martin Vazquez
# Comision: 8


"""
Creo estas funciones auxiliares para leer números enteros y decimales
con validación de entrada, opcionalmente puede validar si el número es positivo o no. 
Las uso en varios ejercicios y lo hago para evitar repetir tantas validaciones en cada ejercicio.
Aprovecho para practicar el concepto de funciones.
"""

def leer_numero_entero(prompt, positivo=False):
    """Lee un número entero desde la entrada estándar, validando la entrada."""
    while True:
        try:
            number = int(input(prompt))
            if positivo and number < 0:
                print("El número debe ser positivo")
                continue
            return number
        except ValueError:
            print("Ingrese un número entero válido")    


def leer_numero_decimal(prompt, positivo=False):
    """Lee un número decimal desde la entrada estándar, validando la entrada."""
    while True:
        try:
            number = float(input(prompt))
            if positivo and number < 0:
                print("El número debe ser positivo")
                continue
            return number
        except ValueError:
            print("Ingrese un número decimal válido")   


def exercise_01():
    """Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""
    
    def imprimir_hola_mundo():
        print("Hola Mundo!")

    imprimir_hola_mundo()


def exercise_02():
    """Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""
    
    def saludar_usuario(nombre):
        return f"Hola {nombre}!"

    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))


def exercise_03():
    """Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados."""
    
    def informacion_personal(nombre, apellido, edad, residencia):
        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = leer_numero_entero("Ingrese su edad: ", positivo=True)
    residencia = input("Ingrese su lugar de residencia: ")

    informacion_personal(nombre, apellido, edad, residencia)


def exercise_04():
    """Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados."""

    import math

    def calcular_area_circulo(radio):
        return math.pi * radio ** 2

    def calcular_perimetro_circulo(radio):
        return 2 * math.pi * radio
    
    radio = leer_numero_decimal("Ingrese el radio del círculo: ", positivo=True)

    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")


def exercise_05():
    """Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función."""
    
    def segundos_a_horas(segundos):
        return segundos / (60 * 60)
    
    segundos = leer_numero_entero("Ingrese la cantidad de segundos: ", positivo=True)

    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos son {horas:.2f} horas")


def exercise_06():
    """Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción."""

    def tabla_multiplicar(numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

    numero = leer_numero_entero("Ingrese un número para ver su tabla de multiplicar: ")
    tabla_multiplicar(numero)

def exercise_07():
    """Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
sultados de forma clara."""

    def operaciones_basicas(a, b):
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        # retorno None si b es 0 para evitar division por 0
        # el cliente de la función debe manejar este caso
        division = a / b if b != 0 else None    
        return (suma, resta, multiplicacion, division)
    
    a = leer_numero_decimal("Ingrese el primer número: ")
    b = leer_numero_decimal("Ingrese el segundo número: ")

    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    if division is not None:
        print(f"División: {division}")
    else:
        print("División: No se puede dividir por cero")


def exercise_08():
    """Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
ción para mostrar el resultado con dos decimales."""

    # (IMC = peso (kg)/ [estatura (m)]2

    def calcular_imc(peso, altura):
        return peso / (altura ** 2)

    peso = leer_numero_decimal("Ingrese su peso en kilogramos: ", positivo=True)
    altura = leer_numero_decimal("Ingrese su altura en metros: ", positivo=True)

    imc = calcular_imc(peso, altura)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")


def exercise_09():
    """Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

    # Celsius a Fahrenheit. (°C x 9/5) + 32 =°F

    def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    celsius = leer_numero_decimal("Ingrese la temperatura en grados Celsius: ")

    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C son {fahrenheit:.2f}°F")


def exercise_10():
    """Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""

    def calcular_promedio(a, b, c):
        return (a + b + c) / 3

    a = leer_numero_decimal("Ingrese el primer número: ")
    b = leer_numero_decimal("Ingrese el segundo número: ")
    c = leer_numero_decimal("Ingrese el tercer número: ")

    promedio = calcular_promedio(a, b, c)
    print(f"El promedio de {a}, {b} y {c} es {promedio:.2f}")


def exercise_10b():
    """Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
Aplicando lo aprendido en Listas la función puede recibir una lista 
y la aplicacion resulta más flexible."""

    # version alternativa usando listas
    def calcular_promedio(numeros):
        return sum(numeros) / len(numeros)
    

    CANTIDAD_NUMEROS = 3

    # podriamos usar una constante o pedir al usuario la cantidad de números a promediar
    # o podriamos usar un ciclo infinito y una condición de salida
    # pero para no complicar más el ejercicio lo dejo así
    
    numeros = []
    for i in range(CANTIDAD_NUMEROS):
        numero = leer_numero_decimal(f"Ingrese el número {i+1}: ")
        numeros.append(numero)  
    
    promedio = calcular_promedio(numeros)
    print(f"El promedio de {numeros} es {promedio:.2f}")
    

if __name__ == '__main__':
    # add exercises in order
    exercises = [exercise_01, exercise_02, exercise_03, exercise_04, exercise_05,
                 exercise_06, exercise_07, exercise_08, exercise_09, exercise_10, exercise_10b]

    print("Trabajo Practico N° 6 - Funciones")
    option = int(input(f"Ingrese el nro de ejercicio que desea ejecutar (1-{len(exercises)}): "))

    if option >= 1 and option <= len(exercises):
        print(f"\nEjecutando ejercicio {option}:\n\n{exercises[option-1].__doc__}\n")
        exercises[option-1]()
    else:
        print("Opcion inválida")