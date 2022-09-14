import jinja2
import pdfkit

def creaPDF(ruta_template,info,rutacss='/home/user/Documentos/Administracion-Servicios-Red/Practica-1/CSS/style.css'):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template,'')
    
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)

    html = template.render(info)

    options = {
        'page-size':"Letter",
        'margin-top':'0.05in',
        'margin-right':'0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding':'UTF-8',
        'enable-local-file-access': ""
    }

    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    ruta_salida = '/home/user/Documentos/Administracion-Servicios-Red/Practica-1/datos-agente.pdf'
    pdfkit.from_string(html,ruta_salida,css=rutacss,options=options,configuration=config)
