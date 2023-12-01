class Casa:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, comodo):
        self.comodos.append(comodo)

class Fechadura:
    def __init__(self, tipo, chave_correta):
        self.tipo = tipo
        self.chave_correta = chave_correta

    def abrir(self, chave_ou_senha):
        return chave_ou_senha == self.chave_correta


class Porta:
    def __init__(self, fechadura):
        self.fechadura = fechadura
        self.comodo = None

    def associar_comodo(self, comodo):
        self.comodo = comodo

    def abrir(self, chave_ou_senha):
        if self.fechadura.abrir(chave_ou_senha):
            return f"Porta aberta para {self.comodo.nome}"
        else:
            return "Falha ao abrir a porta"


class Comodo:
    def __init__(self, nome, cor, interruptor, ar_condicionado, tipo_fechadura, chave_ou_senha):
        self.nome = nome
        self.cor = cor
        self.interruptor = interruptor
        self.ar_condicionado = ar_condicionado
        self.porta = Porta(Fechadura(tipo_fechadura, chave_ou_senha))
        self.porta.associar_comodo(self)

    def __str__(self):
        return f"{self.nome} - Cor: {self.cor}, Interruptor: {self.interruptor}, Porta: {self.porta.fechadura.tipo}, Ar-condicionado: {self.ar_condicionado}"


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def acionar_interruptor(self, comodo):
        return f"{self.nome} acionou o interruptor no(a) {comodo.nome}"

    def acionar_ar_condicionado(self, comodo):
        return f"{self.nome} acionou o ar-condicionado no(a) {comodo.nome}"

    def abrir_porta(self, comodo, chave_ou_senha):
        return f"{self.nome} {comodo.porta.abrir(chave_ou_senha)}"


# Cenário de teste
cozinha = Comodo("Cozinha", "Branco", True, True, "Simples", "chave_cozinha")
sala = Comodo("Sala", "Bege", True, False, "Inteligente", "senha_sala")

pessoa1 = Pessoa("Ana")

print(pessoa1.acionar_interruptor(cozinha))
print(pessoa1.acionar_ar_condicionado(cozinha))
print(pessoa1.abrir_porta(cozinha, "chave_cozinha"))

pessoa2 = Pessoa("João")

print(pessoa2.acionar_interruptor(sala))
print(pessoa2.abrir_porta(sala, "senha_sala"))
