class Produccion:
    flag = False

def esPalindromo (iDerecha,iIzquierda,cadena,Producciones):
    if iDerecha != iIzquierda and iDerecha < iIzquierda:
        if cadena[iDerecha] == cadena[iIzquierda]:
            esPalindromo(iDerecha + 1, iIzquierda - 1, cadena,Producciones)
    else:
        Producciones.flag = True

    
flag=False 
Producciones=Produccion()
cadena = input("Introduce una cadena: ")
flag=esPalindromo(0, len(cadena) - 1,cadena,Producciones)
if(Producciones.flag):
    print("----Cadena Valida----")  
else:  
    print("----Cadena Invalida----")
