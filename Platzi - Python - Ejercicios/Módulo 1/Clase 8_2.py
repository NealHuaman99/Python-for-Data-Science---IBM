a = [1,2,3,4,5]
b = a
#Acá se establece el mismo lugar de memoria
#Para las listas a y b
print(a)
print(b)
del a [0]
print(a)
print(b)
#Se elimina el elemento de ambas listas, pero
#Mi objetivo es eliminar un elemento solo de la lista a
print(id(a))
print(id(b))
c = a[:]
#Acá se establecen lugares diferentes de memorias
#Para las listas c y a
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(a)
print(b)
print(c)
#Acá se puede apreciar que se añade el elemento
#En la lista a y b, pero no en c, porque no están
#En la misma memoria