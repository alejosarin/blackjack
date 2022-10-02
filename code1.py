import random
carta=int(random.uniform(1,13))
carta1tallador=int(random.uniform(1,13))
print("\n\nTu carta es : " + str(carta))
print("Quieres otra carta?")
# Se despliega el menu
suma=carta
print("1. Si.")
print("2. No.")
decision=int(input("Digita tu eleccion: "))
#JUEGO DEL USUARIO
while decision!=2:
    carta=int(random.uniform(1,13))
    suma=suma+carta
    print("\nTu carta es " + str(carta))
    print("La suma de sus cartas es : "+str(suma))
    if suma>21:
        print("\n\nPERDISTE")
        break
    print("Quieres otra carta?")
    print("1. Si.")
    print("2. No.")
    decision=int(input("Digita tu eleccion: "))
    suma2=0
    print("\n\n")
    print("---------------------------------------------------------------------")
    print("\n\n")
    while suma2<suma:
        suma2=carta1tallador+suma2
        print("La carta del tallador es  " + str(carta1tallador))
        if suma2>21:
            print("La suma del tallador es " +str(suma2))
            print("\n\nGANASTE")
            break
        elif suma2>suma or suma2==suma:
            print("La suma del tallador es " +str(suma2))
            print("\n\nPERDISTE")
            break
        carta1tallador=int(random.uniform(1,13))

    
    
    
    

    

