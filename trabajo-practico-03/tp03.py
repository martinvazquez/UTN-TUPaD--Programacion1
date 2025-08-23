# Alumno: Martin Vazquez
# Comision: 8

def exercise_01():
    """ Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
    deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""
    age = int(input("Ingrese su edad: "))

    # considero tener 18 años como ser mayor de edad por eso '>='
    if age >= 18:
        print("Es mayor de edad")


def exercise_02():
    """Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
    mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
    mensaje “Desaprobado”."""

    grade = int(input("ingrese su calificacion (0-10): "))

    if grade >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


def exercise_03():
    """Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
    número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
    contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
    operador de módulo (%) en Python para evaluar si un número es par o impar."""

    number = int(input("Ingrese un número par: "))

    if number % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")


def exercise_04():
    """Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
    siguientes categorías pertenece:
    ●​ Niño/a: menor de 12 años.
    ●​ Adolescente: mayor o igual que 12 años y menor que 18 años.
    ●​ Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    ●​ Adulto/a: mayor o igual que 30 años."""

    age = int(input("Ingrese su edad: "))

    if age < 12:
        print("Niño/a")
    elif age >= 12 and age < 18:
        print("Adolescente")
    elif age >= 18 and age < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")


def exercise_05():
    """Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
    (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
    pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
    pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
    de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
    como una lista o un string."""

    password = input("Ingrese una contraseña de longitud de entre 8 14 caracteres: ")

    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

    """
    Para leer contraseñas desde el teclado de forma mas segura es aconsejable usar el modulo getpass.
    De esta forma la contraseña no se muestra en pantalla mientras se ingresa.

    import getpass
    password = getpass.getpass("Ingrese una contraseña de longitud de entre 8 14 caracteres: ")
    """


def exercise_06():
    """El paquete statistics de python contiene funciones que permiten tomar una lista de números
    y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
    from statistics import mode, median, mean
    mi_lista = [1,2,5,5,3]
    mean(mi_lista)
    En la documentación oficial se puede encontrar más información sobre este paquete:
    https://docs.python.org/es/3.8/library/statistics.html.
    La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
    pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
    ●​ Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
    mediana es mayor que la moda.
    ●​ Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
    la mediana es menor que la moda.
    ●​ Sin sesgo: cuando la media, la mediana y la moda son iguales.
    Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
    numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
    hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
    Definir la lista numeros_aleatorios de la siguiente forma:
    import random
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
    forma aleatoria."""

    from statistics import mode, median, mean
    import random

    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

    media = mean(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    moda = mode(numeros_aleatorios)

    print(f"media: {media} - mediana: {mediana} - moda: {moda}")

    if media > mediana > moda:      # es lo mismo y mas corto que: media > mediana and mediana > moda
        print("Sesgo positivo a la derecha")
    elif media < mediana < moda:    # es lo mismo y mas corto que: media < mediana and mediana < moda
        print("Sesgo negativo o a la izquierda")
    else:
        print("Sin sesgo")


def exercise_07():
    """Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
    termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
    pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
    pantalla."""

    word = input("Ingrese una palabra o frase: ")
    if word[-1] in "aeiouáéíóú":
        word += '!'

    print(word)

    """
    word[-1] obtiene el ultimo caracter/elemento del string/arreglo/lista
    """


def exercise_08():
    """Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
    dependiendo de la opción que desee:
    1.​ Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    2.​ Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    3.​ Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
    El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
    usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
    lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

    MAYUS = 1
    MINUS = 2
    TITLE = 3

    name = input("Ingrese su nombre: ")
    style = int(input("Ingrese el número de estilo que desea para imprimir su nombre \n1 - Masyuculas\n2 - Minusculas\n3 - Título\nopcion: "))

    if style == MAYUS:
        print(name.upper())
    elif style == MINUS:
        print(name.lower())
    elif style == TITLE:
        print(name.title())


def exercise_09():
    """Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
    magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
    por pantalla:
    ●​ Menor que 3: "Muy leve" (imperceptible).
    ●​ Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    ●​ Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
    generalmente no causa daños).
    ●​ Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
    débiles).
    ●​ Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    ●​ Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

    magnitude = float(input("Ingrese la magnitud del terremoto: "))

    if magnitude < 3:
        print("Muy leve")
    elif 3 <= magnitude < 4:
        print("Leve")
    elif 4 <= magnitude < 5:
        print("Moderado")
    elif 5 <= magnitude < 6:
        print("Fuerte")
    elif 6 <= magnitude < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")


def exercise_10():
    """Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
    +------------------------------------------------------------+---------------------------+---------------------------+
    | Periodo del año                                            | Estación en el hemisferio | Estación en el hemisferio |
    |                                                            | norte                     | sur                       |
    +------------------------------------------------------------+---------------------------+---------------------------+
    | Desde el 21 de diciembre hasta el 20 de marzo (incl.)      | Invierno                  | Verano                    |
    +------------------------------------------------------------+---------------------------+---------------------------+
    | Desde el 21 de marzo hasta el 20 de junio (incl.)          | Primavera                 | Otoño                     |
    +------------------------------------------------------------+---------------------------+---------------------------+
    | Desde el 21 de junio hasta el 20 de septiembre (incl.)     | Verano                    | Invierno                  |
    +------------------------------------------------------------+---------------------------+---------------------------+
    | Desde el 21 de septiembre hasta el 20 de diciembre (incl.) | Otoño                     | Primavera                 |
    +------------------------------------------------------------+---------------------------+---------------------------+
    Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
    del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
    si el usuario se encuentra en otoño, invierno, primavera o verano."""

    import sys

    NORTH = 'n'
    SOUTH = 's'

    SUMMER = 'Verano'
    WINTER = 'Invierno'
    AUTUMN = 'Otoño'
    SPRING = 'Primavera'

    hemisphere = input("Ingrese el hemisferio en el que se encuentra (N/S): ")

    if hemisphere.lower() not in [NORTH, SOUTH]:
        print("Hemisferio invalido (NnSs)")
        sys.exit(1)

    month = int(input("Ingrese el número del mes actual (1-12): "))
    day = int(input("Ingrese el número del día actual (1-31): "))

    # safe months
    if month in [1, 2]:
        north_season = WINTER
    elif month in [4, 5]:
        north_season = SPRING
    elif month in [7, 8]:
        north_season = SUMMER
    elif month in [10, 11]:
        north_season = AUTUMN

    # border months
    elif month == 3:
        north_season = SPRING if day >= 21 else WINTER
    elif month == 6:
        north_season = SUMMER if day >= 21 else SPRING
    elif month == 9:
        north_season = AUTUMN if day >= 21 else SUMMER
    elif month == 12:
        north_season = WINTER if day >= 21 else AUTUMN

    season = north_season
    if hemisphere == SOUTH:
        # invert season
        if north_season == WINTER:
            season = SUMMER
        elif north_season == SPRING:
            season = AUTUMN
        elif north_season == SUMMER:
            season = WINTER
        elif north_season == AUTUMN:
            season = SPRING

    print(f"Se encuentra en la estacion {season}")


if __name__ == '__main__':
    # add exercises in order
    exercises = [exercise_01, exercise_02, exercise_03, exercise_04, exercise_05,
                 exercise_06, exercise_07, exercise_08, exercise_09, exercise_10]

    option = int(input(f"Ingrese el nro de ejercicio que desea ejecutar (1-{len(exercises)}): "))

    if option >= 1 and option <= len(exercises):
        print(f"\nEjecutando ejercicio {option}\n\n{exercises[option-1].__doc__}\n")
        exercises[option-1]()
    else:
        print("Opcion inválida")
