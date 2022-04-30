# Al quitarle cuatro kilos al peso de Quico se obtiene dos veces el peso del chavo y si sumamos los pesos de Quico y el chavo se obtiene cinco veces el peso de Ñoño (todos en pesos enteros). En la vecindad se dice que una persona está en etapa 'uno' si está entre 0 y 20 kilos, en etapa 'dos' si está entre 21 y 40 kilos, en etapa 'tres si está entre 41 y 80 kilos y en etapa 'cuatro' si está por encima de 80 kilos. Dado el peso del chavo, realizar un programa que imprima en la primera línea los pesos del Chavo, Quico y Ñoño separados por un solo espacio y en la segunda línea indique en qué etapa se encuentra Ñoño.

peso = int(input("Ingresa el peso del chavo: " ))

chavo = peso
quico = (chavo * 2) + 4
nono = (chavo + quico) / 5

print(chavo, quico, int(nono))

if(nono >= 0 and nono <= 20):
    print("uno")
elif(nono >= 21 and nono <= 40):
    print("dos")
elif(nono >= 41 and nono <= 80):
    print("tres")
elif(nono > 80):
    print("cuatro")