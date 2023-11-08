''' Q 20-01
Considere o código a seguir:

def calc_digit(n):
    def final(digit):
        return digit**n
    return final
num_list = []
for num in range(1, 6):
    num_list.append(calc_digit(num))
    prtin(num_list[num - 1](num))

1
4
27
256
3125
Calcule o resultado do código manualmente.
'''
def calc_digit(n):
    def final(digit):
        return digit**n
    return final
num_list = []
for num in range(1, 6):
    num_list.append(calc_digit(num))
    print(num_list[num - 1](num))

#Saída:
# 1
# 4
# 27
# 256
# 3125