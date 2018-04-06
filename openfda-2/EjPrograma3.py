import http.client
import json


headers={'User-Agent':'http-client'}
#headers le dices el nombre de tu navegador (chrome, firefox)

SERVER = "api.fda.gov"
RESOURCE = '/drug/label.json?limit=100&search=active_ingredient:acetylsalicylic'
conexion = http.client.HTTPSConnection(SERVER)
# Creo una conexion con la pagina fda. Abro un canal con esa pagina
conexion.request("GET", RESOURCE, None, headers)
# Mando esa peticion de tipo get, y le meto el recurso que me interesa
r1 = conexion.getresponse()
# Es la respuesta de informacion de openfda
if r1.status ==404:
    print("Atencion usuario, Recurso: {} no existe o no encontrado".format(RESOURCE))
    exit(1)
else:
    label = r1.read().decode("utf-8")
    # Lees el contenido de la respuesta y lo decodificas a utf8 para que se vean tildes o cosas raras
    # Se guarda en la variable que contiene toodo el fichero json de tipo string
    conexion.close()
    #Cierro la conexión con la pagina
    info = json.loads(label)
    # Cargas toodo el fichero json y lo guardas en una variable, y se lo coloca bien. Es la estructura del fichero
    #Creo un try-except para comprobar que existe el nombre del fabricante, y el programa no se pare por completo

    for i in range(len (info['results'])):
        medicamento_info=info['results'][i]

        if (medicamento_info['openfda']):
            print("El ID del medicamento es: ", medicamento_info['id'])
            print("-El medicamento lo fabrica:",medicamento_info['openfda']['manufacturer_name'][0])
            print("")
        else:

            print("El ID del medicamento es: ", medicamento_info['id'])
            print("*Atención, se desconoce el nombre del fabricante")
            print("")


