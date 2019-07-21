import time
fitxer="dades2.csv"
csv=open(fitxer,"a")
i=0
data=time.strftime("%x")
hora=time.strftime("%X")
info=data+","+hora

for i in range (5):
        csv.write("Motor,"+info+","+str(i)+"\n")
        csv.write("Velocidad,"+info+","+str(i)+"\n")
        csv.write("RPM,"+info+","+str(i)+"\n")
