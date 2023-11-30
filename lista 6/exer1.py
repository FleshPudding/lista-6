class UnidadeMilitar:
    def mover(self):
        pass

    def atacar(self):
        pass

class Soldado(UnidadeMilitar):
    def mover(self):
        print("Soldado: Marchando para a frente!")

    def atacar(self):
        print("Soldado: Atacando com a espada!")

class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("Arqueiro: Avançando para uma posição estratégica!")

    def atacar(self):
        print("Arqueiro: Disparando flechas!")

class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("Cavaleiro: Galopando para o campo de batalha!")

    def atacar(self):
        print("Cavaleiro: Golpeando com a lança!")

soldado1 = Soldado()
arqueiro1 = Arqueiro()
cavaleiro1 = Cavaleiro()

unidades = [soldado1, arqueiro1, cavaleiro1]

for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print("\n")