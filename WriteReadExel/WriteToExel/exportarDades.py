import time

def exportar(fitxer, sensor, dades):
    csv=open(fitxer,"a")  
    data=time.strftime("%x")
    hora=time.strftime("%X")
    print(fitxer)
    print(sensor+","+dades+","+data+","+hora)
    csv.write(sensor+","+dades+","+data+","+hora+"\n")
    
#exportar("dades3.csv","Temperatura Motor","99")
