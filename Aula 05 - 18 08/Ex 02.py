''' Q 18-01
Um palíndromo é uma frase ou palavra que se lê da mesma forma da esquerda pra direita e vice-e-versa. Por exemplo: radar.
Escreva um programa que usa uma função recursiva para determinar se uma string é um palíndromo ou não.
'''
txt = str(input("Insira a palavra para análise: "))

def inverter():
    reversed_string = ''.join(reversed(txt))

    if(reversed_string == txt):
        print("A palavra ", txt, " é um palindromo!")
        print(txt, " = ", reversed_string)
    else:
        print("A palavra não é um palindromo!")

inverter()