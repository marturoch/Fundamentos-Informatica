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
#Ventas/2 devolvera la venta con id numero 2 y ventas devolvera todas las ventas.
#Desafío V: hacé requests.get('https://macowins-server.herokuapp.com/ventas') y 
#requests.get('https://macowins-server.herokuapp.com/ventas/2)' y contrastá el resultado con
#tu respuesta anterior
r6 = requests.get("https://macowins-server.herokuapp.com/ventas") #3me da todas las ventas
print(type(r6.json())) #es una lista
'''
[{'id': 1, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1970-02-07T05:31:12.000Z'}, {'id': 2, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1970-03-16T11:02:24.000Z'}, {'id': 3, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1970-04-22T16:33:36.000Z'}, {'id': 4, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1970-05-29T22:04:48.000Z'}, {'id': 5, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '1970-07-06T03:36:00.000Z'}, {'id': 6, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1970-08-12T09:07:12.000Z'}, {'id': 7, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1970-09-18T14:38:24.000Z'}, {'id': 8, 'producto': {'id': 4, 'tipo': 
'pantalon', 'talle': 38}, 'fecha': '1970-10-25T20:09:36.000Z'}, {'id': 
9, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1970-12-02T01:40:48.000Z'}, {'id': 10, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '1971-01-08T07:12:00.000Z'}, {'id': 11, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1971-02-14T12:43:12.000Z'}, {'id': 12, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1971-03-23T18:14:24.000Z'}, {'id': 13, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1971-04-29T23:45:36.000Z'}, {'id': 14, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1971-06-06T05:16:48.000Z'}, {'id': 15, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1971-07-13T10:48:00.000Z'}, {'id': 16, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1971-08-19T16:19:12.000Z'}, {'id': 17, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1971-09-25T21:50:24.000Z'}, {'id': 18, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1971-11-02T03:21:36.000Z'}, {'id': 19, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1971-12-09T08:52:48.000Z'}, {'id': 20, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1972-01-15T14:24:00.000Z'}, {'id': 21, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1972-02-21T19:55:12.000Z'}, {'id': 22, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1972-03-30T01:26:24.000Z'}, {'id': 23, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1972-05-06T06:57:36.000Z'}, {'id': 24, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1972-06-12T12:28:48.000Z'}, {'id': 25, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1972-07-19T18:00:00.000Z'}, {'id': 26, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1972-08-25T23:31:12.000Z'}, {'id': 27, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1972-10-02T05:02:24.000Z'}, {'id': 28, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1972-11-08T10:33:36.000Z'}, {'id': 29, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1972-12-15T16:04:48.000Z'}, {'id': 30, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1973-01-21T21:36:00.000Z'}, {'id': 31, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1973-02-28T03:07:12.000Z'}, {'id': 32, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1973-04-06T08:38:24.000Z'}, {'id': 33, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1973-05-13T14:09:36.000Z'}, {'id': 34, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1973-06-19T19:40:48.000Z'}, {'id': 35, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1973-07-27T01:12:00.000Z'}, {'id': 36, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1973-09-02T06:43:12.000Z'}, {'id': 37, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1973-10-09T12:14:24.000Z'}, {'id': 38, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1973-11-15T17:45:36.000Z'}, {'id': 39, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1973-12-22T23:16:48.000Z'}, {'id': 40, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1974-01-29T04:48:00.000Z'}, {'id': 41, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1974-03-07T10:19:12.000Z'}, {'id': 42, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1974-04-13T15:50:24.000Z'}, {'id': 43, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1974-05-20T21:21:36.000Z'}, {'id': 44, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1974-06-27T02:52:48.000Z'}, {'id': 45, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1974-08-03T08:24:00.000Z'}, {'id': 46, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1974-09-09T13:55:12.000Z'}, {'id': 47, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1974-10-16T19:26:24.000Z'}, {'id': 48, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1974-11-23T00:57:36.000Z'}, {'id': 49, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1974-12-30T06:28:48.000Z'}, {'id': 50, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1975-02-05T12:00:00.000Z'}, {'id': 51, 
'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1975-03-14T17:31:12.000Z'}, {'id': 52, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1975-04-20T23:02:24.000Z'}, {'id': 53, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1975-05-28T04:33:36.000Z'}, {'id': 54, 'producto': {'id': 18, 
'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1975-07-04T10:04:48.000Z'}, {'id': 55, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1975-08-10T15:36:00.000Z'}, {'id': 56, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1975-09-16T21:07:12.000Z'}, {'id': 57, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1975-10-24T02:38:24.000Z'}, {'id': 58, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1975-11-30T08:09:36.000Z'}, {'id': 59, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1976-01-06T13:40:48.000Z'}, {'id': 60, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1976-02-12T19:12:00.000Z'}, {'id': 61, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1976-03-21T00:43:12.000Z'}, {'id': 62, 'producto': {'id': 
17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1976-04-27T06:14:24.000Z'}, {'id': 63, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1976-06-03T11:45:36.000Z'}, {'id': 64, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1976-07-10T17:16:48.000Z'}, {'id': 65, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1976-08-16T22:48:00.000Z'}, {'id': 66, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1976-09-23T04:19:12.000Z'}, {'id': 67, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1976-10-30T09:50:24.000Z'}, {'id': 68, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1976-12-06T15:21:36.000Z'}, {'id': 69, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': 
'1977-01-12T20:52:48.000Z'}, {'id': 70, 'producto': {'id': 19, 'tipo': 
'saco', 'talle': 'L'}, 'fecha': '1977-02-19T02:24:00.000Z'}, {'id': 71, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1977-03-28T07:55:12.000Z'}, {'id': 72, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1977-05-04T13:26:24.000Z'}, {'id': 73, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1977-06-10T18:57:36.000Z'}, {'id': 74, 'producto': {'id': 16, 'tipo': 'saco', 
'talle': 'XS'}, 'fecha': '1977-07-18T00:28:48.000Z'}, {'id': 75, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1977-08-24T06:00:00.000Z'}, {'id': 76, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1977-09-30T11:31:12.000Z'}, {'id': 77, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1977-11-06T17:02:24.000Z'}, {'id': 78, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1977-12-13T22:33:36.000Z'}, {'id': 79, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1978-01-20T04:04:48.000Z'}, {'id': 80, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1978-02-26T09:36:00.000Z'}, {'id': 81, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1978-04-04T15:07:12.000Z'}, {'id': 82, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1978-05-11T20:38:24.000Z'}, {'id': 83, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1978-06-18T02:09:36.000Z'}, {'id': 84, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1978-07-25T07:40:48.000Z'}, 
{'id': 85, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1978-08-31T13:12:00.000Z'}, {'id': 86, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1978-10-07T18:43:12.000Z'}, {'id': 87, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1978-11-14T00:14:24.000Z'}, {'id': 88, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1978-12-21T05:45:36.000Z'}, {'id': 
89, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1979-01-27T11:16:48.000Z'}, {'id': 90, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1979-03-05T16:48:00.000Z'}, {'id': 91, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1979-04-11T22:19:12.000Z'}, {'id': 92, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1979-05-19T03:50:24.000Z'}, {'id': 93, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1979-06-25T09:21:36.000Z'}, {'id': 94, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1979-08-01T14:52:48.000Z'}, 
{'id': 95, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1979-09-07T20:24:00.000Z'}, {'id': 96, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1979-10-15T01:55:12.000Z'}, {'id': 97, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1979-11-21T07:26:24.000Z'}, {'id': 98, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1979-12-28T12:57:36.000Z'}, {'id': 99, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': 
'1980-02-03T18:28:48.000Z'}, {'id': 100, 'producto': {'id': 7, 'tipo': 
'pantalon', 'talle': 41}, 'fecha': '1980-03-12T00:00:00.000Z'}, {'id': 
101, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '1980-04-18T05:31:12.000Z'}, {'id': 102, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1980-05-25T11:02:24.000Z'}, {'id': 103, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1980-07-01T16:33:36.000Z'}, {'id': 104, 'producto': {'id': 
2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1980-08-07T22:04:48.000Z'}, {'id': 105, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1980-09-14T03:36:00.000Z'}, {'id': 106, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1980-10-21T09:07:12.000Z'}, {'id': 107, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1980-11-27T14:38:24.000Z'}, {'id': 108, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1981-01-03T20:09:36.000Z'}, {'id': 109, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1981-02-10T01:40:48.000Z'}, {'id': 110, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1981-03-19T07:12:00.000Z'}, {'id': 111, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1981-04-25T12:43:12.000Z'}, {'id': 112, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1981-06-01T18:14:24.000Z'}, {'id': 113, 'producto': {'id': 1, 'tipo': 'pantalon', 
'talle': 35}, 'fecha': '1981-07-08T23:45:36.000Z'}, {'id': 114, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1981-08-15T05:16:48.000Z'}, {'id': 115, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1981-09-21T10:48:00.000Z'}, {'id': 116, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1981-10-28T16:19:12.000Z'}, {'id': 117, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1981-12-04T21:50:24.000Z'}, {'id': 118, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1982-01-11T03:21:36.000Z'}, {'id': 119, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1982-02-17T08:52:48.000Z'}, {'id': 120, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1982-03-26T14:24:00.000Z'}, {'id': 121, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1982-05-02T19:55:12.000Z'}, {'id': 122, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': 
'1982-06-09T01:26:24.000Z'}, {'id': 123, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1982-07-16T06:57:36.000Z'}, {'id': 124, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1982-08-22T12:28:48.000Z'}, {'id': 125, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1982-09-28T18:00:00.000Z'}, {'id': 126, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '1982-11-04T23:31:12.000Z'}, {'id': 127, 'producto': {'id': 13, 'tipo': 
'remera', 'talle': 'M'}, 'fecha': '1982-12-12T05:02:24.000Z'}, {'id': 128, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1983-01-18T10:33:36.000Z'}, {'id': 129, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1983-02-24T16:04:48.000Z'}, {'id': 130, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1983-04-02T21:36:00.000Z'}, {'id': 131, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1983-05-10T03:07:12.000Z'}, {'id': 132, 
'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1983-06-16T08:38:24.000Z'}, {'id': 133, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1983-07-23T14:09:36.000Z'}, {'id': 134, 
'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1983-08-29T19:40:48.000Z'}, {'id': 135, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1983-10-06T01:12:00.000Z'}, {'id': 136, 
'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1983-11-12T06:43:12.000Z'}, {'id': 137, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1983-12-19T12:14:24.000Z'}, {'id': 138, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1984-01-25T17:45:36.000Z'}, {'id': 139, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1984-03-02T23:16:48.000Z'}, {'id': 140, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '1984-04-09T04:48:00.000Z'}, {'id': 141, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1984-05-16T10:19:12.000Z'}, {'id': 142, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1984-06-22T15:50:24.000Z'}, {'id': 143, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1984-07-29T21:21:36.000Z'}, 
{'id': 144, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1984-09-05T02:52:48.000Z'}, {'id': 145, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1984-10-12T08:24:00.000Z'}, {'id': 146, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1984-11-18T13:55:12.000Z'}, {'id': 147, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1984-12-25T19:26:24.000Z'}, {'id': 148, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1985-02-01T00:57:36.000Z'}, {'id': 149, 'producto': 
{'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1985-03-10T06:28:48.000Z'}, {'id': 150, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1985-04-16T12:00:00.000Z'}, {'id': 151, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1985-05-23T17:31:12.000Z'}, {'id': 152, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1985-06-29T23:02:24.000Z'}, {'id': 153, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1985-08-06T04:33:36.000Z'}, {'id': 154, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1985-09-12T10:04:48.000Z'}, {'id': 155, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1985-10-19T15:36:00.000Z'}, {'id': 156, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1985-11-25T21:07:12.000Z'}, {'id': 157, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1986-01-02T02:38:24.000Z'}, {'id': 158, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1986-02-08T08:09:36.000Z'}, {'id': 159, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '1986-03-17T13:40:48.000Z'}, {'id': 160, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 
'fecha': '1986-04-23T19:12:00.000Z'}, {'id': 161, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1986-05-31T00:43:12.000Z'}, {'id': 162, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 
'fecha': '1986-07-07T06:14:24.000Z'}, {'id': 163, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1986-08-13T11:45:36.000Z'}, {'id': 164, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1986-09-19T17:16:48.000Z'}, {'id': 165, 'producto': {'id': 3, 
'tipo': 'pantalon', 'talle': 37}, 'fecha': '1986-10-26T22:48:00.000Z'}, {'id': 166, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1986-12-03T04:19:12.000Z'}, {'id': 167, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1987-01-09T09:50:24.000Z'}, {'id': 168, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1987-02-15T15:21:36.000Z'}, {'id': 169, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1987-03-24T20:52:48.000Z'}, 
{'id': 170, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1987-05-01T02:24:00.000Z'}, {'id': 171, 'producto': {'id': 14, 
'tipo': 'remera', 'talle': 'L'}, 'fecha': '1987-06-07T07:55:12.000Z'}, 
{'id': 172, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1987-07-14T13:26:24.000Z'}, {'id': 173, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '1987-08-20T18:57:36.000Z'}, {'id': 174, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1987-09-27T00:28:48.000Z'}, {'id': 175, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1987-11-03T06:00:00.000Z'}, {'id': 176, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1987-12-10T11:31:12.000Z'}, {'id': 177, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1988-01-16T17:02:24.000Z'}, {'id': 178, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1988-02-22T22:33:36.000Z'}, {'id': 179, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1988-03-31T04:04:48.000Z'}, {'id': 180, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1988-05-07T09:36:00.000Z'}, {'id': 181, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1988-06-13T15:07:12.000Z'}, {'id': 182, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': 
'1988-07-20T20:38:24.000Z'}, {'id': 183, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1988-08-27T02:09:36.000Z'}, {'id': 184, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1988-10-03T07:40:48.000Z'}, {'id': 185, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1988-11-09T13:12:00.000Z'}, {'id': 186, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1988-12-16T18:43:12.000Z'}, {'id': 187, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1989-01-23T00:14:24.000Z'}, {'id': 188, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '1989-03-01T05:45:36.000Z'}, {'id': 189, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1989-04-07T11:16:48.000Z'}, {'id': 190, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1989-05-14T16:48:00.000Z'}, {'id': 191, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1989-06-20T22:19:12.000Z'}, {'id': 192, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '1989-07-28T03:50:24.000Z'}, {'id': 193, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1989-09-03T09:21:36.000Z'}, {'id': 194, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1989-10-10T14:52:48.000Z'}, {'id': 195, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1989-11-16T20:24:00.000Z'}, {'id': 196, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1989-12-24T01:55:12.000Z'}, {'id': 197, 'producto': {'id': 2, 'tipo': 'pantalon', 
'talle': 36}, 'fecha': '1990-01-30T07:26:24.000Z'}, {'id': 198, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1990-03-08T12:57:36.000Z'}, {'id': 199, 'producto': {'id': 2, 'tipo': 'pantalon', 
'talle': 36}, 'fecha': '1990-04-14T18:28:48.000Z'}, {'id': 200, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1990-05-22T00:00:00.000Z'}, {'id': 201, 'producto': {'id': 8, 'tipo': 'pantalon', 
'talle': 42}, 'fecha': '1990-06-28T05:31:12.000Z'}, {'id': 202, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1990-08-04T11:02:24.000Z'}, {'id': 203, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1990-09-10T16:33:36.000Z'}, {'id': 204, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1990-10-17T22:04:48.000Z'}, {'id': 205, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1990-11-24T03:36:00.000Z'}, {'id': 206, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1990-12-31T09:07:12.000Z'}, {'id': 207, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '1991-02-06T14:38:24.000Z'}, {'id': 208, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1991-03-15T20:09:36.000Z'}, {'id': 209, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1991-04-22T01:40:48.000Z'}, {'id': 210, 'producto': 
{'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1991-05-29T07:12:00.000Z'}, {'id': 211, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1991-07-05T12:43:12.000Z'}, {'id': 212, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1991-08-11T18:14:24.000Z'}, {'id': 213, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1991-09-17T23:45:36.000Z'}, {'id': 214, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1991-10-25T05:16:48.000Z'}, {'id': 215, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 
'L'}, 'fecha': '1991-12-01T10:48:00.000Z'}, {'id': 216, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1992-01-07T16:19:12.000Z'}, {'id': 217, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1992-02-13T21:50:24.000Z'}, {'id': 218, 
'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1992-03-22T03:21:36.000Z'}, {'id': 219, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1992-04-28T08:52:48.000Z'}, {'id': 220, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1992-06-04T14:24:00.000Z'}, {'id': 221, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1992-07-11T19:55:12.000Z'}, {'id': 222, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1992-08-18T01:26:24.000Z'}, {'id': 223, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1992-09-24T06:57:36.000Z'}, {'id': 224, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1992-10-31T12:28:48.000Z'}, {'id': 225, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1992-12-07T18:00:00.000Z'}, {'id': 226, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1993-01-13T23:31:12.000Z'}, {'id': 227, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1993-02-20T05:02:24.000Z'}, {'id': 228, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1993-03-29T10:33:36.000Z'}, {'id': 229, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1993-05-05T16:04:48.000Z'}, {'id': 230, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1993-06-11T21:36:00.000Z'}, {'id': 231, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1993-07-19T03:07:12.000Z'}, {'id': 
232, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1993-08-25T08:38:24.000Z'}, {'id': 233, 'producto': {'id': 19, 'tipo': 
'saco', 'talle': 'L'}, 'fecha': '1993-10-01T14:09:36.000Z'}, {'id': 234, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1993-11-07T19:40:48.000Z'}, {'id': 235, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1993-12-15T01:12:00.000Z'}, {'id': 236, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1994-01-21T06:43:12.000Z'}, {'id': 237, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '1994-02-27T12:14:24.000Z'}, {'id': 238, 
'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1994-04-05T17:45:36.000Z'}, {'id': 239, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1994-05-12T23:16:48.000Z'}, {'id': 240, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1994-06-19T04:48:00.000Z'}, {'id': 241, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1994-07-26T10:19:12.000Z'}, {'id': 242, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1994-09-01T15:50:24.000Z'}, {'id': 243, 'producto': {'id': 17, 'tipo': 'saco', 
'talle': 'S'}, 'fecha': '1994-10-08T21:21:36.000Z'}, {'id': 244, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1994-11-15T02:52:48.000Z'}, {'id': 245, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1994-12-22T08:24:00.000Z'}, {'id': 246, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '1995-01-28T13:55:12.000Z'}, {'id': 247, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1995-03-06T19:26:24.000Z'}, {'id': 248, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1995-04-13T00:57:36.000Z'}, {'id': 249, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1995-05-20T06:28:48.000Z'}, {'id': 250, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1995-06-26T12:00:00.000Z'}, {'id': 251, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1995-08-02T17:31:12.000Z'}, {'id': 252, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1995-09-08T23:02:24.000Z'}, {'id': 253, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1995-10-16T04:33:36.000Z'}, {'id': 254, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1995-11-22T10:04:48.000Z'}, {'id': 255, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '1995-12-29T15:36:00.000Z'}, {'id': 256, 'producto': {'id': 
10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1996-02-04T21:07:12.000Z'}, {'id': 257, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '1996-03-13T02:38:24.000Z'}, {'id': 258, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1996-04-19T08:09:36.000Z'}, {'id': 259, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1996-05-26T13:40:48.000Z'}, {'id': 260, 'producto': {'id': 
3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1996-07-02T19:12:00.000Z'}, {'id': 261, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1996-08-09T00:43:12.000Z'}, {'id': 262, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '1996-09-15T06:14:24.000Z'}, {'id': 263, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1996-10-22T11:45:36.000Z'}, {'id': 264, 'producto': {'id': 14, 
'tipo': 'remera', 'talle': 'L'}, 'fecha': '1996-11-28T17:16:48.000Z'}, 
{'id': 265, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1997-01-04T22:48:00.000Z'}, {'id': 266, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1997-02-11T04:19:12.000Z'}, 
{'id': 267, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1997-03-20T09:50:24.000Z'}, {'id': 268, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '1997-04-26T15:21:36.000Z'}, {'id': 269, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1997-06-02T20:52:48.000Z'}, {'id': 270, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1997-07-10T02:24:00.000Z'}, {'id': 271, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1997-08-16T07:55:12.000Z'}, {'id': 272, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '1997-09-22T13:26:24.000Z'}, {'id': 273, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1997-10-29T18:57:36.000Z'}, {'id': 274, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1997-12-06T00:28:48.000Z'}, {'id': 275, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1998-01-12T06:00:00.000Z'}, {'id': 276, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '1998-02-18T11:31:12.000Z'}, {'id': 277, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': 
'1998-03-27T17:02:24.000Z'}, {'id': 278, 'producto': {'id': 9, 'tipo': 
'pantalon', 'talle': 43}, 'fecha': '1998-05-03T22:33:36.000Z'}, {'id': 
279, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': 
'1998-06-10T04:04:48.000Z'}, {'id': 280, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '1998-07-17T09:36:00.000Z'}, {'id': 281, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1998-08-23T15:07:12.000Z'}, {'id': 282, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '1998-09-29T20:38:24.000Z'}, {'id': 283, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '1998-11-06T02:09:36.000Z'}, {'id': 284, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '1998-12-13T07:40:48.000Z'}, {'id': 285, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '1999-01-19T13:12:00.000Z'}, {'id': 286, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '1999-02-25T18:43:12.000Z'}, {'id': 287, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1999-04-04T00:14:24.000Z'}, {'id': 288, 'producto': {'id': 
6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '1999-05-11T05:45:36.000Z'}, {'id': 289, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '1999-06-17T11:16:48.000Z'}, {'id': 290, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '1999-07-24T16:48:00.000Z'}, {'id': 291, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 
'fecha': '1999-08-30T22:19:12.000Z'}, {'id': 292, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '1999-10-07T03:50:24.000Z'}, {'id': 293, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 
'fecha': '1999-11-13T09:21:36.000Z'}, {'id': 294, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '1999-12-20T14:52:48.000Z'}, {'id': 295, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2000-01-26T20:24:00.000Z'}, {'id': 296, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2000-03-04T01:55:12.000Z'}, {'id': 297, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '2000-04-10T07:26:24.000Z'}, {'id': 298, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2000-05-17T12:57:36.000Z'}, {'id': 299, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '2000-06-23T18:28:48.000Z'}, {'id': 300, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2000-07-31T00:00:00.000Z'}, {'id': 301, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2000-09-06T05:31:12.000Z'}, {'id': 302, 'producto': 
{'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2000-10-13T11:02:24.000Z'}, {'id': 303, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '2000-11-19T16:33:36.000Z'}, {'id': 304, 'producto': 
{'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2000-12-26T22:04:48.000Z'}, {'id': 305, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '2001-02-02T03:36:00.000Z'}, {'id': 306, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '2001-03-11T09:07:12.000Z'}, {'id': 307, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2001-04-17T14:38:24.000Z'}, {'id': 308, 'producto': 
{'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2001-05-24T20:09:36.000Z'}, {'id': 309, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2001-07-01T01:40:48.000Z'}, {'id': 310, 'producto': 
{'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2001-08-07T07:12:00.000Z'}, {'id': 311, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2001-09-13T12:43:12.000Z'}, {'id': 312, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2001-10-20T18:14:24.000Z'}, {'id': 313, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2001-11-26T23:45:36.000Z'}, {'id': 314, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2002-01-03T05:16:48.000Z'}, {'id': 315, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2002-02-09T10:48:00.000Z'}, {'id': 316, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '2002-03-18T16:19:12.000Z'}, {'id': 317, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2002-04-24T21:50:24.000Z'}, {'id': 318, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '2002-06-01T03:21:36.000Z'}, {'id': 319, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2002-07-08T08:52:48.000Z'}, {'id': 320, 'producto': {'id': 
15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2002-08-14T14:24:00.000Z'}, {'id': 321, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 
'fecha': '2002-09-20T19:55:12.000Z'}, {'id': 322, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2002-10-28T01:26:24.000Z'}, {'id': 323, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2002-12-04T06:57:36.000Z'}, {'id': 324, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2003-01-10T12:28:48.000Z'}, {'id': 325, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2003-02-16T18:00:00.000Z'}, {'id': 326, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2003-03-25T23:31:12.000Z'}, {'id': 327, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2003-05-02T05:02:24.000Z'}, {'id': 328, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2003-06-08T10:33:36.000Z'}, {'id': 329, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2003-07-15T16:04:48.000Z'}, {'id': 330, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '2003-08-21T21:36:00.000Z'}, {'id': 331, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2003-09-28T03:07:12.000Z'}, {'id': 332, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2003-11-04T08:38:24.000Z'}, {'id': 333, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2003-12-11T14:09:36.000Z'}, {'id': 334, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2004-01-17T19:40:48.000Z'}, {'id': 335, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2004-02-24T01:12:00.000Z'}, {'id': 336, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2004-04-01T06:43:12.000Z'}, {'id': 337, 
'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '2004-05-08T12:14:24.000Z'}, {'id': 338, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2004-06-14T17:45:36.000Z'}, {'id': 339, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2004-07-21T23:16:48.000Z'}, {'id': 340, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2004-08-28T04:48:00.000Z'}, {'id': 341, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2004-10-04T10:19:12.000Z'}, {'id': 342, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2004-11-10T15:50:24.000Z'}, {'id': 343, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2004-12-17T21:21:36.000Z'}, {'id': 344, 'producto': {'id': 17, 'tipo': 'saco', 
'talle': 'S'}, 'fecha': '2005-01-24T02:52:48.000Z'}, {'id': 345, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2005-03-02T08:24:00.000Z'}, {'id': 346, 'producto': {'id': 2, 'tipo': 'pantalon', 
'talle': 36}, 'fecha': '2005-04-08T13:55:12.000Z'}, {'id': 347, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2005-05-15T19:26:24.000Z'}, {'id': 348, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2005-06-22T00:57:36.000Z'}, {'id': 349, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2005-07-29T06:28:48.000Z'}, {'id': 350, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2005-09-04T12:00:00.000Z'}, {'id': 351, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2005-10-11T17:31:12.000Z'}, {'id': 352, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '2005-11-17T23:02:24.000Z'}, {'id': 353, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2005-12-25T04:33:36.000Z'}, {'id': 354, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2006-01-31T10:04:48.000Z'}, {'id': 355, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2006-03-09T15:36:00.000Z'}, {'id': 356, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2006-04-15T21:07:12.000Z'}, {'id': 357, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '2006-05-23T02:38:24.000Z'}, {'id': 358, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2006-06-29T08:09:36.000Z'}, {'id': 359, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '2006-08-05T13:40:48.000Z'}, {'id': 360, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2006-09-11T19:12:00.000Z'}, {'id': 361, 'producto': 
{'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '2006-10-19T00:43:12.000Z'}, {'id': 362, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '2006-11-25T06:14:24.000Z'}, {'id': 363, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2007-01-01T11:45:36.000Z'}, {'id': 364, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2007-02-07T17:16:48.000Z'}, {'id': 365, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2007-03-16T22:48:00.000Z'}, {'id': 366, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2007-04-23T04:19:12.000Z'}, {'id': 367, 
'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2007-05-30T09:50:24.000Z'}, {'id': 368, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2007-07-06T15:21:36.000Z'}, {'id': 369, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2007-08-12T20:52:48.000Z'}, {'id': 370, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2007-09-19T02:24:00.000Z'}, {'id': 371, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2007-10-26T07:55:12.000Z'}, {'id': 372, 'producto': {'id': 5, 'tipo': 'pantalon', 
'talle': 39}, 'fecha': '2007-12-02T13:26:24.000Z'}, {'id': 373, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2008-01-08T18:57:36.000Z'}, {'id': 374, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '2008-02-15T00:28:48.000Z'}, {'id': 375, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2008-03-23T06:00:00.000Z'}, {'id': 376, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2008-04-29T11:31:12.000Z'}, {'id': 377, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2008-06-05T17:02:24.000Z'}, {'id': 378, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2008-07-12T22:33:36.000Z'}, {'id': 379, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2008-08-19T04:04:48.000Z'}, {'id': 380, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2008-09-25T09:36:00.000Z'}, {'id': 381, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2008-11-01T15:07:12.000Z'}, {'id': 382, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '2008-12-08T20:38:24.000Z'}, {'id': 383, 'producto': 
{'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2009-01-15T02:09:36.000Z'}, {'id': 384, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 
'M', 'enStock': False}, 'fecha': '2009-02-21T07:40:48.000Z'}, {'id': 385, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2009-03-30T13:12:00.000Z'}, {'id': 386, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2009-05-06T18:43:12.000Z'}, {'id': 387, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2009-06-13T00:14:24.000Z'}, {'id': 388, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2009-07-20T05:45:36.000Z'}, {'id': 389, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2009-08-26T11:16:48.000Z'}, {'id': 390, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2009-10-02T16:48:00.000Z'}, {'id': 391, 
'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2009-11-08T22:19:12.000Z'}, {'id': 392, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2009-12-16T03:50:24.000Z'}, {'id': 393, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2010-01-22T09:21:36.000Z'}, {'id': 394, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2010-02-28T14:52:48.000Z'}, {'id': 395, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2010-04-06T20:24:00.000Z'}, {'id': 396, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2010-05-14T01:55:12.000Z'}, {'id': 397, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '2010-06-20T07:26:24.000Z'}, {'id': 398, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2010-07-27T12:57:36.000Z'}, {'id': 399, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '2010-09-02T18:28:48.000Z'}, {'id': 400, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 
'M', 'enStock': False}, 'fecha': '2010-10-10T00:00:00.000Z'}, {'id': 401, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2010-11-16T05:31:12.000Z'}, {'id': 402, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2010-12-23T11:02:24.000Z'}, {'id': 403, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2011-01-29T16:33:36.000Z'}, {'id': 404, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2011-03-07T22:04:48.000Z'}, {'id': 405, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '2011-04-14T03:36:00.000Z'}, {'id': 406, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2011-05-21T09:07:12.000Z'}, {'id': 407, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2011-06-27T14:38:24.000Z'}, {'id': 408, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2011-08-03T20:09:36.000Z'}, {'id': 409, 
'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2011-09-10T01:40:48.000Z'}, {'id': 410, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2011-10-17T07:12:00.000Z'}, {'id': 411, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2011-11-23T12:43:12.000Z'}, {'id': 412, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '2011-12-30T18:14:24.000Z'}, {'id': 413, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '2012-02-05T23:45:36.000Z'}, {'id': 414, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2012-03-14T05:16:48.000Z'}, 
{'id': 415, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2012-04-20T10:48:00.000Z'}, {'id': 416, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2012-05-27T16:19:12.000Z'}, {'id': 417, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2012-07-03T21:50:24.000Z'}, {'id': 418, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2012-08-10T03:21:36.000Z'}, {'id': 419, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2012-09-16T08:52:48.000Z'}, {'id': 420, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2012-10-23T14:24:00.000Z'}, {'id': 421, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2012-11-29T19:55:12.000Z'}, {'id': 422, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2013-01-06T01:26:24.000Z'}, {'id': 423, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '2013-02-12T06:57:36.000Z'}, {'id': 424, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '2013-03-21T12:28:48.000Z'}, {'id': 425, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2013-04-27T18:00:00.000Z'}, {'id': 426, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '2013-06-03T23:31:12.000Z'}, {'id': 427, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2013-07-11T05:02:24.000Z'}, {'id': 428, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2013-08-17T10:33:36.000Z'}, {'id': 429, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': 
'2013-09-23T16:04:48.000Z'}, {'id': 430, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '2013-10-30T21:36:00.000Z'}, {'id': 431, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '2013-12-07T03:07:12.000Z'}, {'id': 432, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2014-01-13T08:38:24.000Z'}, {'id': 433, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 
38}, 'fecha': '2014-02-19T14:09:36.000Z'}, {'id': 434, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2014-03-28T19:40:48.000Z'}, {'id': 435, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2014-05-05T01:12:00.000Z'}, {'id': 436, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2014-06-11T06:43:12.000Z'}, {'id': 437, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2014-07-18T12:14:24.000Z'}, {'id': 438, 'producto': {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 'fecha': '2014-08-24T17:45:36.000Z'}, {'id': 439, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2014-09-30T23:16:48.000Z'}, {'id': 440, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2014-11-07T04:48:00.000Z'}, {'id': 441, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 
'fecha': '2014-12-14T10:19:12.000Z'}, {'id': 442, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '2015-01-20T15:50:24.000Z'}, {'id': 443, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 
'fecha': '2015-02-26T21:21:36.000Z'}, {'id': 444, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2015-04-05T02:52:48.000Z'}, 
{'id': 445, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2015-05-12T08:24:00.000Z'}, {'id': 446, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2015-06-18T13:55:12.000Z'}, {'id': 447, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2015-07-25T19:26:24.000Z'}, {'id': 448, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2015-09-01T00:57:36.000Z'}, {'id': 449, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2015-10-08T06:28:48.000Z'}, {'id': 450, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2015-11-14T12:00:00.000Z'}, {'id': 451, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2015-12-21T17:31:12.000Z'}, {'id': 452, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2016-01-27T23:02:24.000Z'}, {'id': 453, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2016-03-05T04:33:36.000Z'}, {'id': 454, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2016-04-11T10:04:48.000Z'}, {'id': 455, 'producto': {'id': 17, 'tipo': 'saco', 'talle': 'S'}, 'fecha': '2016-05-18T15:36:00.000Z'}, {'id': 456, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2016-06-24T21:07:12.000Z'}, {'id': 457, 
'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2016-08-01T02:38:24.000Z'}, {'id': 458, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2016-09-07T08:09:36.000Z'}, {'id': 459, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2016-10-14T13:40:48.000Z'}, {'id': 460, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2016-11-20T19:12:00.000Z'}, {'id': 461, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2016-12-28T00:43:12.000Z'}, {'id': 462, 'producto': {'id': 6, 'tipo': 'pantalon', 'talle': 40}, 'fecha': '2017-02-03T06:14:24.000Z'}, {'id': 463, 'producto': {'id': 4, 'tipo': 'pantalon', 'talle': 38}, 'fecha': '2017-03-12T11:45:36.000Z'}, {'id': 464, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2017-04-18T17:16:48.000Z'}, {'id': 465, 'producto': {'id': 2, 'tipo': 'pantalon', 'talle': 36}, 'fecha': '2017-05-25T22:48:00.000Z'}, {'id': 466, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '2017-07-02T04:19:12.000Z'}, {'id': 467, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '2017-08-08T09:50:24.000Z'}, {'id': 468, 'producto': {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, 'fecha': '2017-09-14T15:21:36.000Z'}, {'id': 469, 'producto': {'id': 3, 'tipo': 'pantalon', 'talle': 37}, 'fecha': '2017-10-21T20:52:48.000Z'}, {'id': 470, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2017-11-28T02:24:00.000Z'}, {'id': 471, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2018-01-04T07:55:12.000Z'}, {'id': 472, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2018-02-10T13:26:24.000Z'}, {'id': 473, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '2018-03-19T18:57:36.000Z'}, {'id': 474, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2018-04-26T00:28:48.000Z'}, {'id': 475, 'producto': {'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2018-06-02T06:00:00.000Z'}, {'id': 476, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2018-07-09T11:31:12.000Z'}, {'id': 477, 'producto': {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '2018-08-15T17:02:24.000Z'}, {'id': 478, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2018-09-21T22:33:36.000Z'}, {'id': 479, 'producto': {'id': 8, 'tipo': 'pantalon', 'talle': 42}, 'fecha': '2018-10-29T04:04:48.000Z'}, {'id': 480, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2018-12-05T09:36:00.000Z'}, {'id': 481, 'producto': 
{'id': 5, 'tipo': 'pantalon', 'talle': 39}, 'fecha': '2019-01-11T15:07:12.000Z'}, {'id': 482, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '2019-02-17T20:38:24.000Z'}, {'id': 483, 'producto': 
{'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2019-03-27T02:09:36.000Z'}, {'id': 484, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '2019-05-03T07:40:48.000Z'}, {'id': 485, 'producto': {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, 'fecha': '2019-06-09T13:12:00.000Z'}, {'id': 486, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2019-07-16T18:43:12.000Z'}, {'id': 487, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2019-08-23T00:14:24.000Z'}, {'id': 488, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2019-09-29T05:45:36.000Z'}, {'id': 489, 'producto': {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 'fecha': '2019-11-05T11:16:48.000Z'}, {'id': 490, 'producto': {'id': 9, 'tipo': 'pantalon', 'talle': 43}, 'fecha': '2019-12-12T16:48:00.000Z'}, {'id': 491, 'producto': {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 'fecha': '2020-01-18T22:19:12.000Z'}, {'id': 492, 'producto': {'id': 16, 'tipo': 'saco', 
'talle': 'XS'}, 'fecha': '2020-02-25T03:50:24.000Z'}, {'id': 493, 'producto': {'id': 7, 'tipo': 'pantalon', 'talle': 41}, 'fecha': '2020-04-02T09:21:36.000Z'}, {'id': 494, 'producto': {'id': 10, 'tipo': 'pantalon', 'talle': 44}, 'fecha': '2020-05-09T14:52:48.000Z'}, {'id': 495, 'producto': {'id': 13, 'tipo': 'remera', 'talle': 'M'}, 'fecha': '2020-06-15T20:24:00.000Z'}, {'id': 496, 'producto': {'id': 12, 'tipo': 'remera', 
'talle': 'S'}, 'fecha': '2020-07-23T01:55:12.000Z'}, {'id': 497, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2020-08-29T07:26:24.000Z'}, {'id': 498, 'producto': {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 'fecha': '2020-10-05T12:57:36.000Z'}, {'id': 499, 'producto': {'id': 1, 'tipo': 'pantalon', 'talle': 35}, 'fecha': '2020-11-11T18:28:48.000Z'}, {'id': 500, 'producto': {'id': 19, 'tipo': 'saco', 'talle': 'L'}, 'fecha': '2020-12-19T00:00:00.000Z'}]
'''
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

