#Escreva um programa que leia 2 entradas do usuário e as imprima do menor para o maior.

'''(Restrição: dois números inteiros não são o mesmo número)

Exemplo:


Insira dois números inteiros: 14 10
Os números inseridos em ordem crescente são: 10 14''' 

#EX Q06-01

num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

if(num1<num2):
    print("Os números inseridos em ordem crescente são: ", num1, " e ", num2)
else:
    print("Os números inseridos em ordem crescente são: ", num2, " e ", num1)