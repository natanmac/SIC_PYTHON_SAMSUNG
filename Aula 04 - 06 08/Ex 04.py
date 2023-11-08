'''Q16-01 -> Natan Macedo
Há uma pontuação tupla como se segue. Esta tupla contém informações sobre quatro alunos. Nesta informação, o nome do aluno e as notas em inglês, matemática e ciências formam um tuple. Por exemplo, 'Davi' tem uma nota de 88 em inglês, 95 em matemática e 90 em ciências.

notas = (('Davi',  88,  95, 90), ('Felipe', 83, 98, 81), ('Luciano', 81, 97, 98), ('Rodrigo', 82, 89, 83))
Extrair somente as notas matemáticas, usando a função zip na tupla da nota. Escreva um código que calcula a média das pontuações de matemáticas extraídas.
'''

notas = (('Davi',  88,  95, 90), ('Felipe', 83, 98, 81), ('Luciano', 81, 97, 98), ('Rodrigo', 82, 89, 83))

Davi = notas[0]
Felipe = notas[1]
Luciano = notas[2]
Rodrigo = notas[3]

x = list(zip(Davi, Felipe, Luciano, Rodrigo))

media = sum(x[2])/4

print(media)