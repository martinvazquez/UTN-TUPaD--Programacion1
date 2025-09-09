# Alumno: Martin Vazquez
# Comision: 8

def exercise_01():
    """1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja."""

    grades = [6.3, 4.3, 5.8, 9.2, 7.5, 8.0, 8.2, 9.5, 7.7, 7.9]
    print(f"Notas: {grades}")

    min_grade = min(grades)
    max_grade = max(grades)
    print(f"La menor nota es: {min_grade}, y la mayor nota es: {max_grade}")

    """
    from https://docs.python.org/3/library/functions.html#min
    
    min(iterable, /, *, key=None)
    min(iterable, /, *, default, key=None)
    min(arg1, arg2, /, *args, key=None)

    Return the smallest item in an iterable or the smallest of two or more arguments.
    --------------------------------------------------
    from https://docs.python.org/3/library/functions.html#max

    max(iterable, /, *, key=None)
    max(iterable, /, *, default, key=None)
    max(arg1, arg2, /, *args, key=None)

    Return the largest item in an iterable or the largest of two or more arguments.
    """


def exercise_02():
    """Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista."""
    
    QUANTITY = 5
    product_list = []

    # ciclo para la carga de productos
    for _ in range(QUANTITY):
        product = input("Ingrese un producto: ")
        product_list.append(product)

    print(sorted(product_list))

    # ciclo para validar el ingreso de un producto válido
    while True:
        item_to_remove = input("Ingrese el producto que desea remover de la lista:")

        try:
            product_list.remove(item_to_remove)
            break
        except ValueError:
            print("El producto ingresado no existe en la lista.")

    print(sorted(product_list))

    # otra forma de hacerloe s mostrar la lista como un menu indexado
    # y solicitar al usuario el numro de indice del producto a remover

    """
    from https://docs.python.org/3/library/functions.html#sorted

    sorted(iterable, /, *, key=None, reverse=False)

    Return a new sorted list from the items in iterable.
    --------------------------------------------------
    - La exepcion ValueError ocurre cuando se intenta remover un elemento que no existe en la lista.
    La uso en un ciclo para validary forzar la entrada válida de un producto por parte del usuario
    """
       

def exercise_03():
    """Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista."""
    
    import random

    SIZE = 15
    numbers = []
    even_list = []  # pares
    odd_list = []   # impares

    for _ in range(SIZE):
        numbers.append(random.randint(1,100))

    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    print("Lista de números:", numbers)
    print("Lista de números pares", even_list)
    print("Lista de números impares", odd_list)


def exercise_04():
    """Dada una lista con valores repetidos:
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado."""
    
    datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
    uniques = list(set(datos))

    print("Datos originales:", datos)
    print("Datos sin repetir:", uniques)

    """
    set se parece a una lista, pero no permite almacenar elementos duplicados
    asi que se puede crear un set a partir de una lista, esto elimina los elementos duplicados
    y por ultimo se crea una lista a partir de este set porque 
    el ejercicio pide una lista y una lista no es lo mismo que un set
    """


def exercise_05():
    """Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada."""
    
    ADD = '+'
    REMOVE = '-'

    student_list = ["maria", "juan", "laura", "pedro", "leticia", "francisco", "virginia", "esteban"]
    print("Estudiantes actuales:", sorted(student_list))

    while True:
        option = input(f"Ingrese {ADD} para agregar un nuevo estudiante, {REMOVE} para removerlo: ")

        if option in [ADD, REMOVE]:
            break

        print(f"{option} no es una opción valida.")

    student = input("Ingrese el nombre del estudiante: ")

    if option == ADD:
        student_list.append(student)
        print(f"El estudiante {student} se agregó correctamente")
    else:
        try:
            student_list.remove(student)
            print(f"El estudiante {student} se eliminó correctamente")
        except ValueError:
            print(f"El estudiante {student} no existe en la lista")

    print("Lista actulizada:", sorted(student_list))


def exercise_06():
    """Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero)."""
    
    # se crea una lista de 7 enteros (0-6)
    numbers = list(range(7))
    print("lista original:", numbers)

    # usando slices
    # se arma una lista con los elementos del 
    # segundo elemento de la lista hasta el final (numbers[1:] es [1, 2, 3, 4, 5])
    # y lo concatenamos el primer elemento de la lista al final (number[:1] es [0])
    # numbers = numbers[1:] + numbers[:1]

    # CORRECCION: lo anterior está, rota a la izquierda, pero se pide rotar a la derecha
    numbers = numbers[-1:] + numbers[:-1]
    print("lista rotada:", numbers)
    

