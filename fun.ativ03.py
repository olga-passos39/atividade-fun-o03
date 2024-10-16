# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
import math

def calcular_area_base(raio):
    if raio < 0:
        return "O raio não pode ser negativo."
    
    area = math.pi * (raio ** 2)
    return area

resultado = calcular_area_base(5)
print(f"A área do círculo com raio 5 é: {resultado:.2f}")
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.
import math

def calcular_area_base(raio):
    if raio < 0:
        return "O raio não pode ser negativo."
    
    area = math.pi * (raio ** 2)
    return area

def calcular_volume_cilindro(raio, altura):
    if raio < 0 or altura < 0:
        return "O raio e a altura não podem ser negativos."
    
    area_base = calcular_area_base(raio)
    
    volume = area_base * altura
    return volume

raio = int(input("digite o raio"))
altura = int(input("digite a altura"))
resultado = calcular_volume_cilindro(raio, altura)
print(f"O volume do cilindro com raio {raio} e altura {altura} é: {resultado:.2f}")