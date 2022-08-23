class Estatica():
    def __init__(self):
        self.vetor = [None, None, None, None, None]
        self.size = 0

    def size(self):
        return self.size

    def getPrim(self):
        return self.vetor[0]

    def getUlt(self):
        return self.vetor[self.size-1]

    def Vazia(self):
        return self.size == 0

    def Cheia(self):
        return self.size == 5

    def imprimir(self):
        for i in range(self.size):
            print(self.vetor[i], end=' ')
        print()

    def inserirFim(self, valor):
        self.vetor[self.size] = valor
        self.size += 1
        

    def inserirInicio(self, valor):
       for i in range(self.size, 0, -1):
            self.vetor[i] = self.vetor[i-1]
            self.vetor[0] = valor
            self.size += 1

    def removerFim(self):
        self.size -= 1

    def removerInicio(self):
        for i in range(1, self.size):
            self.vetor[i-1] = self.vetor[i]
        self.size -= 1

    def removerPosicao(self, posicao):
        for i in range(posicao, self.size - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.vetor[self.size - 1] = None
        self.size -= 1

    def removerElemento(self, valor):
        index = self.consultarElemento(valor)
        if not (index is None):
            self.removerPosicao(index)

    def consultarElemento(self, valor):
        for i in range(self.size):
            if self.vetor[i] == valor:
                return i


    def contarQtdOcorrencias(self, valor):
        sizeElementos = 0
        for i in range(self.size):
            if self.vetor[i] == valor:
                sizeElementos += 1
        return sizeElementos

    def somaElementos(self):
        soma = 0
        for i in range(self.size):
            soma += self.vetor[i]
        return soma

    def substituirTodasOcorrencias(self, valor, novovalor):
        for i in range(self.size):
            if self.vetor[i] == valor:
                self.vetor[i] = novovalor
