#inserisci i 3 valori di A, B e C e risolvi l'equazione di secondo grado con relative formule
import math
a_valore=0
b_valore=0
c_valore=0
def delta_eqz(a=int,b=int,c=int):
    risultato=int((b*b)-4*(a*c))
    return  risultato
print("EQUAZIONI DI SECONDO GRADO")
#assicuro che ci sia almeno un valore diverso da 0
while (a_valore == 0 and b_valore == 0 and c_valore == 0):
    print("inserisci almeno un valore diverso da 0")
    a_valore=int(input("Inserisci il valore di a: "))
    b_valore=int(input("Inserisci il valore di b: "))
    c_valore=int(input("Inserisci il valore di c: "))
     
#restituisco in output il tipo di equazione in base ai valori inseriti e scrivo l'equazione
if(c_valore == 0):
    print("Questa è spuria")
    print(("L'equazione è ") + (str(a_valore)) + ("x^2") + (" + ") + str(b_valore) +("x")  + (" = 0"))
if(b_valore == 0):
    print("Questa è pura")
    print(("L'equazione è ") + (str(a_valore)) + ("x^2")  + (" + ") + str(c_valore) + (" = 0"))
if(b_valore == 0 and c_valore == 0):
    print("Questa è monomia")
    print(("L'equazione è ") + (str(a_valore)) + ("x^2")  + (" = 0"))
if(a_valore!=0 and b_valore!=0 and c_valore!=0):
    print("Questa è completa")
    print(("L'equazione è ") + (str(a_valore)) + ("x^2") + (" + ") + str(b_valore) +("x") + (" + ") + str(c_valore) + (" = 0"))
#applico le formule per la risoluzione
print("Faccio il delta")
delta=(delta_eqz(a_valore,b_valore,c_valore))
print("Il delta è "+ str(delta))
if(delta<0):
    print("L'equazione è impossibile")
if(delta == 0):
    print("L'equazione ha 2 soluzioni reali e coincidenti")
    sopra_x1=(-1*b_valore) +  math.sqrt(delta)
    sopra_x2=(-1*b_valore) -  math.sqrt(delta)
    x1= (sopra_x1/ 2*a_valore ) 
    x2= (sopra_x2/ 2*a_valore)  
    print("x1 vale " + str(x1))
    print("x2 vale " + str(x2))  
if(delta > 0):
    print("L'equazione ha due soluzioni reali e distinte")   
    sopra_x1=(-1*b_valore) +  math.sqrt(delta)
    sopra_x2=(-1*b_valore) -  math.sqrt(delta)
    x1= (sopra_x1/ 2*a_valore ) 
    x2= (sopra_x2/ 2*a_valore)  
    #restituisco i 2 valori di x 
    print("x1 vale " + str(x1))
    print("x2 vale " + str(x2))



     
     
    