def exercise_07():
    """Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica."""
    
    MIN = 0
    MAX = 1
    DAYS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    temperatures = [
        [4.5, 26.7],    # lunes
        [5.7, 28.4],    # martes
        [8.3, 28.5],    # miercoles
        [9.5, 31.4],    # jueves
        [7.1, 27.2],    # viernes
        [5.2, 25.6],    # sabado
        [3.3, 23.4]     # domingo
    ]
    
    max_thermal_range = -1000
    max_thermal_range_day = ""
    thermal_average_min = 0
    thermal_average_max = 0
    
    for index, temperature in enumerate(temperatures):
        thermal_range = temperature[MAX] - temperature[MIN] # falta guardar el dia
        
        if thermal_range > max_thermal_range:
            max_thermal_range = thermal_range
            max_thermal_range_day = index       # guardo el indice (dia)

        thermal_average_min += temperature[MIN]
        thermal_average_max += temperature[MAX]

    thermal_average_min /= len(temperatures)
    thermal_average_max /= len(temperatures)

    for index, day in enumerate(DAYS):
        print(f"{day:10} \t Min.: {temperatures[index][MIN]} - Max.: {temperatures[index][MAX]}")


    print(f"\nPromedio de la temperatura mínima: {thermal_average_min:.1f}°")
    print(f"Promedio de la temperatura máxima: {thermal_average_max:.1f}°")

    print(f"\nLa máxima amplitud térmica fúe de {max_thermal_range} y se registró el día {DAYS[max_thermal_range_day]}")
    

    
def exercise_08():
    """Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia."""

    import random

    # listas de cadenas con la longitud de la matriz para mejorar la visualizacion
    # con solo modificar estas listas se modifica la lista resultante
    students = ["Galileo", "Marie", "John", "Hedy", "Alan",]
    courses = ["Programacion", "Matematicas", "Bases de Datos", "asas"]

    # list comprehensions para cargar las notas aleatoriamente y de tamaño dinámico
    # https://docs.python.org/3.8/tutorial/datastructures.html#list-comprehensions
    grades = [[random.randint(1,100) for _ in courses] for _ in students]

    # calcular promedio de cada estudiante, se almacenan en una lista
    student_averages = []
    for grade in grades:
        student_averages.append(sum(grade) / len(grade))

    # calcular promedio de cada materia, se almacenan en una lista
    course_averages = [0] * len(courses)    
    for i in range(len(students)):
        for j in range(len(courses)):
            course_averages[j] += grades[i][j]  # suma aqui
    
    for i, _ in enumerate(course_averages):
        course_averages[i] /= len(students)      # division aqui

    # se muestran las notas y promedios caclculados en una misma tabla
    # se usa generator expressions para hacer le codigo mas conciso
    # https://docs.python.org/3/reference/expressions.html#generator-expressions
    header = f"{'Estudiante':15}" + "".join(f"{course:15}" for course in courses) + f"{'Promedio E.':15}"
    print(header)
    print("-" * len(header))

    # se imprimen las notas y el promedio de estudiante
    for i, student in enumerate(students):
        row = f"{student:15}" + "".join(f"{grade:<15}" for grade in grades[i]) + f"{student_averages[i]:<15.1f}"
        print(row)

    # se imprime el promedio de cada materia
    print("-" * len(header))
    footer = f"{'Promedio M.':15}" + "".join(f"{course_average:<15.1f}" for course_average in course_averages)
    print(footer)



    """ ejemplo de salida

Estudiante     Programacion   Matematicas    Bases de Datos Promedio E.    
---------------------------------------------------------------------------
Galileo        93             19             93             68.3           
Marie          3              99             69             57.0           
John           49             3              79             43.7           
Hedy           91             76             74             80.3           
Alan           54             69             74             65.7           
---------------------------------------------------------------------------
Promedio M.    58.0           53.2           77.8                   

    """

    
