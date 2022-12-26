i=0
output=0
print("LE TABELLINE")
numero=int(input("Inserisci un numero: "))
if(numero== 0):
    print("Non esiste la tabellina dello zero")
while numero==0:
    numero=int(input("Inserisci un numero: "))
    print("Non esiste la tabellina dello zero")
     


while i < 10:
     i=i+1
     output=numero*i 
     print (str(numero)+ " * "+ str(i) +" = " + str(output))
     
        

     
     
    
