''' Q 17-01
Escreva um programa que recebe dois pontos no plano cartesiano, (x1, y1) e (x2, y2) e imprime a distância entre esses 2 pontos.
'''
import math
while True:
    try:
        x1 = int(input("Insira o x1: "))
        y1 = int(input("Insira o y1: "))
        x2 = int(input("Insira o x2: "))
        y2 = int(input("Insira o y2: "))
        break
    except ValueError:
        print("Você colocou um valor inválido, tente novamente!")

def distDoisPontos ():
    distAB = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    print("A distancia entre os dois pontos é: ", distAB)
    return distAB

distDoisPontos()
