class Requisitos:
    estados=[]
    lexemas=[]
    inicial=[]
    final=[]
    transicion=[]
    cadenas=[]
    flag=False
 
def LLenarTabla (Tabla,Lenguaje):
    for i in range(0, len(Lenguaje.transicion)):
            x=int(Lenguaje.transicion[i][0])
            y=int(Lenguaje.lexemas[Lenguaje.transicion[i][1]])
            Tabla[x][y].append(Lenguaje.transicion[i][2])

    return Tabla
            #a     #b      #c
# tabla = q0[[0,1][0][]
#          q1[null][2]
#          q2[null][null]]
#por el momento buscamos conocer donde estamos parados

def Automata(cadena,Lenguaje,Estado,iterador,Tabla,historial):
    if(len(cadena)>iterador):
        if(cadena[iterador] in Lenguaje.lexemas):
            historial=historial+"("+cadena[iterador]+")->"
            y=Lenguaje.lexemas[cadena[iterador]]
            x=int(Estado)
            Transiciones=len(Tabla[x][y])
            for i in range(0,Transiciones):
                Automata(cadena,Lenguaje,Tabla[x][y][i],iterador+1,Tabla,historial + "q"+ Tabla[x][y][i])
            if(Transiciones == 0):
                print("Rama muerta")
                Automata(cadena,Lenguaje,x,iterador+1,Tabla,historial + "q"+str(x))
    else:
        if(Estado in Lenguaje.final):
            Lenguaje.cadenas.append(historial)
            Lenguaje.flag=True
            
#por el momento hace transiciones
#falta detener y validar algunas cosas           
def main():#Abrimos archivo y tratamos datos para poder ser tratados
    archivo = open("AF.txt", "r")
    id= []
    iterador=0
    Lenguaje=Requisitos()

    for line in archivo:
        for number in line.split():
            if iterador == 0:
                Lenguaje.estados=number.split(",")
            if iterador == 1:
                Lenguaje.lexemas=number.split(",")
            if iterador == 2:
                Lenguaje.inicial=number.split(",")
            if iterador == 3:
                Lenguaje.final=number.split(",")
            if iterador > 3:
                Lenguaje.transicion.append(number.split(","))
            iterador= iterador + 1 
    #---------------------------------------------------------------
    #creamo diccionario de lexemas
    for i in range(0,len(Lenguaje.lexemas)):
        id.append(i)

    aux = {}

    for i in range(len(Lenguaje.lexemas)):
        aux[Lenguaje.lexemas[i]]=id[i]    
    Lenguaje.lexemas=aux
    #-------------------------------------------------------------
    # print(Lenguaje.estados)
    # print(Lenguaje.lexemas)
    # print(Lenguaje.transicion)

    cadena = input("Ingrese cada a evaluar:")

    Tabla= [[[] for x in range(len(Lenguaje.lexemas))] for y in range(len(Lenguaje.estados))] 
    Tabla=LLenarTabla(Tabla,Lenguaje)
    
    Historial="q"+str(Lenguaje.inicial[0])
    
    Automata(cadena,Lenguaje,int(Lenguaje.inicial[0]),0,Tabla,Historial)
    
    if(Lenguaje.flag):
        print("Cadena Valida")
    else:
        print("Cadena Invalida")

    for i in range(len(Lenguaje.cadenas)):
        print(Lenguaje.cadenas[i])
        
main()