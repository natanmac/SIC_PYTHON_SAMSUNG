'''Q14-01 -> Natan Macedo
Há uma variável do dicionário maria como segue. Nesta variável de dicionário, cursos como 'coreano' e 'inglês' e suas pontuações são armazenados como key:value. Imprima a nota média de 89,25 para as notas de Maria.
Dica: Use as funções de valores() e len() do dicionário 


maria = {'coreano': 94, 'ingles': 91, 'matematica': 89, 'ciencia': 83}'''

maria = {'coreano': 94, 'ingles': 91, 'matematica': 89, 'ciencia': 83}
notas = []
qtdNotas = 0

for i in maria.values():
    notas.append(i)
    qtdNotas += 1

media = sum(notas)/qtdNotas

print("A média da Maria é de: ", media)