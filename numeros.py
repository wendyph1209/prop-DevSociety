print("NUMEROS DE 10 AL 10 pares y que no son multiplos de 3 \n")

for i in range (10,101):
    if (i % 2 == 0 and i % 3 == 1):
        print(i)

print("NUMEROS DE 10 AL 10 que no son multiplos de 3 \n")
for i in range (10,101):
    if (i % 3 == 1):
        print(i)