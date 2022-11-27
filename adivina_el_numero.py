import random

numero=random.randint(1,9)  # ELIJE UN NUMERO AL AZAR: 1,2,3,4,5,6,7,8,9
i=5
print("ESCRIBE EL NUMERO A ADIVINAR, OJO TENES 5 VIDAS")
print("PISTA: EL NUMERO ESTA ENTRE 1 Y 9") 
numero_adivinar=45
while i>0 and numero!=numero_adivinar: 			# SE INICIA EL CONTADOR I EN 0, Y SI LLEGA A 5 Y EL NUMERO QUE INGRESA NO ES IGUAL AL 
    i=i-1                              	 # NUMERO RANDOM VUELVE AL MENU
    print("")
    numero_adivinar = int(input("Numero: "))
    if i==0:                                            #SI EL CONTADOR ES IGUAL A 5 IMPRIME QUE SE TERMINARON LAS VIDAS
        print("*SE TERMINARON LAS VIDAS*")
    else:
        if numero==numero_adivinar:
            print("NUMERO CORRECTO!!")
            break
        else: 
            print("NUMERO INCORRECTO!!!")
            print("TE QUEDAN ",i,(" VIDAS!"))
            