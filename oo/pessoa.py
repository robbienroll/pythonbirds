class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 43):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hi {id(self)}'

if __name__ == '__main__':
    ian = Pessoa(nome ='Ian')
    rob = Pessoa(ian, nome = 'Robson')
    print(Pessoa.cumprimentar(ian))
    print(id(ian))
    print(ian.cumprimentar())
    print(ian.nome)
    print(ian.idade)
    for filho in rob.filhos:
        print(filho.nome)