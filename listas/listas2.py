import random
lista = []

lista.append(56)
print(lista)
numero = int(input("ingresa un numero: "))
lista.append(numero)
print(lista)

#ingresar 10 numeros aleatorios
for i in range (10):
     aleat = random.randint(0,100)
     lista.append(aleat)
print(lista)