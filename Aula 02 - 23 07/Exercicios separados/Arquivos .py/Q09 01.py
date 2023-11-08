'''Um número Armstrong é um número inteiro de três dígitos que é igual à soma dos cubos de cada dígito. 
Encontre todos os números Armstrong entre números inteiros de três dígitos e imprima-os.

Exemplo: 

153 é um número Armstrong, pois 1³+5³+3³ = 1+125+27 = 153'''

#EX Q09-01

num = 100
j = 0
fim = []

while num < 1000:
    x = [int(a) for a in str(num)] #Separa os números e cria um array com eles

    for i in x:
        i = i**3
        j = j + i
    
    if (j == num):
            fim.append(j)
    
    num = num + 1
    x.clear()
    j = 0

print("Os números de Armstrog são: ", fim)