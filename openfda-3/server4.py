import http.server
import socketserver       #Se usará codigo de las anteriores practicas.
import http.client
import json


SERVER = "api.fda.gov"
RESOURCE = "/drug/label.json?limit=10"
PORT = int(input("Usuario introduzca el número del puerto: "))
if PORT <=1023 or  PORT >= 65536:   #Entre esos valores, no se puede establecer ningún puerto ya que no existen o estan reservados.
    print("Error usando el puerto")
else:
    def medicamento_pedir():
        lista_medicamentos=[] #Creamos una lista donde estarán todos los medicamentos pedidos.
        headers = {'User-Agent': 'http-client'}
        conexion = http.client.HTTPSConnection(SERVER)
        conexion.request("GET", RESOURCE, None, headers)
        r1 = conexion.getresponse()
        if r1.status == 404:
            print("Atencion usuario, Recurso: {} no existe o no encontrado".format(RESOURCE))
            exit(1)
        else:
            label= r1.read().decode("utf-8")
            conexion.close()
            info = json.loads(label)
            for i in range(len(info['results'])): #La longitud es de 10 debido al parametro del recurso
                info_medicamento = info['results'][i]
                if  (info_medicamento['openfda']):
                    #Si existe añadiremos el nombre genérico del medicamento
                    lista_medicamentos.append(info_medicamento['openfda']['generic_name'][0]) #Añades medicamentos a la lista.
                else:
                    lista_medicamentos.append("No se encuentra el nombre generico del medicamento")
            return lista_medicamentos #Te devuelve la lista con los medicamentos.

#Usamos el método de la herencia
    class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

        def do_GET(self):#aplicaremos el método GET
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            lista=medicamento_pedir()#Variable con todos los medicamentos recogidos por la función.
            content = "<html><body style='background-color: green'><ul>"

            #creamos el html
            content += "<h1>" + 'La lista de medicamentos es la siguiente: ' + "</h1>"
            content +="<img src ='http://www.openbiomedical.org/wordpress/wp-content/uploads/2015/09/openfda_logo.jpg' >"
            for medicamento in lista:#recorro la lista donde se han añadido los medicamentos.
                content+="<li>"+medicamento+'</li>'#creamos una lista en html.
            content+= "<a href ='https://open.fda.gov/'>Para mas informacion pincha aqui </a>"
            content+="</ul></body></html>"
            self.wfile.write(bytes(content,'utf8')) #Contestas a la peticion que recibes y le devuelves el contenido
            return



    Handler = testHTTPRequestHandler   #Handler llevará a cabo lo que hemos aplicado en la clase
    httpd = socketserver.TCPServer(("", PORT), Handler) #Se crea una conexion con el puerto indicado previamente.
    print("Sirviendo en el puerto: ", PORT)

    try:
        httpd.serve_forever()  #Creas un servidor para siempre


    except KeyboardInterrupt:   #Except en caso de que el usuario pare el servidor,

        print("El usuario ha interrumpido el servidor en el puerto:", PORT)
        print("Reanudelo de nuevo")

    print("Servidor parado")
    httpd.server_close()







