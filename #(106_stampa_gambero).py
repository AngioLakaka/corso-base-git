#(106_stampa_gambero) Inserisci una parola/frase.
#Stampa il risultato partendo da destra. Es. Giorgio diventa "oigroiG"
i:int=0
parola:str=input("Inserisci una parola o una frase: ")
lunghezza:int=len(parola)
i=lunghezza
indice:str=""
stringa_contrario:str=""
unisci_lista:str=""

parola_contrario:list=[]
while i>0 :
    i=i-1
    indice=parola[i]
    parola_contrario.append(indice)
    #if(i == 0):
      #break
#ho usato la funzione join che ho trovato su google per concatenare
#la lista e farla diventare stringa
stringa_contrario=unisci_lista.join(parola_contrario)
print(stringa_contrario)



