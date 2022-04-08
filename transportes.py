from random import uniform

class MeioDeTransporte():
    def __init__(self, dominio, passageiros):
        self.dominio = dominio
        self.passageiros = passageiros

#    def receber_passageiros(num):


class Terrestre(MeioDeTransporte):
    def __init__(self, passageiros, eixos):
        super().__init__('terrestre', passageiros)
        self.eixos = eixos

    def pagar_pedagio(self):
        print(f"O valor do pedagio eh R${int(self.eixos) * 1.42}")


class Aquatico(MeioDeTransporte):
    def __init__(self,  passageiros, motores, velas):
        super().__init__('aquatico', passageiros)
        self.motores = motores
        self.velas = velas


class Aereo(MeioDeTransporte):
    def __init__(self, passageiros, propulcao):
        super().__init__('aereo', passageiros)
        self.propulcao = propulcao

    def falta_muito(self):
        if self.propulcao == 'turbina':
            print('Ja ja estamos chegando')
        elif self.propulcao == 'helice':
            print('Ainda vai demorar')
        else:
            print('O capitao respondera todas as suas perguntas quando ele chegar')


class Carro(Terrestre):
    def __init__(self, passageiros):
        super().__init__(passageiros, 2)

    def busina(self):
        print('Calma e respira. O sinal ja vai abrir')


class Caminhao(Terrestre):
    def __init__(self, passageiros, eixos):
        super().__init__(passageiros, eixos)

    def carga_total(self):
        carga = int(self.eixos)
        return carga

    
class Remo(Aquatico):
    def __init__(self, passageiros):
        super().__init__(passageiros, 0, 0)


class Barco(Aquatico):
    def __init__(self, passageiros, motores, velas):
        super().__init__(passageiros, motores, velas)

    def olhar_pro_ceu(self):
        if int(self.velas) >= 1:
            print('Que ceu lindo!')
        else:
            print('...')


class Aviao(Aereo):
    def __init__(self, passageiros, propulcao, autonomia):
        super().__init__(passageiros, propulcao)
        self.autonomia = autonomia

    def procurando_praia(self):
        if int(self.autonomia) >= 598:
            print('Bora pra praia')
        else:
            print('Bora pro Praia')


class Helicoptero(Aereo):
    def __init__(self, passageiros):
        super().__init__(passageiros, 'helice')

    def chance_de_sobrevivencia(self):
        chance = str(uniform(0, 1)) + '%'
        print(f'A chance de sobrevivencia eh {chance}. Nao ha nada com que se preocupar.')