#4. URLs y URIs
#Desafío VIII: decí usando tus palabras qué significa la URI de este ejemplo cerebral
#cerebro://recuerdos:3403/recientes#hoy?tema=http
#La URI de este ejemplo significa que estamos viendo los recuerdos del cerebro de hoy y del tema http.

#Desafío IX: ¿a través de qué IP accedés a google desde tu computadora?
#Desde la interfaz de red de mi wifi.

#6. CABECERAS
#Desafío X: ¿Qué devolverá la página principal (home) de nuestro sitio?
# Averiguá el Content-Type de /home
r = requests.get('https://macowins-server.herokuapp.com/home')
print(r.headers)
for clave in r.headers.keys():
    if clave=="Content-Type":
        print(r.headers[clave])
#text/html; charset=UTF-8

#Desafío XI: consultá 4 sitios diferentes y averiguá para todos ellos qué servidor utilizan, 
# si el contenido se transfiere encriptado, y la fecha de expieración del contenido.
r = requests.get('https://github.com/')
for clave, valor in r.headers.items():
    print(clave, valor)
#Server GitHub.com
#Expires=Wed, 29 Jun 2022 23:47:15 GMT
#Accept-Encoding
#Content-Encoding gzip
#Transfer-Encoding chunked

r = requests.get('https://ucema.edu.ar/carreras-de-grado')
for clave, valor in r.headers.items():
    print(clave, valor)
