''' Q 19-01
Escreva um programa que usa a função map() para realizar operações de multiplicação com os itens da lista n_list = [10, 20, 30]. 
O programa deve imprimir 2x e 3x os valores de n_list.
'''
n_list = [10, 20, 30]

def doisX (x):
    return x * 2

def tresX (y):
    return y * 3

def multList2():
    doisVezes = list(map(doisX, n_list))
    print("A lista multiplicada por 2:", doisVezes)

def multList3():
    tresVezes = list(map(tresX, n_list))
    print("A lista multiplicada por 3:", tresVezes)

multList2()
multList3()