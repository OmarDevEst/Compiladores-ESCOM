class Lenguaje :
    lacteo=0
    lampara=0
    lambdas=0
    taco=0
    
def estadoAceptacionTaco(lexemas,estado):
    if(len(lexemas)>estado):
        if(lexemas[estado] =="a"and estado == 1):
            estadoAceptacionTaco(lexemas,2)
        
        if(lexemas[estado] =="c"and estado == 2):
                estadoAceptacionTaco(lexemas,3)
        
        if(lexemas[estado] =="o" and estado==3):
            if(len(lexemas)==4):
                Lenguaje.taco=Lenguaje.taco + 1
                    
def estadoLa(lexemas,estado):
    if(lexemas[estado]=="a"):
        estadoAceptacionLacteo(lexemas,2)
        estadoLam(lexemas,2)

def estadoLam(lexemas,estado):
    if(len(lexemas)>estado):
        if(lexemas[estado] == "m" and estado == 2):
                estadoAceptacionLampara(lexemas,3)
                estadoAceptacionLambda(lexemas,3)

def estadoAceptacionLacteo(lexemas,estado):
    
    if(len(lexemas)>estado):
        if(lexemas[estado] =="c"and estado == 2):
                estadoAceptacionLacteo(lexemas,3)
              
        if(lexemas[estado] =="t"and estado == 3):
                estadoAceptacionLacteo(lexemas,4) 

        if(lexemas[estado] =="e"and estado == 4):
                estadoAceptacionLacteo(lexemas,5)   
                
        if(lexemas[estado] =="o" and estado==5):   
                if(len(lexemas)==6):  
                    Lenguaje.lacteo=Lenguaje.lacteo + 1
                
def estadoAceptacionLampara(lexemas,estado):
    if(len(lexemas)>estado):
        if(lexemas[estado] =="p"and estado == 3):
            estadoAceptacionLampara(lexemas,4)
        
        if(lexemas[estado] =="a"and estado == 4):
            estadoAceptacionLampara(lexemas,5)

        if(lexemas[estado] =="r"and estado == 5):
            estadoAceptacionLampara(lexemas,6)

        if(lexemas[estado] =="a" and estado==6): 

            if(len(lexemas)==7):  
                Lenguaje.lampara=Lenguaje.lampara + 1
            
def estadoAceptacionLambda(lexemas,estado):
    if(len(lexemas)>estado):
        if(lexemas[estado] =="b"and estado == 3):
            estadoAceptacionLambda(lexemas,4)
        
        if(lexemas[estado] =="d"and estado == 4):
            estadoAceptacionLambda(lexemas,5)
        
        if(lexemas[estado] =="a" and estado==5): 
            if(len(lexemas)==6):  
                Lenguaje.lambdas=Lenguaje.lambdas + 1


    

with open("palabras.txt") as f:
    archivo = " ".join([l.rstrip() for l in f])

lexemas = archivo.split()

for i in range(len(lexemas)):
       
    if lexemas[i][0] == "l" :
        estadoLa(lexemas[i],1)
        
    if lexemas[i][0] == "t" :
        estadoAceptacionTaco(lexemas[i],1)

        

print("taco:" + str(Lenguaje.taco))
print("lacteo:" + str(Lenguaje.lacteo))
print("lampara:" + str(Lenguaje.lampara))
print("lambda:" + str(Lenguaje.lambdas))