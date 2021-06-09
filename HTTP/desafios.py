import requests
r = requests.get("https://macowins-server.herokuapp.com/prendas/1")
print(r.json())
#{'id': 1, 'tipo': 'pantalon', 'talle': 35}
#es un diccionario
datos = r.json()
for clave, valor in datos.items():
    print (clave, valor)
#id 1
#tipo pantalon
#talle 35

#🏅 DESAFIO I: Hacé otro pedido para traer a la prenda 20. Deberías obtener el siguiente resultado:
#{
#  "id": 20,
#  "tipo": "saco",
#  "talle": "XL"
#}
r2 = requests.get("https://macowins-server.herokuapp.com/prendas/20")
print(r2.json())
#{'id': 20, 'tipo': 'saco', 'talle': 'XL'}

#2. CODIGOS DE RESPUESTA
#Desafío II: ¡averigualo! Hacé requests.get('https://macowins-server.herokuapp.com/prendas/400') y observá qué sucede.
r3 = requests.get('https://macowins-server.herokuapp.com/prendas/400')
#print(r3.json())
#salta un error
print(r3.status_code) #404: error, no encuentra el recurso que estaba buscando, no se pudo hacer bien el pedido
print(r3.headers) #metada sobre el pedido
#{'Server': 'Cowboy', 
#'Connection': 'keep-alive', 
#'X-Powered-By': 'Express', 
#'Expires': '-1', 
#'Content-Type': 'text/html; charset=utf-8', 
#'Content-Length': '0',
#'Etag': 'W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"', 
#'Vary': 'Accept-Encoding',
#'Date': 'Sat, 27 Feb 2021 19:14:21 GMT', 
#'Via': '1.1 vegur'}

#🏅 Desafío III: contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?
#🤔 Para pensar: ¿Qué cambió? ¿Qué cambio o cambios te parecen relevates entre ambas respuestas? ¿Qué emoji le pondrías a esta respuesta?
print(r.headers)
#{'Server': 'Cowboy', 
#'Connection': 'keep-alive', 
#'X-Powered-By': 'Express', 
#'Expires': '-1', 
#'Content-Type': 'application/json; charset=utf-8', 
#'Content-Length': '50', 
#'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 
#'Vary': 'Accept-Encoding', 'Date': 'Sat, 27 Feb 2021 18:11:12 GMT',
#'Via': '1.1 vegur'}
print(r.status_code) #200, todo OK :) 

#🏅 Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo https://macowins-server.herokuapp.com/prindas/1? ¡Averigualo!
r4 = requests.get('https://macowins-server.herokuapp.com/prindas/1')
print(r4.status_code) #404 tambien.

r5 = requests.get("https://macowins-server.herokuapp.com/nueva-funcionalidad-que-a-veces-no-anda-bien")
print(r5.status_code) #500. Un mensaje de error genérico, dado cuando se encontró una condición inesperada y no es adecuado ningún mensaje más específico.
print(r5.headers)
#{'Server': 'Cowboy', 
#'Connection': 'keep-alive',
# 'X-Powered-By': 'Express', 
# 'Vary': 'Origin, Accept-Encoding', 
# 'Access-Control-Allow-Credentials': 'true', 
# 'Cache-Control': 'no-cache', 
# 'Pragma': 'no-cache', 
# 'Expires': '-1', 
# 'Content-Security-Policy': "default-src 'none'", 
# 'X-Content-Type-Options': 'nosniff',
# 'Content-Type': 'text/html; charset=utf-8', 
# 'Content-Length': '148', 
# 'Date': 'Mon, 01 Mar 2021 20:18:38 GMT', 
# 'Via': '1.1 vegur'}
print(r5.content)
#b'<!DOCTYPE html>
#  <html lang="en">
#      <head>
#      <meta charset="utf-8">
#        <title>Error</title>
#      </head>
#      <body>
#        <pre>Internal Server Error</pre>
#      </body>
#  </html>'

#3. PARAMETROS
#Hagamos un nuevo pedido, pero ahora a una ruta ligeramente diferente:
#🤔 Para pensar: ¿es lo mismo consultar /prendas/ que /prendas/1? ¿En qué se diferencian? ¿Qué ocurre si hacemos r.content? ¿Por qué?
r5 = requests.get("https://macowins-server.herokuapp.com/prendas")
print(type(r5.json())) #-> es una lista con diccionarios adentro de cada prenda
for i in r5.json():
    print(i)
