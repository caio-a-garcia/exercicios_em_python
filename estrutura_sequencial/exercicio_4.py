entrada = input('Entre quatro notas bimestrais separadas por vírgulas. Ex: "42, 70, 96, 87": ')

lista = entrada.replace(' ','').split(',')

lista_numerica = []

for nota in lista:
  lista_numerica.append(float(nota))

resultado = sum(lista_numerica)/len(lista_numerica)

print(resultado)
