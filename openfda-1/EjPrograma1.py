import http.client
import json

headers = {'User-Agent': 'http-client'}
#headers le dices el nombre de tu navegador (chrome, firefox)
conexion = http.client.HTTPSConnection("api.fda.gov")
#Creo una conexion con la pagina fda. Abro un canal con esa pagina
conexion.request("GET", "/drug/label.json", None, headers)
#Mando esa peticion de tipo get, y le meto el recurso que me interesa
r1 = conexion.getresponse()
#Es la respuesta de informacion de openfda
print(r1.status, r1.reason)
#El status es 200, y la razon OK
label = r1.read().decode("utf-8")
# Lees el contenido de la respuesta y lo decodificas a utf8 para que se vean tildes o cosas raras
# Se guarda en la variable que contiene toodo el fichero json de tipo string
conexion.close()

info = json.loads(label)
#Cargas toodo el fichero json y lo guardas en una variable, y se lo coloca bien. Es la estructura del fichero
medicamento_info=info['results'][0]
#Results es una lista que tiene una unica posicion, y dentro tiene mas informacion

print('El ID del medicamento es: ', medicamento_info['id'])
print('El medicamento se usa para: ', medicamento_info['purpose'][0])
print('El medicamento lo fabrica: ', medicamento_info['openfda']['manufacturer_name'][0])




