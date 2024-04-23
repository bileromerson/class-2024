
class Casa():
    #método inicializador da classe
    def __init__(self, rua, numero, cep, telefone):
        self.rua = rua
        self.numero = numero
        self.cep = cep
        self.telefone = telefone
    #métodos da classe
    def enderecoCompleto(self):
        return f"Rua: {self.rua}, Nº{self.numero} - CEP: {self.cep} / {self.telefone}"
    
casa1 = Casa(rua="Filipe", numero="77", cep="954872", telefone="(31) 92433-5678")

print(casa1.enderecoCompleto())