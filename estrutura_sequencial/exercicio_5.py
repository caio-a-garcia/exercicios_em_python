metros = input('Digite valor em metros que eu converto para cent�metros: ')

metros_limpo = metros.replace(',','.').replace('m','')

centimetros = str(float(metros_limpo) * 100)

print(metros_limpo + 'm = ' + centimetros + 'cm')
