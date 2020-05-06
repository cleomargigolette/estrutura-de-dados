from random import randint

def generate_list_of_ints(length, max_number):
    lista_int = []
    while True:
        if len(lista_int) < length:
            num =(randint(0,max_number))
            lista_int.append(num)
        else:
            break
    return lista_int    

if __name__ == '__main__':
    print(len(generate_list_of_ints(10, 100)))
    print((generate_list_of_ints(10, 100)))
