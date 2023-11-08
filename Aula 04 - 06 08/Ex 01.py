'''Q13-01 -> Natan Macedo
A matriz bidimensional a contém os valores [[1, 2], [3, 4], [5, 6]]. Mude esta matriz bidimensional para uma matriz unidimensional como [1, 2, 3, 4, 5, 6], e imprima-a.
Dica: Use um for loop. Defina uma nova matriz e coloque os elementos de uma nessa matriz.'''

matriz1 = [[1, 2], [3, 4], [5, 6]]
matriz2 = []

for i in matriz1:
    for n in i:
        matriz2.append(n)

print("A matriz inicial é: ", matriz1)
print("A matriz atualizada fica: ", matriz2)