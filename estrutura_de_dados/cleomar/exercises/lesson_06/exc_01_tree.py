# -*- coding: utf-8 -*-
class Pessoa:
    
    def __init__(self, name, age, kinship):
        if name != "":
            self.name = name
            self.age = age
            self.kinship = kinship
        else:
            self.name = "Sem nome"
            self.age = age
        self.parents = []

amanda = Pessoa("Amanda Isabely Gigolette da Silva", 3 , "filha")

cleomar = Pessoa("Cleomar Gigolette da Silva", 29 , "pai")
karoline = Pessoa("Karoline Conceição da Silva", 24, "mãe")


iraci = Pessoa("Iraci Gigolette", 53, "avó paterna")
romildo = Pessoa("Romildo da Silva", 63, "Avô paterno")

maria = Pessoa("Maria Catarina da Silva", 91, "bisavó paterna" )
joao = Pessoa("João Silva", 87, "bisavô paterno")

doralina = Pessoa("Doralina Gigolette", 85, "bisavó paterna")
costante = Pessoa("Costante Gigolette", 86, "bisavô paterno")


simone = Pessoa("Simone Drumm", 45, "vó materna")
edison = Pessoa("Edison Conceição da Silva", 53, "vô materno")

dorvalina = Pessoa("Dorvalina Drumm", 64, "bisavó materna")
helio = Pessoa("Hélio Drumm", 68, "bisavô masterno")

gersulina = Pessoa("Gersulina Soares", 85, "bisavó masterna")
otto = Pessoa("Otto Soares", 90, "bisavô masterno")


amanda.parents.append(cleomar)
amanda.parents.append(karoline)

cleomar.parents.append(romildo)
cleomar.parents.append(iraci)
iraci.parents.append(costante)
iraci.parents.append(doralina)
romildo.parents.append(maria)
romildo.parents.append(joao)

karoline.parents.append(simone)
karoline.parents.append(edison)
simone.parents.append(dorvalina)
simone.parents.append(helio)
edison.parents.append(gersulina)
edison.parents.append(otto)

def print_pessoa(pessoa, level):
    print(".." * level  + pessoa.kinship + "    " + pessoa.name + "     " + "Idade: " + str(pessoa.age))
    for parent in pessoa.parents:
        print_pessoa(parent, level + 1)


print_pessoa(amanda, 0)