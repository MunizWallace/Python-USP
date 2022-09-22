n = input('Digite um número para checar seus dígitos: ')
tamanho = len(n)
n = int(n)
igual = False
i = 1
while i < tamanho:
    ultimo = n % 10
    n = n//10
    if ultimo == (n % 10):
        igual = True
    i = i+1
if igual == True:
    print('sim')
else:
    print('não')
