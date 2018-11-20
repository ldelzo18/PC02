def menor_en_arreglo(arreglo):
    menor = arreglo[0]
    for x in range(len(arreglo)):
        
        if arreglo[x] < menor:
            temp = arreglo[x]
            arreglo[x] = menor
            menor = temp
    return menor

numeros = []

while(len(numeros)<5):
    try:
        numeros.append((int)(input("Ingrese un numero:\n")))
    except:
        print("El numero ingresado no es valido!, por favor ingrese otro numero")

print("El menor valor de todos los numeros ingresados es: ",menor_en_arreglo(numeros))