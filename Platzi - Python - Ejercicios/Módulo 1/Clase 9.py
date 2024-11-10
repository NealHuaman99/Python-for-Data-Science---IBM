matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(matrix)
print(matrix[2][1])
matrix_2 =[[1,2],[3,4],
           [5,6],[7,8],
           [9,10],[11,12]]
print(matrix_2)
print(matrix_2[3][0])
#Las dimensiones con que trabaja siempre son 2
#(Fila,Columna) siguiendo ese orden
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))
#Cuando se hace con o sin (), es una tupla
#En una tupla no se puede modificar los elementos
print(numbers[0])
#numbers[0] = "unos" -> Para cambiar datos, pero en
#Una Tupla no se puede, sale error
#print(numbers)