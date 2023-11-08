'''Escreva um programa onde o usuário deve responder duas perguntas, 
se é maior de idade e se é casado, depois imprima o resultado.

Exemplo:


Você é maior de idade? (digite 1 se sim, 0 se não): 1
Você é casado(a)? (digite 1 se sim, 0 se não): 0
Você é maior de idade e solteiro.
'''

#EX Q07-01

mIdade = ''
eCasado = ''

while mIdade != 0 and mIdade != 1:
    mIdade = int(input("Você é maior de idade? (digite 1 se sim, 0 se não)"))

while eCasado != 0 and eCasado != 1:
    eCasado = int(input("Você é casado? (digite 1 se sim, 0 se não)"))

if((mIdade == 0) and (eCasado == 0)):
    print("Você é menor de idade e não é casado!")
elif((mIdade == 1) and (eCasado == 0)):
    print("Você é maior de idade e não é casado!")
elif((mIdade == 1) and (eCasado == 1)):
    print("Você é maior de idade e é casado!")
else:
    print("Você é menor de idade e casado!")