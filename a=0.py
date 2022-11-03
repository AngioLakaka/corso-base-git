
max=0
min=1000000000000000
while True:
    i=int(input("Inserisci i numeri: "))
    if(i==0):
        break 
    if(i<min):
        min=i   
    if(i>max):
        max=i
    
if(max==0):
    print("Non hai inserito abbastanza numeri")
else:
     str_min=str(min)
     str_max=str(max)
     print("il numero minimo è: "+ str_min)
     print("il numero massimo è: "+ str_max)

