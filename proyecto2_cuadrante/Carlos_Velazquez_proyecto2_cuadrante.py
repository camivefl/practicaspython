x = int(input("ingrese la cordenada x: ")) #se pide la cordenada x, se hace un cast de str a int
y = int(input("ingrese la cordenada y: "))# se pide la cordenada y, se hace un cast de str a int

if x > 0 and y > 0 :
    print('la cordenada se encuenra en el primer cuadrante') # se condiciona que si x es mayor a 0 e y es mayor a cero nuestra cordenada se encuentra en el primer cuadrante
elif x < 0 and y > 0 :
    print('la cordenada se encuenra en el segundo cuadrante') # se condiciona que si x es menor a 0 e y es mayor a cero nuestra cordenada se encuentra en el segundo cuadrante
elif x < 0 and y < 0 :
    print('la cordenada se encuenra en el tercer cuadrante')# se condiciona que si x es menor a 0 e y es menor a cero nuestra cordenada se encuentra en el tercer cuadrante
elif x > 0 and y < 0 :
    print('la cordenada se encuenra en el cuarto cuadrante')# se condiciona que si x es mayor a 0 e y es menor a cero nuestra cordenada se encuentra en el cuarto cuadrante
elif x == 0 and y == 0 :
    print('la cordenada se encuentra en (0,0), sigue en el origen') # se condiciono a x e y iguales a cero, donde el punto no se mueve del origen (0,0)