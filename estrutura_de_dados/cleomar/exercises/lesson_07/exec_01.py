import plate_generator

class Vehicle:
    
    wheels = 4
    plate = plate_generator.pg.new_plate()


class Motorcycle(Vehicle):
    
    displacement = "250cc"
    brand = "Honda"

    def __init__(self, displacement, brand):
        self.wheels = 2
        if displacement != None:
            self.displacement = displacement
        if brand != None:
            self.brand = brand

class Truck(Vehicle):
    brand = "Volvo"
    category = "Pesado"             

    def __init__(self, brand, category):
        if brand != None:
            self.brand = brand
        if category != None:
            self.category = category    

class Car(Vehicle):
    brand = "Chevrolet"
    model = "Camaro"             

    def __init__(self, brand, model):
        if brand != None:
            self.brand = brand
        if model != None:
            self.model = model   

print("-"* 105)

moto = Motorcycle("150cc", None)
print("MOTO:")
print("Cilindradas: " + str(moto.displacement))
print("Número de rodas: " + str(moto.wheels))
print("Placa: " + str(moto.plate))
print("Marca: " + str(moto.brand))

print("-"* 105)
caminhao = Truck(None, None)
print("CAMINHÃO:")
print("Marca: " + str(caminhao.brand))
print("Número de rodas: " + str(caminhao.wheels))
print("Placa: " + str(caminhao.plate))
print("Categoria: " + str(caminhao.category))

print("-"* 105)
carro = Car(None, None)
print("CARRO:")
print("Marca: " + str(carro.brand))
print("Número de rodas: " + str(carro.wheels))
print("Placa: " + str(carro.plate))
print("Marca: " + str(carro.model))