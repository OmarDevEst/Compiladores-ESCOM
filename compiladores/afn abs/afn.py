class Aceptacion:
    flag=False

def automataLenguajeAB(lexema,transicion,estado):
    if estado == 0:
        if (len(lexema) -1) >= transicion :
            if((len(lexema)-1)  == transicion):
                Aceptacion.flag = True
            if(not Aceptacion.flag):
                if lexema[transicion] == 'a':
                    transicion = transicion+1
                    automataLenguajeAB(lexema,transicion,1)
                    automataLenguajeAB(lexema,transicion,0)
                if lexema[transicion] == 'b':
                    transicion = transicion+1
                    automataLenguajeAB(lexema,transicion,0)
            
        
    if estado == 1:
        if (len(lexema) -1 )>= transicion :
            if lexema[transicion] == 'b':
                transicion = transicion+1
                automataLenguajeAB(lexema,transicion,2)
            
            
    if estado == 2:
        if((len(lexema))==transicion):
            Aceptacion.flag =True



print("Bienvenideo al automata AFN")
lexema=input("Ingrese cadena:")


transicion=0
estado=0

automataLenguajeAB(lexema,transicion,estado)

print(Aceptacion.flag)
