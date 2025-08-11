segundos_ingresados = int(input("Ingrese la cantidad de segundos: "))

# el operador // es la division entera (redondea hacia abajo, trunca)
horas = segundos_ingresados // (60 * 60)
minutos = (segundos_ingresados % (60 * 60)) // 60
segundos = segundos_ingresados % 60


print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos")