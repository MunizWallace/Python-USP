n = int(input('Digite um número inteiro para calcular o fatorial: '))
produto = 1
i = 0
while i != n:
    produto = produto*(n-i)
    i = i+1
print(produto)
