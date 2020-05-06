num_max = 100

def num_primos(num_max):
    primos = []
    for i in range(1, num_max):
        cont = 0
        for y in range(1, i+1):
            if i%y == 0:
                cont +=1
        if cont<=2 and i != 1:
            primos.append(i)        
    return primos        
print(num_primos(num_max))  
print(len(num_primos(num_max)))    