x=0
while x <=45:
    dato = float(input("ingrese un valor:"))
    x = dato+x
    print("suma acumulada:", x)
    if 0 <= dato <=5:
        print("Numero valido")
        
    else:
        print("Numero invalido")
        break

    