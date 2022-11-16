from pysnmp.hlapi import *

def resumen(agente,OID):
    data = ""
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(agente["comunidad"],mpModel=int(agente["snmpv"])),
        UdpTransportTarget((agente["ip"],int(agente["puerto"]))),
        ContextData(),
        ObjectType(ObjectIdentity(OID))
    )

    errorIndication,errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s '%(errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
    else:
        for varBind in varBinds:
            loc = str(varBind).find('=')
            data = str(varBind)[loc+1:]
    return data
