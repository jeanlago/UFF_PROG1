salario = float(input())

if salario <= 400:
    percentual = 15
    novo = (15*salario)/100
elif salario <= 800:
    percentual = 12
    novo = (12*salario)/100
elif salario <= 1200:
    percentual = 10
    novo = (10*salario)/100
elif salario <= 2000:
    percentual = 7
    novo = (7*salario)/100
else:
    percentual = 4
    novo = (4*salario)/100

print(f'Novo salario: {salario + novo:.2f}\nReajuste ganho: {novo:.2f}\nEm percentual: {percentual} %')
