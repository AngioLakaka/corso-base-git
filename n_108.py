#(108_stringa_bilanciata) Chiedi all'utente 2 stringhe. 
# Controlla che tutti i caratteri presenti nella prima stringa siano presenti nella seconda striga. 
# Non importa la posizione.
 #Stampa il risultato se vero o falso.
i = 0
stringa1= input("Inserisci una stringa: ")
lunghezza1=len(stringa1)
stringa2=input("inserisci una seconda stringa: ")
is_present=bool

while i < lunghezza1:
      is_present=stringa1[i] in stringa2   
      if(is_present == False):
        break

      i = i+1
print(is_present)
