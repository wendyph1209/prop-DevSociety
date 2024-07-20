"""Tipos de operadores de Python
Operadores aritméticos
Operadores relacionales
Operadores Bit a Bit
Operadores de asignación
Operadores lógicos
Operadores de pertenencia
Operadores de identidad"""
numero1 = int(input("INGRESA UN NUMERO: "))
numero2 = int(input("INGRESA OTRO NUMERO: "))


#OPERADORES ARITMETICOS
print("")
print("OPERADORES DE ARITMETICOS")

print("Suma ", numero1," + ", numero2, " = ", numero1 + numero2)
print("Resta ", numero1," - ", numero2, " = ", numero1-numero2)
print("Multiplicación ", numero1," * ", numero2, " = ", numero1*numero2)
print("Division ", numero1," / ", numero2, " = ", numero1/numero2)
print("modulo ", numero1," % ", numero2, " = ", numero1%numero2)
print("Potencia de ", numero1," ** ", numero2, " = ", numero1**numero2)
print("Resultado entero de ", numero1," // ", numero2, " = ", numero1//numero2)

#OPERADORES COMPARACIÓN Ó RELACIONALES
print("")
print("OPERADORES DE COMPARACIÓN Ó RELACIONALES ")

print(" ", numero1," es igual a ", numero2, " = ", numero1 == numero2)
print(" ", numero1," es diferente a ", numero2, " = ", numero1 != numero2)
print(" ", numero1," es menor a ", numero2, " = ", numero1 < numero2)
print(" ", numero1," es mayor a ", numero2, " = ", numero1 > numero2)
print(" ", numero1," es menor o igual a ", numero2, " = ", numero1 <= numero2)
print(" ", numero1," es mayor o igual a ", numero2, " = ", numero1 >= numero2)

#OPERADORES DE ASIGNACION
print("")
print("OPERADORES DE ASIGNACIÓN")

X = numero1
print("X = ", X)
X = numero1
X += numero2
print("X += ", numero2, "=", X)
X = numero1
X -= numero2
print("X -= ",numero2, "=", X)
X = numero1
X /= numero2
print("X /= ", numero2, "=", X)
X = numero1
X %= numero2
print("X %= ", numero2, "=", X)
X = numero1
X //= numero2
print("X //= ",numero2, "=", X)
X = numero1
X **= numero2
print("X **= ", numero2, "=", X)
X = numero1
X &= numero2
print("X &= ", numero2, "=", X)
X = numero1
X |= numero2
print("X |= ", numero2, "=", X)
X = numero1
X ^= numero2
print("X ^= ", numero2, "=", X)
X = numero1
X >>= numero2
print("X >>= ", numero2, "=", X)
X = numero1
X <<= numero2
print("X <<= ", numero2, "=", X)

#OPERADORES LÓGICOS
print("")
print("OPERADORES LÓGICOS")

print("True and True = ", True and True)
print("True and False = ", True and False)
print("False and True = ", False and True)
print("False and False = ", False and False)

#OPERADORES BITWISE
print("")
print("OPERADORES BITWISE / BINARIOS")


print("", numero1," = ", bin(numero1))
print("", numero2," = ", bin(numero2))
print("")
print("", numero1," & ", numero2, " = ", bin(numero1 & numero2))
print("", numero1," | ", numero2, " = ", bin(numero1 | numero2))
print("", numero1," ~ = ", bin( ~ numero1))
print("", numero1," ^ ", numero2, " = ", bin(numero1 ^ numero2))
print("", numero1," >> 2 = ", bin( numero1 >> 2))
print("", numero1," << 3 = ", bin( numero1 << 3))

#OPERADORES BITWISE
print("")
print("OPERADORES DE IDENTIDAD")

print("", numero1," is ", numero1, " = ", numero1 is numero1)
print("", numero1," is ", numero2, " = ", numero1 is numero2)
print("", numero1," is not", numero1, " = ", numero1 is not numero1)
print("", numero1," is not", numero2, " = ", numero1 is not numero2)

#OPERADORES MEMBRESIA
print("")
print("OPERADORES DE MEMBRESIA")

nombre = input("INGRESA TU NOMBRE: ")
letra = input("INGRESA UNA LETRA A BUSCAR: ")
print("", letra, " se encuentra en ", nombre, " = ", letra in nombre )
print("", letra, " no se encuentra en ", nombre, " = ", letra not in nombre )

print("")
print("OPERADOR DE WALRUS")
print(nombre2 := input("ASIGNA Y DEVUELVE (:=) UN NOMBRE: "))

