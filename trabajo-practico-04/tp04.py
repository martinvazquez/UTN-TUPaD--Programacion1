# Alumno: Martin Vazquez
# Comision: 8

def exercise_01():
    """Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
    
    for i in range(101):
        print(i)


def exercise_02():
    """Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
        
    # ciclo para solicitar numero válido
    while True:
        try:
            number = int(input("Ingrese un número: "))
            break
        except ValueError:
            print("Ingrese un número válido")

    digits = 0

    # caso excepcional: defino que el número 0 tiene 1 dígito 
    if number == 0:
        digits = 1 

    aux = abs(number)

    # cuento la cantidad de digitos diviendo el numero sucesivamente por 10
    while aux > 0:
        aux //= 10        
        digits += 1

    print(f"El número {number} tiene {digits} dígitos")

    """
    - La exepcion ValueError ocurre cuando se intenta convertir una cadena que no representa a un número valido.
    La uso en un ciclo para validary forzar la entrada válida de un número por parte del usuario
    """
       

def exercise_03():
    """Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""
    
     # ciclo para solicitar numeros válidos
    while True:
        try:
            number1 = int(input("Ingrese un número (limite inferior del rango): "))
            number2 = int(input("ingrese un número (limite superior del rango): "))
            break
        except ValueError:
            print("Ingrese dos números válidos")

    # ordeno el rango si es necesario
    if number1 > number2:
        number1, number2 = number2, number1

    sum = 0

    for i in range (number1+1, number2):
        sum += i

    print(f"La suma de los numeros en el rango abierto ({number1}, {number2}) es de {sum}")


def exercise_04():
    """Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0."""
    
    sum = 0

    # ciclo para leer numeros
    while True:
        # ciclo para leer un numero válido
        while True:
            try:
                number = int(input("Ingrese un número para sumar (ingrese 0 para salir): "))
                break
            except ValueError:
                print("Ingrese un número válido")

        if number == 0:
            break

        sum += number

    print(f"La suma de los números ingresados es: {sum}")


def exercise_05():
    """Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
    
    import random

    attempts = 1
    random_number = random.randint(0,9)

    # ciclo para leer el numero adivinado del usario
    while True:
        # ciclo para leer un numero válido
        while True:
            try:
                number = int(input("¿Qué número entre 0 y 9 tengo?: "))
                break
            except ValueError:
                print("Ingrese un número válido")

        if number == random_number:
            break

        print(f"Fallaste, no era el {number}. Intenta de nuevo.")
        attempts += 1

    print(f"Adivinaste, el número era el {random_number} y lo hiciste en {attempts} intentos")

    """
    - El ciclo no termina hasta que el número se adivine
    """


def exercise_06():
    """Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""
    
    for i in range(100, -1, -2):
        print(i)

    
def exercise_07():
    """Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario"""
    
    while True:
        try:
            number = int(input("Ingrese un número positivo (): "))
            if number < 0:
                continue
            break
        except ValueError:
            print("Ingrese un número válido.")

    sum = 0

    for i in range(0, number+1, 2):
        sum += i

    print(f"La suma de números pares del rango cerrado [0, {number}] es: {sum}")

    
def exercise_08():
    """Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
    
    MAX_NUMBERS = 10    # CAMBIAR AQUI LA CANTIDAD DE NUMEROS A LEER

    odd = even = positive = negative = 0

    # ciclo para leer los numeros
    for _ in range(MAX_NUMBERS):
        # ciclo para leer un válido
        while True:
            try:
                number = int(input("Ingrese un número: "))
                break
            except ValueError:
                print("Ingrese un número válido.")

        # el n° cero es neutral (no es negativo ni positivo)
        
        if number > 0:
            positive += 1
        else:
            negative += 1

        # el número cero es positivo!
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        
    print(f"\nSe ingresaron {MAX_NUMBERS} números, de los cuales:")
    print(f"\t{positive} son positivos\n\t{negative} son negativos\n\t{even} son pares\n\t{odd} son impares")

    
def exercise_09():
    """Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)"""
    
    MAX_NUMBERS = 10

    sum = 0

    for i in range(MAX_NUMBERS):
        # 
        while True:
            try:
                number = int(input("Ingrese un número: "))
                break
            except ValueError:
                print("Ingrese un número válido")

        sum += number

    print(f"La media de los {MAX_NUMBERS} números ingresados es {sum/MAX_NUMBERS}")

    
def exercise_10():
    """Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""
    
    while True:
        try:
            number = int(input("Ingrese un número: "))
            break
        except ValueError:
            print("Ingrese un número válido")

    unit = inverse = 0

    # mantengo el numero ingresado para mostrarlo luego
    aux = abs(number)

    while aux > 0:
        # se obtiene el último digito
        unit = aux % 10
        # se arma el numero inverso
        # al número existente lo muevo un lugar a la izquierda para hacer lugar para el nuevo digito
        inverse = inverse * 10 + unit
        # del número original elimino la unidad que ya se proceso (trunc)
        aux //= 10

    # obtengo el signo del número (si el número es cero, tomo signo positivo)
    # si divido un número por su absoluto, obtengo 1 o -1 segun el signo del número
    sign = number // abs(number) if number != 0 else 1

    print(f"El número inverso de {number} es {inverse*sign}")

    
if __name__ == '__main__':
    # add exercises in order
    exercises = [exercise_01, exercise_02, exercise_03, exercise_04, exercise_05,
                 exercise_06, exercise_07, exercise_08, exercise_09, exercise_10]

    option = int(input(f"Ingrese el nro de ejercicio que desea ejecutar (1-{len(exercises)}): "))

    if option >= 1 and option <= len(exercises):
        print(f"\nEjecutando ejercicio {option}:\n\n{exercises[option-1].__doc__}\n")
        exercises[option-1]()
    else:
        print("Opcion inválida")
