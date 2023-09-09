class Animal:
    def __init__(self, nome):
        self.nome = nome

    def Onomatopeia(self):
        pass
        #print(f"O {self.nome} está ")


class Cachorro(Animal):
    def Onomatopeia(self):
        return f"O {self.nome} faz 'Au Au!'"


class Gato(Animal):
    def Onomatopeia(self):
        return f"O {self.nome} faz 'Miau!'"


cachorro = Cachorro("Cachorro")
gato = Gato("Gato")


print(cachorro.Onomatopeia())
print(gato.Onomatopeia())
