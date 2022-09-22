import math

print('Programa raizes por Bhaskara')

a = float(input('Digite a '))
b = float(input('Digite b '))
c = float(input('Digite c '))

print('A equação dada é:', a, 'x² +', b, 'x +', c, '= 0')

delta = b**2 - 4*a*c
print('O delta da equação é:', delta)

if delta < 0:
    print('Não há raiz real para a equação informada')
if delta == 0:
    print('Há uma raiz real para a equação informada')
    x = (-b/(2*a))
    print('A raiz da equação é', x)
if delta > 0:
    print('Há duas raizes reais para a equação informada')
    x1 = ((-b+math.sqrt(delta))/(2*a))
    x2 = ((-b-math.sqrt(delta))/(2*a))
    print('As raízes são', x1, 'e', x2)
