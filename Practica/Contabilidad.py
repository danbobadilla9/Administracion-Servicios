import datetime


def generarReporteContabilidad():
    print("\tEl reporte se ejecutara en todos los agentes conocidos \n")
    print("\tCondiciones de horario: EL usuario no puede ingresar una fecha antes de los records que se tengan en la BD\n")
    print("\tEl formato a ingresar es el siguiente: MM/DD/YYYY, H:M:S\n")
    horaInicio = input("\t Ingresa la hora de inicio del reporte: ")
    unix_Time = unix_time = datetime.datetime.timestamp(datetime.datetime.strptime(horaInicio,"%m/%d/%Y, %H:%M:%S"))
    print("Hora inicio"+str(unix_Time))
    horaInicio = input("\t Ingresa la hora de fin del reporte: ")
    unix_Time = unix_time = datetime.datetime.timestamp(datetime.datetime.strptime(horaInicio,"%m/%d/%Y, %H:%M:%S"))
    print("Hora finalizacion"+str( type (unix_Time)))
    
    
    return;