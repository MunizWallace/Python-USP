n = input('Digite um número para checar seus dígitos: ')
tamanho = len(n)
n = int(n)
i = 1
igual = False
while i < tamanho:
    ultimo = (n % 10)
    penultimo = ((n//10) % 10)
    if ultimo == penultimo:
        igual = True
    n = n//10
    i = i+1
if igual == True:
    print('sim')
else:
    print('não')
