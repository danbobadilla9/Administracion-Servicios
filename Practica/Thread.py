import schedule
import time
import threading
import rrdtool
import os
from pysnmp.hlapi import *
from copy import copy

def updateSNMP(data,index):
    while 1:
        paquetesMulticast = int(
            consultaSNMP(data["comunidad"],data["ip"],
                        '1.3.6.1.2.1.2.2.1.17.1'))
        paquetesIp = int(
            consultaSNMP(data["comunidad"],data["ip"],
                        '1.3.6.1.2.1.4.10.0'))
        icmpEnviados = int(
            consultaSNMP(data["comunidad"],data["ip"],
                        '1.3.6.1.2.1.5.1.0'))
        tcpTransmitidos = int(
            consultaSNMP(data["comunidad"],data["ip"],
                        '1.3.6.1.2.1.6.12.0'))
        datagramasEnviados = int(
            consultaSNMP(data["comunidad"],data["ip"],
                        '1.3.6.1.2.1.7.4.0'))
        
        valor = "N:" + str(paquetesMulticast) + ':' + str(paquetesIp) + ':' + str(icmpEnviados) + ':' + str(tcpTransmitidos) + ':' + str(datagramasEnviados)
        # print (valor)
        rrdtool.update(str(index)+'.rrd', valor)
    # rrdtool.dump('traficoRED.rrd','traficoRED.xml')
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)




def consultaSNMP(comunidad,host,oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            varB=(' = '.join([x.prettyPrint() for x in varBind]))
            resultado= varB.split()[2]
    return resultado

def createDB(data,index):
    #Primero comprobamos que la BD ya este creada 
    if not os.path.exists('/home/user/Documentos/Administracion-Servicios-Red/Practica-2/Practica/'+str(index)+'.rrd'):
        #Creamos la BD denominada index.rrd
        #--start "Iniciamos en la hora actual del sistema"
        #--step "Indicamos el tiempo de cada intervalo"
        #--DS "El data source es un contador que toma 120segundos = 2 minutos con una cantidad minima y maxima desconocidas"
        #--RRA " es un promedio de los datos, cuyo 0.5 es aceptado, toma 1 step y 200 registros"
        ret = rrdtool.create(str(index)+".rrd",
                        "--start",'1668489780',
                        "--step",'60',
                        "DS:multiCastSalida:COUNTER:120:U:U",
                        "DS:paquetesIpSalida:COUNTER:120:U:U",
                        "DS:icmpEntrada:COUNTER:120:U:U",
                        "DS:segmentosSalida:COUNTER:120:U:U",
                        "DS:datagramasSalida:COUNTER:120:U:U",
                        "RRA:AVERAGE:0.5:1:200",
                        "RRA:AVERAGE:0.5:1:200",
                        "RRA:AVERAGE:0.5:1:200",
                        "RRA:AVERAGE:0.5:1:200",
                        "RRA:AVERAGE:0.5:1:200")
        if ret:
            print (rrdtool.error())
    else:
        print("DB YA INSTANCIADA")

def initThread(js,index):
    createDB(js,index)
    data = copy(js)
    updateSNMP(data,index)
