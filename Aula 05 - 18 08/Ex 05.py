''' Q 21-01
Escreva um programa que faz multiplicação (*) e divisão (/) usando os métodos __mul__ e __truediv__ 
aprendidos na unidade 21. Assumindo que v1 = (30, 40) e v2 = (10, 20),
codifique (escreva a declaração de saída) para retornar a saída abaixo como 
resultado da multiplicação e divisão de dois vetores.

v1 * v2 = (300, 800)
v1 / v2 = (3.0, 2.0)
'''
v1 = (30, 40)
v2 = (10, 20)
listdiv = []
listmult = []

a = (v1[0]).__truediv__(v2[0])
b = (v1[1]).__truediv__(v2[1])
listdiv.append(a)
listdiv.append(b)

c = (v1[0]).__mul__(v2[0])
d = (v1[1]).__mul__(v2[1])
listmult.append(c)
listmult.append(d)

print(listdiv)
print(listmult)