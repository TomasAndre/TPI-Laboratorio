def juego1():
    #PIEDRA, PAPEL O TIJERA
    import random                   
    vida_usuario=3
    vida_pc=3
    while vida_usuario!=0 or vida_pc!=0:    #ciclo while para llevar el contador de vida

        aleatorio = random.randrange(0, 3)   #NUMERO ALEATORIO DE 0 A 3
        pc = ""
        print("1) Piedra")
        print("2) Papel")
        print("3) Tijera")
        opcion = int(input("Que elijes: "))       # respuesta del usuario

        if opcion == 1:
            usuario = "piedra"
        elif opcion == 2:
            usuario = "papel"
        elif opcion == 3:
            usuario = "tijera"
        print("Tu elijes: ",usuario)

        if aleatorio == 0:          # respuesta aleatoria de la pc
            pc = "piedra"
        elif aleatorio == 1:
            pc = "papel"
        elif aleatorio == 2:
            pc = "tijera"
        print("PC elijio: ",pc)
        
        if pc == "piedra" and usuario == "papel":
            print("GANASTE, papel envulve piedra")
            vida_pc=vida_pc-1
        elif pc == "papel" and usuario == "tijera":
            print("GANASTE, Tijera corta papel")
            vida_pc=vida_pc-1
        elif pc == "tijera" and usuario == "piedra":
            print("GANASTE, Piedra pisa tijera")
            vida_pc=vida_pc-1
        if pc == "papel" and usuario == "piedra":
            print("PERDISTE, papel envulve piedra")
            vida_usuario=vida_usuario-1
        elif pc == "tijera" and usuario == "papel":
            print("PERDISTE, tijera corta papel")
            vida_usuario=vida_usuario-1
        elif pc == "piedra" and usuario == "tijera":
            print("PERDISTE, piedra pisa tijera")
            vida_usuario=vida_usuario+1
        elif pc == usuario:
            print("EMPATE")
        print("-------------")
        if vida_usuario==0 or vida_pc==0:
            if vida_usuario==0:
                print("JUEGO TERMINADO!!")
                print("GANA PC")
                print("VIDAS USUARIO: ",vida_usuario)
                print("VIDA PC= ",vida_pc)
                break
            if vida_pc==0:
                print("JUEGO TERMINADO!!")
                print("GANASTE")
                print("VIDAS USUARIO: ",vida_usuario)
                print("VIDA PC= ",vida_pc)
                break


def juego2():
    #ADIVINA EL NUMERO
    import random
    numero=random.randint(1,9)  # ELIJE UN NUMERO AL AZAR: 1,2,3,4,5,6,7,8,9
    i=5 
    print("ESCRIBE EL NUMERO A ADIVINAR, OJO TENES 5 VIDAS")
    print("PISTA: EL NUMERO ESTA ENTRE 1 Y 9") 
    numero_adivinar=45
    while i>0 and numero!=numero_adivinar: 
        i=i-1                              	 
        print("")
        numero_adivinar = int(input("Numero: "))
        if i==0:                                      #SI EL CONTADOR ES IGUAL A 5 IMPRIME QUE SE TERMINARON LAS VIDAS
            print("*SE TERMINARON LAS VIDAS*")
        else:
            if numero==numero_adivinar:
                print("***************")
                print("NUMERO CORRECTO")
                print("***************")
                break
            else: 
                print("NUMERO INCORRECTO!!!")
                print("TE QUEDAN ",i,(" VIDAS!"))
                

def juego3():
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
    

 
def juego4():
    #MULTIPLICAR
    import random

    num1 = random.randint(1,9) #NUMERO AL AZAR ENTRE 1 Y 9
    num2 = random.randint(1,9) #NUMERO AL AZAR ENTRE 1 Y 9

    resultado = num1*num2       #MULTIPLICACION LOS DOS NUMEROS ALEATORIOS
    vida = 3 

    while vida != 0:
        print("¿Cuanto es:",num1,"x",num2,"?")
        respuesta = int(input("RESULTADO: "))

        if resultado!=respuesta: 
            print("El numero es incorrecto, te quedan ",vida-1," intentos")
            vida=vida-1
        else:
            print("|||||||||||||||||") 
            print("||||CORRECTO!!|||")
            print("|||||||||||||||||") 
            print("El resultado de ",num1, "x",num2, "es:",resultado)
            break


lista_juegos=["PIEDRA PAPEL O TIJERA","ADIVINA EL NUMERO","ADIVINA LA EDAD","MULTIPLICAR","GRACIAS POR JUGAR!"]
menu=0
while menu!=5:
    print("***MENU DE JUEGOS***")
    print("1- PIEDRA PAPEL O TIJERA")
    print("2- ADIVINA EL NUMERO")
    print("3- ADIVINA LA EDAD")
    print("4- MULTIPLICAR")
    print("5- SALIR")
    menu = int(input("Escribe que juego quiere jugar: "))
    if menu == 1:
        print("")
        print("BIENVENIDO A ",lista_juegos[0]) 
        print(juego1())
    if menu == 2:
        print("")
        print("BIENVENIDO A ",lista_juegos[1])
        print(juego2())
    if menu == 3:
        print("")
        print("BIENVENIDO A ",lista_juegos[2])
        print(juego3())
    if menu == 4:
        print("")
        print("BIENVENIDO A ",lista_juegos[3])
        print(juego4())
print("||||||||||||||||||")        
print(lista_juegos[4]) 
print("||||||||||||||||||")    