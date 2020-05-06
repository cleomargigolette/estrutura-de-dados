from app import lib


stack = lib.stack
ultimo = None
for item in range(1,11):  
    stack.push(item)

for teste in range(len(stack.list)):
    print(stack.list[teste])
print("======================================================")

for item in range(3):
    stack.pop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

for teste in range(len(stack.list)):
    print(stack.list[teste])
print("======================================================")

for item in range(1,6):                                                                                                                                                             
    stack.push(item)                                                                                                                                                                                                                                                                                                                                                        

for teste in range(len(stack.list)):                                                                                                                                                                                                                                                                                        
    print(stack.list[teste])
print("======================================================")

for item in range(8):
    ultimo = stack.pop()

for teste in range(len(stack.list)):
    print(stack.list[teste])
print("======================================================")

print("O número secreto é " + str(ultimo))                                                                                                                                                                                                                                                                                                                                                                                        