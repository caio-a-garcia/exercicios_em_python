valor_por_h = float(input('Quanto você ganha por hora?'))

horas_trabalhadas = float(input('Quantas horas você trabalhou no último mês?'))

total_ganho = valor_por_h * horas_trabalhadas

print('Mês passado você ganhou R${:.2f}.'.format(total_ganho))
