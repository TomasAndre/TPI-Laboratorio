import random
numero= random.randint(10,22)
intentosrealizados= 3
print("**************************************")
print("Bienvenido a adivina la edad que tengo")
print("**************************************")
print("")
print("***************************************************************")
print("Te doy una pista, mi edad esta entre 10 y 22. Tenes 3 intentos!")
print("***************************************************************")

while intentosrealizados != 0:
    respuesta=int(input("Intenta adivinar,¿Cuantos años tengo?: "))
    intentosrealizados= intentosrealizados-1
    if respuesta==numero: 
        print("||||||||||||||||||||||||||||||||||||||||||")
        print("|Felicidades tu respuesta es la correcta!|")
        print("||||||||||||||||||||||||||||||||||||||||||")
        break

    if intentosrealizados==0:
        print("|||||||||||||||||||||||||||||||||||||")
        print("|Perdiste, mi edad era de ",numero," años!|")
        print("|||||||||||||||||||||||||||||||||||||") 
        break
    if respuesta<numero:
        print("Tu repuesta es muy baja")
        print("Intentos: ",intentosrealizados)
    else:
        print("Tu respuesta es muy alta")
        print("Intentos:",intentosrealizados)
    

 