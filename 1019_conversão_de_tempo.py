
segundos = int(input())

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = segundos % 60

print(f'{horas:01}:{minutos:01}:{segundos:01}')