#{'id': 1, 'tipo': 'pantalon', 'talle': 35}
#{'id': 2, 'tipo': 'pantalon', 'talle': 36}
#{'id': 3, 'tipo': 'pantalon', 'talle': 37}
#{'id': 4, 'tipo': 'pantalon', 'talle': 38}
#{'id': 5, 'tipo': 'pantalon', 'talle': 39}
#{'id': 6, 'tipo': 'pantalon', 'talle': 40}
#{'id': 7, 'tipo': 'pantalon', 'talle': 41}
#{'id': 8, 'tipo': 'pantalon', 'talle': 42}
#{'id': 9, 'tipo': 'pantalon', 'talle': 43}
#{'id': 10, 'tipo': 'pantalon', 'talle': 44}
#{'id': 11, 'tipo': 'remera', 'talle': 'XS'}
#{'id': 12, 'tipo': 'remera', 'talle': 'S'}
#{'id': 13, 'tipo': 'remera', 'talle': 'M'}
#{'id': 14, 'tipo': 'remera', 'talle': 'L'}
#{'id': 15, 'tipo': 'remera', 'talle': 'XL'}
#{'id': 16, 'tipo': 'saco', 'talle': 'XS'}
#{'id': 17, 'tipo': 'saco', 'talle': 'S'}
#{'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}
#{'id': 19, 'tipo': 'saco', 'talle': 'L'}
#{'id': 20, 'tipo': 'saco', 'talle': 'XL'}
print(r5.status_code) #200
info = r.headers
for clave, valor in info.items():
    print (clave, valor)
#Server Cowboy
#Connection keep-alive
#X-Powered-By Express
#Expires -1
#Content-Type application/json; charset=utf-8
#Etag W/"4eb-TC9HXwiZ/qnCJXcle3sd76elfpU"
#Vary Accept-Encoding
#Content-Encoding gzip
#Date Tue, 18 May 2021 23:29:55 GMT
#Transfer-Encoding chunked
#Via 1.1 vegur
print(r.content)
#b'[\n  {\n    "id": 1,\n    "tipo": "pantalon",\n    "talle": 35\n  },\n  {\n    "id": 2,\n    "tipo": "pantalon",\n    "talle": 36\n  },\n  {\n    "id": 3,\n    "tipo": "pantalon",\n    "talle": 37\n  },\n  {\n    "id": 4,\n    "tipo": "pantalon",\n    "talle": 38\n  },\n  {\n    "id": 5,\n    "tipo": "pantalon",\n    "talle": 39\n  },\n  {\n   
# "id": 6,\n    "tipo": "pantalon",\n    "talle": 40\n  },\n  {\n    "id": 7,\n    "tipo": "pantalon",\n    "talle": 
#41\n  },\n  {\n    "id": 8,\n    "tipo": "pantalon",\n    
#"talle": 42\n  },\n  {\n    "id": 9,\n    "tipo": "pantalon",\n    "talle": 43\n  },\n  {\n    "id": 10,\n    "tipo": "pantalon",\n    "talle": 44\n  },\n  {\n    "id": 11,\n    "tipo": "remera",\n    "talle": "XS"\n  },\n  {\n    "id": 12,\n    "tipo": "remera",\n    "talle": "S"\n  },\n 
# {\n    "id": 13,\n    "tipo": "remera",\n    "talle": "M"\n  },\n  {\n    "id": 14,\n    "tipo": "remera",\n    "talle": "L"\n  },\n  {\n    "id": 15,\n    "tipo": "remera",\n    "talle": "XL"\n  },\n  {\n    "id": 16,\n    "tipo": "saco",\n    "talle": "XS"\n  },\n  {\n    "id": 17,\n   
# "tipo": "saco",\n    "talle": "S"\n  },\n  {\n    "id": 18,\n    "tipo": "saco",\n    "talle": "M",\n    "enStock": false\n  },\n  {\n    "id": 19,\n    "tipo": "saco",\n   
# "talle": "L"\n  },\n  {\n    "id": 20,\n    "tipo": "saco",\n    "talle": "XL"\n  }\n]'

#r = requests.get("https://macowins-server.herokuapp.com/prendas/1") #estamos consultando el primer diccionanrio de la lista
#print(r.json())
#{'id': 1, 'tipo': 'pantalon', 'talle': 35}

#🤔 Para pensar: ¿qué hará /ventas/2? ¿/ventas/?.
r6 = requests.get("https://macowins-server.herokuapp.com/ventas") #3me da todas las ventas
print(type(r6.json())) #es una lista
for i in r6.json(): # i es cada diccionario de la lista 
    for clave, valor in i.items():
        print(clave, valor)
#id 169
#producto {'id': 11, 'tipo': 'remera', 'talle': 'XS'}      
#fecha 1987-03-24T20:52:48.000Z
#id 170
#producto {'id': 14, 'tipo': 'remera', 'talle': 'L'}       
#fecha 1987-05-01T02:24:00.000Z

