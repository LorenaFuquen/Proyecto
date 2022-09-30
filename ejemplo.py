print("Hola mundo!")
print(type(9),type("Lorena"),type(5.6),type(True))
print(1>2)
"""Concatenar"""

pal1= "Leidy"
pal2= "Lorena"
pal3= "Fuquen"
pal4= "Calderón"

print(pal1+" "+pal2+" "+pal3+" "+pal4)

"""Convertir en str"""
x=3
print("El valor de la x es:"+ str(x))

"""f-string"""

divi= 22/7

print(f"El resultado de la division es {divi}")

pi= "{:.2f}" .format(divi)

print(f"El valor de pi es {pi}")

"""Listas"""

hostname= ["R1","R2","R3","R4","R5"]
print(hostname)
print(type(hostname),"Numero de valores en la lista",len(hostname))

print(hostname[0])
print(hostname[-1])
hostname[2]="Valor"
print(hostname)

del hostname[3]
print(hostname)

"""Diccionarios"""

ipAdress= {'R1': '10.1.1.1', 'R2': '10.2.2.1', 'R3': '10.3.3.1'}

print("Diccionario ",ipAdress["R1"])

ipAdress=['R6']= 10

print(ipAdress)


print("Hola mundo git")
