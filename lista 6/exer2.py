class Assinatura:
    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass

class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        return 29.99

    def exibir_detalhes(self):
        print("Assinatura Simples: Acesso a filmes e séries em qualidade padrão.")

class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print("Assinatura Premium: Acesso a filmes e séries em qualidade HD e Ultra HD.")

assinatura_simples = AssinaturaSimples()
assinatura_premium = AssinaturaPremium()

assinaturas = [assinatura_simples, assinatura_premium]

for assinatura in assinaturas:
    tipo = "Simples" if isinstance(assinatura, AssinaturaSimples) else "Premium"
    preco = assinatura.calcular_preco()
    detalhes = assinatura.exibir_detalhes()

    print(f"Tipo: {tipo}")
    print(f"Preço: R$ {preco}")
    print("\n")