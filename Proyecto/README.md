# Proyecto Analisis-RRSS-Python

Proyectos:

* Proyecto_arduino.ipynb - Adquisición y análisis de datos de tweets sobre Arduino y Trump
* Proyecto_jecrespom.ipynb - Adquisición y análisis de los followers y friends del usuario @jecrespom
* Proyecto_Trump.ipynb - Análisis de los datos sobre Trump con un fichero de relaciones de grafo ya hecho

## Proyecto_arduino.ipynb

### Datos de tweets obtenidos de la palabra clave 'arduino' y guardados en formato pickle y sqlite

BBDD: tweets.sqlite
Tabla: arduino

Tweets: 16269
Relaciones grafo: 13616
fichero relaciones: grafo_arduino.csv

### Datos de tweets obtenidos de la palabra clave 'Trump' y guardados en formato pickle y sqlite

BBDD: tweets.sqlite
Tabla: trump

Tweets: 183489
Relaciones grafo: 246622
fichero relaciones: grafo_json_trump.csv

## Proyecto_jecrespom.ipynb

Análisis de la red de followers y friends del usuario @jecrespom.

Followers = 2602. Solo se recogen xx de Followes de segundo nivel. (en varias recopilaciones)
Friends = 746. Se recoge el 100% de Friends de segundo nivel.

fichero relaciones followers: grafo_followers.csv, grafo_followers_2.csv y grafo_followers_todos.csv (en varias fases de captura)
fichero relaciones friends: grafo_friends.csv (relaciones: 1080782)
fichero relaciones todo (followers + friends): grafo_jecrespom.csv

Para el caso de Followers se deja preparado para poder continuar cogiendo Followers.
Script (pasar a función o módulo en el futuro) que toma el fichero de relaciones y toma los followers ya consultados y nos los vuelve a consultar. También guarda los followers que no permite consulta en otro fichero para tampoco consultarlos en followers_acceso_no_permitido.txt.

Ficheros:

* grafo_followers.csv - Primera captura de datos (514 Followers y 564724 relaciones)
* grafo_followers_2.csv - Segunda captura de datos (336 Followers y 482437 relaciones)
* grafo_followers_todos.csv - Total de primera y segunda captura (850 Followers y 1047161 relaciones)
* followers_acceso_no_permitido.txt - Listado de followers sin acceso a sus datos (74 Followers)

### Proyecto_Trump.ipynb

Proyecto propuesto
