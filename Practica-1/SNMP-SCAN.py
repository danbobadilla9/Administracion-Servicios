from copy import copy
from distutils.log import info
import PeticionesSNMP
import json
import PDF

def registrados():
    file = open("./json/db.json","r")
    js = json.loads(file.read())
    if js :
        print("\t Mostrando dispositivos conocidos \n")
        for agentes in js:
            print("Agente: "+agentes)
            # for key, info in js[agentes].items():
            #     print(key,info)
            # print("\n")
            cantInter = PeticionesSNMP.resumen(js[agentes],"1.3.6.1.2.1.2.1.0")
            print("3) Numero de interfaces de red: "+cantInter)
            print("4) Estado administrativo y descripción de sus interfaces de red \n")
            for i in range(1,int(cantInter)+1):
                print("Interfaz: "+str(i)+" Desc: "+PeticionesSNMP.resumen(js[agentes],"1.3.6.1.2.1.2.2.1.2."+str(i))+"\nEstado: "+("Interfaz Desactivada","Interfaz Activa")[int(PeticionesSNMP.resumen(js[agentes],"1.3.6.1.2.1.2.2.1.8."+str(i))) == 1]+"\n")
            print("\n")
            lastIndex = agentes
        return (int(lastIndex),js)
    else:
        print("\t No hay dispositivos conocidos \n")
        return (0, js)
    

def agregarDispositivo(lastIndex,js):
    ip = input("Ingresa la dirección del agente: ")
    snmpv = input("Ingresa la version de SNMP: ")
    comunidad = input("Ingresa el nombre de la comunidad: ")
    puerto = input("Ingrese el puerto: ")
    #Escribiendo en el archivo
    file = open("./json/db.json","w")
    datos = {"ip":ip,"snmpv":snmpv,"comunidad":comunidad,"puerto":puerto}
    agente = copy(js)
    agente [str(lastIndex+1)]= datos
    json.dump(agente,file, indent=4)
    return agente 

def eliminarDispositivo(js):
    numAgente = input("Ingresa el numero de agente a eliminar: ")
    try:
        js.pop(numAgente)
    except KeyError:
        print("El elemento a eliminar no existe")
    file = open("./json/db.json","w")
    json.dump(js,file, indent=4)
    return js

def generarReporte(js):
    numAgente = input("Ingresa el numero de agente: ")
    agente = js.get(numAgente)
    datos = PeticionesSNMP.resumen(agente,'1.3.6.1.2.1.1.1.0').split(' ')
    cantInter = PeticionesSNMP.resumen(agente,"1.3.6.1.2.1.2.1.0")
    info = {}
    if datos[1] == "Linux":
        info['logo'] = 'src="/home/user/Documentos/Administracion-Servicios-Red/Practica-1/img/linux.png"'
        info['sistema'] = datos[1]
    else:
        info['logo'] = 'src="/home/user/Documentos/Administracion-Servicios-Red/Practica-1/img/windows.png"'
        info['sistema'] = 'Windows'
    info['nombreDispositivo'] = PeticionesSNMP.resumen(agente,'1.3.6.1.2.1.1.5.0')
    info['contacto'] = PeticionesSNMP.resumen(agente,'1.3.6.1.2.1.1.4.0')
    info['ubicacion'] = PeticionesSNMP.resumen(agente,'1.3.6.1.2.1.1.6.0')
    info['numeroI'] = PeticionesSNMP.resumen(agente,"1.3.6.1.2.1.2.1.0")
    tabla = ""
    for i in range(1,int(cantInter)+1):
        encabe = f'<tr><th>Interfaz {i} </th><th>Estado</th></tr>'
        desc = PeticionesSNMP.resumen(agente,"1.3.6.1.2.1.2.2.1.2."+str(i))
        estado = ("Interfaz Desactivada","Interfaz Activa")[int(PeticionesSNMP.resumen(agente,"1.3.6.1.2.1.2.2.1.8."+str(i))) == 1]
        cuerpo = f'<tr><td>Descripción: {desc} </td><td>{estado}</td></tr>'
        divTabla = f'<div><table class="demo"><thead>{encabe}</thead><tbody>{cuerpo}</tbody></table><div/>'
        tabla+=divTabla
    info['tabla'] = tabla
    ruta_template = '/home/user/Documentos/Administracion-Servicios-Red/Practica-1/template.html'
    PDF.creaPDF(ruta_template,info)
    
print("Resumen de los dispositivos previamente registrados \n")
(lastIndex,js) = registrados()
print("Funciones disponibles \n")
print(" \t 1)Agregar Dispositivo \n")
print(" \t 2)Eliminar Dispositivo \n")
print(" \t 3)Generar Reporte PDF \n")
print(" \t 4)Exit \n")
opcion = input("Inserte opcion: ")
while True:
    if int(opcion) == 1:
        js = agregarDispositivo(lastIndex,js)
    elif int(opcion) == 2:
        js = eliminarDispositivo(js)
    elif int(opcion) == 3:
        generarReporte(js)
    elif int(opcion) == 4:
        exit()
    opcion = input("Inserte opcion: ")
