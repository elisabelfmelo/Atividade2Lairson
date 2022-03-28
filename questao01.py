n = 1
n1 = 0
n2 = 0
n3 = 0
n4 = 0
while n > 0:
 n = int(input("Digite um número:"))
if n >= 0 and n <= 25: 
 n1 = n1 + 1
elif n >= 26 and n <= 50:
 n2 = n2 + 1
elif n >= 51 and n <= 75:
 n3 = n3 + 1
elif n >= 76 and n <= 100:
 n4 = n4 + 1
print("A quantidade de números entre 0 e 25 é: ", n1, ",  entre 26,50 é: ", n2, ", entre  51,75 é: ", n3, ", e entre 76,100 é: ",n4)