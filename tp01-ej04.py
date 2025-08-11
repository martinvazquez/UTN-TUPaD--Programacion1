import math

radio = float(input("Ingrese el radio de un círculo: "))
area = math.pi * radio ** 2
perimetro = 2 + math.pi * radio

print(f"El círculo de radio {radio} tiene:\n\tperímetro = {perimetro}\n\tárea = {area}")