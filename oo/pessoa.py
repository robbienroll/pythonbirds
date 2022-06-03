class Pessoa:
    olhos = 2   #atributo default ou de classe

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
    rob.sobrenome = 'Marini'    # atributo dinamico
    del rob.filhos
    rob.olhos = 1
    del rob.olhos
    print(rob.__dict__)     # nao printa atributos de classe
    print(ian.__dict__)     # nao printa atributos de classe
    Pessoa.olhos  =3
    print(Pessoa.olhos)
    print(rob.olhos)
    print(ian.olhos)
    print(id(Pessoa.olhos), id(rob.olhos), id(ian.olhos))