#Server nginx
#Accept-Encoding, Cookie
#Transfer-Encoding chunked
#Content-Encoding gzip
#Expires Sun, 19 Nov 1978 05:00:00 GMT

r = requests.get('https://www.infobae.com/ultimas-noticias/')
for clave, valor in r.headers.items():
    print(clave, valor)
#Server openresty
#Content-Encoding gzip
#Vary Accept-Encoding
#Transfer-Encoding chunked
#Expires Tue, 29 Jun 2021 23:53:42 GMT

r = requests.get('https://www.tiempo.com/buenos-aires.htm')
for clave, valor in r.headers.items():
    print(clave, valor)
#Server cloudflare
#Vary Accept-Encoding, User-Agent
#Content-Encoding gzip
#Transfer-Encoding chunked
#Expires Wed, 30 Jun 2021 00:00:00 GMT

#9. Creando y actualizando contenido
#Desafío XII: ¿qué código de estado devuelve cuando un recurso es creado? Averigualo
data = {'id': 21}
r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
r.headers
#Devuelve el status code 201

#Para pensar: Hmm, funcionó, pero ¿creó el contenido que queríamos? ¿Por qué?
data =  { "tipo": "chomba", "talle": "XS" }
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=data)
#no porque no le pasamos un id en la data y en su lugar puso un id inventado.

