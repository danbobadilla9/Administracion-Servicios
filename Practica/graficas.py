import datetime
import sys
import rrdtool
import time

def instanciarGrafica(agente,index):
    print("\tEl formato a ingresar es el siguiente: MM/DD/YYYY, H:M:S\n")
    horaInicio = input("\t Ingresa la hora de inicio del reporte: ")
    unix_time = datetime.datetime.timestamp(datetime.datetime.strptime(horaInicio,"%m/%d/%Y, %H:%M:%S"))
    tiempoInicial = int(unix_time)
    horaInicio = input("\t Ingresa la hora de fin del reporte: ")
    unix_time = datetime.datetime.timestamp(datetime.datetime.strptime(horaInicio,"%m/%d/%Y, %H:%M:%S"))
    tiempoFinal = int(unix_time)
    #Generando 1 grafica paquetes Multicast enviados
    generarGrafica(agente,index,"G1",tiempoInicial,tiempoFinal,
    "Multicast","Paquetes Multicast Enviados","multiCastSalida","maxMulti","#2bdfff","Paquetes Multicast enviados")

    #Generando 2 grafica paquetes que utiliza el protocolo IP
    generarGrafica(agente,index,"G2",tiempoInicial,tiempoFinal,
    "Paquetes IP Salida","Paquetes que envia el protocolo IP","paquetesIpSalida","maxSalida","#b800dc","Paquetes Enviados")

    #Generando 3 grafica  Mensajes ICMP que ah recibido el agente
    generarGrafica(agente,index,"G3",tiempoInicial,tiempoFinal,
    "ICMP","Mensajes ICMP recibidos ","icmpEntrada","maxICMP","#ff4b69","Mensajes ICMP recibidos")

    #Generando 4 grafica Segmentos TCP
    generarGrafica(agente,index,"G4",tiempoInicial,tiempoFinal,
    "Segmentos TCP","Segmentos TCP transmitidos que contienen \n uno o más octetos transmitidos previamente",
    "segmentosSalida","maxTCP","#c7ff25","Segmentos TCP")

    #Generando 5 grafica DataGrams enviados por el agente ?
    generarGrafica(agente,index,"G5",tiempoInicial,tiempoFinal,
    "Datagrams","Datagramas que ha enviado el dispositivo","datagramasSalida","maxDatagrama","#9300ff",
    "Datagramas enviados por le dispositivo")

    return

def generarGrafica(agente,idDB,nameImagen,tiempoInicial,tiempoFinal,labelEjeY,title,dataStore,nameMax,color,nameLinea):
    ret = rrdtool.graphv( nameImagen+".png",
                     "--start",str(tiempoInicial),
                     "--end",str(tiempoFinal),
                     "--vertical-label="+labelEjeY,
                     "--title="+title,
                     "DEF:informacion="+str(idDB)+".rrd:"+dataStore+":AVERAGE",
                     "VDEF:informacionLast=informacion,LAST",
                     "VDEF:segEntradaMax=informacion,MAXIMUM",
                     "PRINT:informacionLast:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S " + nameMax,
                     "LINE3:informacion" + color + ":" + nameLinea)
