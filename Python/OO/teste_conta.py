class Conta:
    def __init__(self, titular, numero, saldo,limite):
        print('Inicializando uma conta')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
        
    def extrato(self):
        print(f'Numero: {self.numero}\saldo: {self.saldo}')
    