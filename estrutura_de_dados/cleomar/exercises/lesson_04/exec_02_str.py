frase = input("Digite sua frase:")

def modificacao_recursica(frase, indice):
    if indice >= len(frase):
        return
        
    frase_modificada = list(frase)
    frase_modificada[indice] = "*"
    print("".join(frase_modificada))
    modificacao_recursica(frase, indice + 1)


modificacao_recursica(frase, 0)