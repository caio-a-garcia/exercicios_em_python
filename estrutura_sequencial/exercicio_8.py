valor_por_h = float(input('Quanto voc� ganha por hora?'))

horas_trabalhadas = float(input('Quantas horas voc� trabalhou no �ltimo m�s?'))

total_ganho = valor_por_h * horas_trabalhadas

print('M�s passado voc� ganhou R${:.2f}.'.format(total_ganho))