#Desafío: Nos quedaron prendas con ids que no nos sirven; ¡borralas!
a = requests.delete('https://macowins-server.herokuapp.com/prendas/200')
b = requests.delete('https://macowins-server.herokuapp.com/prendas/oiTJPhJ')
c = requests.delete('https://macowins-server.herokuapp.com/prendas/-hr7uKL')

#Desafío XIII: Creá una venta.
data = {'id': 1800, 'tipo': 'remera', 'talle': 'XS'}, 'fecha': '2021-29-06T15:07:12.000Z'}
r = requests.post('https://macowins-server.herokuapp.com/ventas', data=data)

#🏅 Desafío XIV: Intentá hacer POST sobre una venta concreta, como por ejemplo https://macowins-server.herokuapp.com/prendas/1. ¿Qué sucede?
r13 = requests.post("https://macowins-server.herokuapp.com/prendas/1")
print(r13.status_code)#404
print(r13.json()) #tira error
#no se puede, el post se podria hacer sobre prendas, le tenemos que decir que vamos a agregar
#ej 
#data = {'id':21}
#r = requests.post("https://macowins-server.herokuapp.com/prendas", data=data)

#Desafío XV: ¿cuales de los siguientes sitios tiene (o parecen tener, al menos) rutas REST?
# Github -> si
# Youtube -> no
# Facebook -> si
# Infobae, Pagina12, La Nacion -> si
# UNQ, UCEMA -> si