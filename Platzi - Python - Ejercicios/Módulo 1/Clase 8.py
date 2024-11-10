to_do = ["Dirigirnos al hotel", 
         "Ir a almorzar",
         "Visitar un moseo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4,-23,51,102.3]
print(numbers)
print(type(numbers))
#Existe el tipo de dato "Lista".
mix = [1,"uno",3.14,True,[2,3,"cuatro"]]
#La sintaxis de las listas nos dice que toda
#La información debe estar dentro "[]".
print(mix)
print(type(mix))
print(len(mix))
print("Primer elemento: ",mix[0])
print("Segundo elemento: ",mix[1])
print("Último elemento: ",mix[-1])
string = "Hola mundo"
print("Primera Letras: ",string[0])
print("Segundo Letras: ",string[1])
print("Último Letras: ",string[-1])
print(mix[:2])
print(mix[2:])
print(mix[2:-2])
mix.append(False)
print(mix)
mix.append(["a","b"])
#Append añade un elemento al final de la 
#Lista
print(mix)
mix.insert(1,["a","b"])
#Insert añade a la lista un elemento en la
#Posición indicada
print(mix.index(["a","b"]))
#Index devuelve la posición en la
#Primera aparición
numbers = [1,2,3,4,-23,51,102.31]
print("Máximo: ",max(numbers))
print("Mínimo: ",min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
#Sirve para eliminar elementos de la lista
del numbers
#Del numbers -> Elimina toda la lista