def exercise_09():
    """Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada."""

    PLAYER1 = 'X'
    PLAYER2 = 'O'
    CURRENT_PLAYER = PLAYER1

    def draw_board(board):
        """imprime un tablero (3x3) en pantalla"""

        print("    0  1  2")
        for idx, row in enumerate(board):
            print(f" {idx} ", end="")
            for col in row:
                print(f"[{col}]", end="")
            print()

    
    def play(board, row, col, player) -> bool: 
        """coloca la pieza en el tablero, retorna:
        True en caso de éxito
        False, en caso de error (rango invalido o celda ocupada)
        """

        # se valida que la fila seleccionada se valida        
        if row not in range(len(board)):
            return False
        
        # se valida que la columna seleccionada sea valida
        if col not in range(len(board[0])):
            return False
        
        # se valida que la celda no este ocupada
        if board[row][col] != '-':
            return False
        
        board[row][col] = player
        return True


    # se crea una matriz/tablero de 3x3 inicializa con '-'
    # list comprehension para ser mas concisos
    board = [['-' for _ in range(3)] for _ in range(3)]

    # se dibuja el tablero inicial
    draw_board(board)

    # se juega hasta llenar el tablero (no se valida el juego en si)
    for _ in range(9):
        # se pide al jugador actual que ingrese fila y columna
        print(f"\nTurno de: {CURRENT_PLAYER}")

        while True:
            try:
                row, col = input("Ingrese la fila y columna (separados por coma): ").split(",")
                row = int(row)
                col = int(col)
            except ValueError:
                print("La fila y columna no son válidas")
                continue

            if play(board, row, col, CURRENT_PLAYER):
                break
            else:
                print("La fila y columna exceden los limites del tablero o la celda esta ocupada")
       
        # se dibuja el tablero
        draw_board(board)

        # se alterna el jugador
        CURRENT_PLAYER = PLAYER1 if CURRENT_PLAYER == PLAYER2 else PLAYER2


    
def exercise_10():
    """Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana."""
    
    import random

    # listas de cadenas con la longitud de la matriz para mejorar la visualizacion y hacerlo dinamico    
    products = ["Harina", "Azucar", "Aceite", "Leche"]
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # list comprehensions para cargar ventas aleatoriamente y de tamaño dinámico
    sales = [[random.randint(1,100) for _ in days] for _ in products]

    # se calculan las ventas totales por producto (de aquí se encuentra el producto más vendido)
    sales_per_product = []
    for sale in sales:
        # se obtiene la fila, es decir las ventas de un producto todos los dias
        # por lo tanto con solo sumar esa fila/lista se obtiene el total de ventas de ese producto
        sales_per_product.append(sum(sale))
    
    # se calculan las ventas totales por día (para encontrar el dia con mayor ventas)
    sales_per_day = [0] * len(days)
    for sale in sales:
        for idx, day in enumerate(days):
            sales_per_day[idx] += sale[idx]

    # se imprimen las ventas de la semana  
    header = f"{'Producto':15}" + "".join(f"{day:15}" for day in days) + f"{'Total x P.':15}"
    print(header)
    print("-" * len(header))
    
    for i, product in enumerate(products):
        row = f"{product:15}" + "".join(f"{sale:<15}" for sale in sales[i]) + f"{sales_per_product[i]:<15}"
        print(row)
        
    print("-" * len(header))
    footer = f"{'Total x D.':15}" + "".join(f"{sale_per_day:<15}" for sale_per_day in sales_per_day)
    print(footer)

    # se muestra el producto mas vendido de la semana
    top_product_sales = max(sales_per_product)
    top_product_name = products[sales_per_product.index(top_product_sales)]
    print(f"\nEl producto mas vendido de la semana es {top_product_name} con {top_product_sales} ventas.")

    # se muestra el dia con mas ventas de la de la semana
    top_day_sales = max(sales_per_day)
    top_day_name = days[sales_per_day.index(top_day_sales)]
    print(f"El día con mas ventas fue el {top_day_name} con {top_day_sales} ventas.")


    """
    https://docs.python.org/3/library/functions.html#max

    la funcion max() retorna el elemento mas grande de un iterable o de dos o mas argumentos

    https://docs.python.org/3/tutorial/datastructures.html

    list.index(x[, start[, end]])
    retorna el indice del primera ocurrencia del elemento c en la lista    

    ejemplo de salida:

Producto       Lunes          Martes         Miércoles      Jueves         Viernes        Sábado         Domingo        Total x P.     
---------------------------------------------------------------------------------------------------------------------------------------
Harina         81             92             15             54             83             54             70             449            
Azucar         7              45             40             19             84             67             70             332            
Aceite         89             59             34             4              81             12             58             337            
Leche          9              71             21             74             34             47             25             281            
---------------------------------------------------------------------------------------------------------------------------------------
Total x D.     186            267            110            151            282            180            223            

El producto mas vendido de la semana es Harina con 449 ventas.
El día con mas ventas fue el Viernes con 282 ventas.
    """

    
if __name__ == '__main__':
    # add exercises in order
    exercises = [exercise_01, exercise_02, exercise_03, exercise_04, exercise_05,
                 exercise_06, exercise_07, exercise_08, exercise_09, exercise_10]

    print("Trabajo Practico N° 5 - Listas")
    option = int(input(f"Ingrese el nro de ejercicio que desea ejecutar (1-{len(exercises)}): "))

    if option >= 1 and option <= len(exercises):
        print(f"\nEjecutando ejercicio {option}:\n\n{exercises[option-1].__doc__}\n")
        exercises[option-1]()
    else:
        print("Opcion inválida")