r7 = requests.get("https://macowins-server.herokuapp.com/ventas/2")#me da la venta con id 2
print(type(r7.json())) #diccionario
for clave, valor in r7.json().items():
    print(clave, valor)
#id 2
#producto {'id': 17, 'tipo': 'saco', 'talle': 'S'}
#fecha 1970-03-16T11:02:24.000Z
print(r7.json())

r8 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon")
for i in r8.json():
    for clave, valor in i.items():
        print(clave, valor)
#id 1
#tipo pantalon
#talle 35
#id 2
#tipo pantalon
#talle 36
#id 3
#tipo pantalon
#talle 37
#id 4
#tipo pantalon
#talle 38
#id 5
#tipo pantalon
#talle 39
#id 6
#tipo pantalon
#talle 40
#id 7
#tipo pantalon
#talle 41
#id 8
#tipo pantalon
#talle 42
#id 9
#tipo pantalon
#talle 43
#id 10
#tipo pantalon
#talle 44

r9 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=saco")
for i in r9.json():
    for clave, valor in i.items():
        print(clave, valor)
#id 16
#tipo saco
#talle XS
#id 17
#tipo saco
#talle S
#id 18
#tipo saco
#talle M
#enStock False
#id 19
#tipo saco
#talle L
#id 20
#tipo saco
#talle XL

#🏅 Desafío VI: Obtené las remeras.
r10 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=remera")
for i in r10.json():
    for clave, valor in i.items():
        print(clave, valor)
#tipo remera
#talle XS
#id 12
#tipo remera
#talle S
#id 13
#tipo remera
#talle M
#id 14
#tipo remera
#talle L
#id 15
#tipo remera
#talle XL

r11 = requests.get("https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon")
for i in r11.json():
    for clave, valor in i.items():
        print(clave, valor)
#id 6
#tipo pantalon
#talle 40

#🏅 Desafío VII: Obtené las remeras XS
r12 = requests.get("https://macowins-server.herokuapp.com/prendas?talle=XS&tipo=remera")
for i in r12.json():
    for clave, valor in i.items():
        print(clave, valor)
#id 11
#tipo remera
#talle XS

'''
🤔 Para pensar: ¿cuál es el protocolo que estamos estudiando? ¿Se observa en las URLs que venimos mencionando?
#HTTP (HyperText Transfer Protocol) es el protocolo que venimos estudiando. Se observa en las URLs que venimos mencionando. 

HTTP/1.1 200 OK
X-Powered-By: Express
Vary: Origin, Accept-Encoding
Access-Control-Allow-Credentials: true
Cache-Control: no-cache
Pragma: no-cache
Expires: -1
X-Total-Count: 100
Access-Control-Expose-Headers: X-Total-Count, Link
Link: <https://macowins-server.herokuapp.com/posts/?_page=1>; rel="first", <https://macowins-server.herokuapp.com/posts/?_page=2>; rel="next", <https://macowins-server.herokuapp.com/posts/?_page=10>; rel="last"
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Content-Length: 794
ETag: W/"31a-kfX25hKekB1DHqT0GE68BdzBP1Q"
Date: Sun, 19 Apr 2020 20:18:21 GMT
Connection: keep-alive
🤔 Para pensar: ¿Cuál fue el Content-Type de las respuesta del ejemplo? ¿Por qué devolvió eso?
Content-Type: application/json; charset=utf-8

POST

>>> data = {'id': 21}
>>>  r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
🏅 Desafío XII: ¿qué código de estado devuelve cuando un recurso es creado? Averigualo
201. CREATED


#🏅 Desafío: Nos quedaron prendas con ids que no nos sirven; ¡borralas!
#🏅 Desafío XIII: Creá una venta.
data = {
  "id": 501,
  "producto": {
    "id": 8,
    "tipo": "pantalon",
    "talle": 42
  },
  "fecha": "2021-05-16T11:02:24.000Z"
}
r = requests.post("https://macowins-server.herokuapp.com/ventas", data=data)
'''

#🏅 Desafío XIV: Intentá hacer POST sobre una venta concreta, como por ejemplo https://macowins-server.herokuapp.com/prendas/1. ¿Qué sucede?
r13 = requests.post("https://macowins-server.herokuapp.com/prendas/1")
print(r13.status_code)#404
print(r13.json()) #tira error
#no se puede, el post se podria hacer sobre prendas, le tenemos que decir que vamos a agregar
#ej 
#data = {'id':21}
#r = requests.post("https://macowins-server.herokuapp.com/prendas", data=data)
