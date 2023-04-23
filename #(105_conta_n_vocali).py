#(105_conta_n_vocali) 
#Conta il numero di vocali e stampane il risultato per ogni vocale. 
#Giorgio. a=0, e=0, i=2, o=2, u=0
i:int=0
count_a:int=0
count_e:int=0
count_i:int=0
count_o:int=0
count_u:int=0
parola:str=input("Inserisci una parola: ")
lunghezza=len(parola)
indice:str=""
while i <=lunghezza : 
     indice=parola[i]
     if(indice == "a"):
        count_a= count_a + 1
     if(indice == "e"):
        count_e = count_e + 1
     if(indice == "i"):
        count_i = count_i + 1
     if(indice == "o "):
        count_o = count_o + 1
     if(indice == "u"):
        count_u = count_u + 1
     i=i+1
print("a " + "= " + str(count_a))  
print("e " + "= " + str(count_e))  
print("i " + "= " + str(count_i))  
print("o " + "= " + str(count_o))  
print("u " + "= " + str(count_u))  


       

