class Pessoa:
    def __init__(self, nome = None, idade = 43):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Hi {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Steve Harris')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'RobMarini'
    print(p.nome)
    print(p.idade)