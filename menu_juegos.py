lista_juegos=["PIEDRA PAPEL O TIJERA","ADIVINA EL NUMERO","juego pablo","MULTIPLICAR","GRACIAS POR JUGAR!"]
menu=0
while menu!=5:
    print("JUEGOS")
    print("1- PIEDRA PAPEL O TIJERA")
    print("2- ADIVINA EL NUMERO")
    print("3-")
    print("4- MULTIPLICAR")
    print("5- SALIR")
    menu = int(input("Escribe que juego quiere jugar: "))
    if menu == 1:
        print("BIENVENIDO A ",lista_juegos[0]) 
    if menu == 2:
        print("BIENVENIDO A ",lista_juegos[1])
    if menu == 3:
        print("BIENVENIDO A ",lista_juegos[2])
    if menu == 4:
        print("BIENVENIDO A ",lista_juegos[3])
print(lista_juegos[4]) 