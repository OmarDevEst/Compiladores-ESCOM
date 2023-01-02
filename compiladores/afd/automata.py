class Lenguaje :
    la=0
    lala=0
    le=0
    lento=0
    li=0
    litro=0
    lo=0
    loco=0
    lu=0
    luna=0

def estadoAceptacionLala(lexemas,estado): 
    #Estado Lal
    if(len(lexemas)>estado):
        if(lexemas[estado]== "l" and estado == 2):
            estadoAceptacionLala(lexemas,3)
        #Estado Lala
        if(lexemas[estado]== "a" and estado == 3):
            #checamos que sela el fin de lexema
            if(len(lexemas)==4):
                Lenguaje.lala=Lenguaje.lala+1
        
def estadoAceptacionLento(lexemas,estado):
    
    if(len(lexemas)>estado):
        #Estado Len
        if(lexemas[estado]== "n" and estado == 2):
            estadoAceptacionLento(lexemas,3)
        #Estado Lent
        if(lexemas[estado]== "t" and estado == 3):
            estadoAceptacionLento(lexemas,4)
        #Estado Lento
        if(lexemas[estado]== "o" and estado == 4):
            #descubrimos si es el fin del lexema
            if(len(lexemas)==5):
                Lenguaje.lento=Lenguaje.lento+1

def estadoAceptacionLitro(lexemas,estado):
    if(len(lexemas)>estado):
        #Estado Lit
        if(lexemas[estado]== "t" and estado == 2):
            estadoAceptacionLitro(lexemas,3)
        #Estado Lit
        if(lexemas[estado]== "r" and estado == 3):
            estadoAceptacionLitro(lexemas,4)
        #Estado Litro
        if(lexemas[estado]== "o" and estado == 4):
            #verficamos fin de lexema
            if(len(lexemas)==5):
                Lenguaje.litro=Lenguaje.litro+1
        
def estadoAceptacionLoco(lexemas,estado):
    if(len(lexemas)>estado):
        #Estado Loc
        if(lexemas[estado]== "c" and estado == 2):
            estadoAceptacionLoco(lexemas,3)
        #Estado Loco
        if(lexemas[estado]== "o" and estado == 3):
            #verificamos fin de lexema
            if(len(lexemas)==4):
                Lenguaje.loco = Lenguaje.loco + 1

def estadoAceptacionLuna(lexemas,estado):
    if(len(lexemas)>estado):   
        #Estado Lun
        if(lexemas[estado]== "n" and estado == 2):
            estadoAceptacionLuna(lexemas,3)
        #Estado Luna
        if(lexemas[estado]== "a" and estado == 3):
            #verificamos fin de lexema
            if(len(lexemas)==4):
                Lenguaje.luna = Lenguaje.luna + 1

def estadoAceptacionLConjugada(lexemas,estado):
    #La aceptado
    if(lexemas[estado]== "a" ):
        if (len(lexemas)==2):
            Lenguaje.la = Lenguaje.la + 1
        #Automata continua a lala aceptado
        else:
            estadoAceptacionLala(lexemas,2)
        
    if(lexemas[estado]== "e" ):
        if (len(lexemas)==2):
            Lenguaje.le = Lenguaje.le + 1
        else:
            estadoAceptacionLento(lexemas,2)
    
    if(lexemas[estado]== "i" ):
        if (len(lexemas)==2):
            Lenguaje.li = Lenguaje.li + 1
        else:
            estadoAceptacionLitro(lexemas,2)
            
    if(lexemas[estado]== "o" ):
        if (len(lexemas)==2):
            Lenguaje.lo = Lenguaje.lo + 1
        else:
            estadoAceptacionLoco(lexemas,2)
            
    if(lexemas[estado]== "u" ):
        if (len(lexemas)==2):
            Lenguaje.lu = Lenguaje.lu + 1
        else:
            estadoAceptacionLuna(lexemas,2)   

with open("palabras.txt") as f:
    archivo = " ".join([l.rstrip() for l in f])

lexemas = archivo.split()

for i in range(len(lexemas)):
       
    if lexemas[i][0] == "l" :
        estadoAceptacionLConjugada(lexemas[i],1)    

print("La:" + str(Lenguaje.la))
print("Le:" + str(Lenguaje.le))
print("Li:" + str(Lenguaje.li))
print("Lo:" + str(Lenguaje.lo))
print("Lu:" + str(Lenguaje.lu))
print("Lala:" + str(Lenguaje.lala))
print("Lento:" + str(Lenguaje.lento))
print("Litro:" + str(Lenguaje.litro))
print("Loco:" + str(Lenguaje.litro))
print("Luna:" + str(Lenguaje.luna))
