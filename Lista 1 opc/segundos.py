segundos = input('Por favor, entre com o número de segundos que deseja converter: ')
segundos = int(segundos)
dias = segundos//86400
restsegundos = segundos % 86400
horas = restsegundos//3600
restsegundos = restsegundos % 3600
minutos = restsegundos//60
restsegundos = restsegundos % 60
print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', restsegundos, 'segundos')
