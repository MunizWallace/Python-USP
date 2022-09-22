n = input('Digite um número para somar seus dígitos: ')
tamanho = len(n)
n = int(n)
soma = 0
i = 0
while i < tamanho:
    soma = soma+n % 10
    n = n//10
    i = i+1
print(soma)
