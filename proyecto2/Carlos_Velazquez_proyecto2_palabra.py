palab = input("ingrese una palabra entre 4 y 8 letras: ") # se pide una palabra que contenga enmtre 4 y 8 letras guardandola en la variable palab

comp = (len(palab)) # se guarda en la variable comp cuantas letras tiene la cadena palab )ingresada por el usuario) por medio de len

if 4 <= comp <= 8 :
    print("la palabra es correcta") #se hace una condición donde si la palabra ingresada por el usuario esta en el rango de 4 y 8 letras se da un mensaje que es correcto 
elif comp < 4 :
    print(f'Hacen falta letras. solo tiene {comp} letras, solo se aceptan palabras entre 4 y 8 letras. GRACIAS') #se hace una condición donde si la palabra ingresada por el usuario es menor a 4 letras, se le indica por medio de un menseje que no se aceptan palabras entre 4 y 8 letras
elif comp > 8 :
    print(f'sobran letras tiene {comp} letras, solo se aceptan palabras entre 4 y 8 letras. GRACIAS') #se hace una condición donde si la palabra ingresada por el usuario es mayor a 8 letras, se le indica por medio de un menseje que no se aceptan palabras entre 4 y 8 letras

