#OPERACIONES CON ESTRUCTURAS DE CONTROL

#CONDICIONALES
#USO DE IF
print()
print("USO DE IF")
edad1 = input("INRESA TU EDAD: ")
edad2 = input("INRESA OTRA EDAD: ")

if edad1 == edad2:
    print("OH! TIENEN LA MISMA EDAD")

#USO DE ELSE
print()
print("USO DE ELSE")
if edad1 == edad2:
    print("TIENEN LA MISMA EDAD")
else:
    print("NO LA MISMA EDAD")

#USO DE ELIF
print()
print("USO DE ELIF")
if edad1 == edad2:
    print("TIENEN LA MISMA EDAD")
elif edad1 > edad2:
    print("Eres mayor")
else:
    print("Eres menor")

#OPERADOR TERNARIO
print()
print("OPERADOR TERNARIO")
print("SU EDAD ES IGUAL" if edad1 == edad2 else "NO TIENEN LA MISMA EDAD")


num = int(input("QUE TABLA QUIERES IMPRIMIR: "))

for i in range (1, 11):
    multiplicacion = num * i
    print("", num, " * ", i, " = ", multiplicacion)

#USO DE WHILE
print()
print("USO DE WHILE")

num = 5
print("NUMEROS MENORES A: ", num)
while num > 0:
    num -=1
    print(num)

#EXCEPCIONES
print()
print("USO DE EXCEPCIONES")

try:
    numPensado = int(input("PIENSA EN UN NUMERO: "))
    print("SI ES UN NUMERO")
except Exception:
    print("NO ES UN NUMERO")

