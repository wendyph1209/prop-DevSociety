
from datetime import datetime
print("CUÁNTOS DIAS FALTAN PARA NAVIDAD Y DÍA DE MUERTOS?????")

navidad = datetime(2024, 12, 25)
muertos = datetime(2024, 11, 2)

fechaIntr = input("INGRESA FECHA (aaaa, mm, dd): ")
fecha = datetime.strptime(fechaIntr, '%Y/%m/%d')


print ("FALTAN ", str((navidad - fecha).days), " DIAS PARA NAVIDAD Y \n ",str((muertos - fecha).days), " DIAS PARA MUERTOS" )

