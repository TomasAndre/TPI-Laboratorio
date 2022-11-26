import random

num1 = random.randint(1,9) #NUMERO AL AZAR ENTRE 0 Y 100
num2 = random.randint(1,9) #NUMERO AL AZAR ENTRE 0 Y 100

resultado = num1*num2       #MULTIPLICACION LOS DOS NUMEROS ALEATORIOS
vida = 3 

while vida != 0:
  print("¿Cuanto es:",num1,"x",num2,"?")
  respuesta = int(input("RESULTADO: "))
  if resultado!=respuesta: 
    print("El numero es incorrecto, te quedan ",vida-1," intentos")
    vida=vida-1
  else:
    print("****************") 
    print("    CORRECTO!!  ")
    print("****************") 
    print("El resultado de ",num1, "x",num2, "es:",resultado)
    break