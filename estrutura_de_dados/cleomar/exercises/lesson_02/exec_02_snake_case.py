frase = input("Digite uma frase CammelCase:")

def change_case(frase): 
    res = [str[0].lower()] 
    for c in str[1:]: 
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            res.append('_') 
            res.append(c.lower()) 
        else: 
            res.append(c) 
      
    return ''.join(res) 
      
str = "CammelCase"
print(change_case(frase)) 