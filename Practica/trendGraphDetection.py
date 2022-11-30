import sys
import rrdtool
import time
import datetime
from  Notify import send_alert_attached
import time
rrdpath = './'
imgpath = './'

def generarGrafica(ultima_lectura,title,variable):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv( imgpath+"deteccion.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label="+variable+" load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title="+title,
                    "DEF:cargaCPU="+rrdpath+"1.rrd:"+variable+":AVERAGE",
                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",
                     "CDEF:umbral50=cargaCPU,50,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga de"+variable,
                     "AREA:umbral50#FF9F00:Carga "+variable+" mayor de 50",
                     "HRULE:8#FF0000:Umbral  50%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )