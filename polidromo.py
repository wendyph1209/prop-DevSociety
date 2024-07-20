print("PALABRAS POLIDROMAS")
palabra = input("Ingresa la palabra: ").lower()
if palabra==palabra[::-1]:
  print('Es un Palíndromo')
else:
  print('No es un Palíndromo')