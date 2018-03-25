import http.client
import json

SERVER = "api.fda.gov"
RESOURCE = "/drug/label.json?limit=10"   #limit=10 significa que busco 10 medicamentos

headers = {'User-Agent': 'http-client'}
#headers le dices el nombre de tu navegador (chrome, firefox)
conexion = http.client.HTTPSConnection(SERVER)
#Creo una conexion con la pagina fda. Abro un canal con esa pagina
conexion.request("GET", RESOURCE, None, headers)
#Mando esa peticion de tipo get, y le meto el recurso que me interesa

r1 = conexion.getresponse()
#Es la respuesta de informacion de openfda
if r1.status==404:
    print("Atencion usuario, Recurso: {} no existe o no encontrado".format(RESOURCE))
    exit(1)
else:

    label = r1.read().decode("utf-8")
    # Lees el contenido de la respuesta y lo decodificas a utf8 para que se vean tildes o cosas raras
    # Se guarda en la variable que contiene toodo el fichero json de tipo string

    conexion.close()

    info = json.loads(label)
    #Cargas toodo el fichero json y lo guardas en una variable, y se lo coloca bien. Es la estructura del fichero
    for i in range(len(info['results'])):
        medicamento_info = info['results'][i]
        print('El ID del medicamento', [i+1], 'es: ', medicamento_info['id'])
