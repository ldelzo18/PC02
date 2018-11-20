matriz = [[1,3,5,1],[5,7,9,8],[9,6,8,9],[15,54,2,4]]

temp = 0
puntero = 0
for x in range(len(matriz)):
    temp += matriz[x][puntero]
    puntero += 1

print("La suma de la diagonal es ",temp)
    