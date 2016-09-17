#!/bin/python3
#encode: utf8
import datetime
import csv
import psycopg2


conn = psycopg2.connect("dbname=cervebase port=5432")

# crear un cursor para ejecutar consultas
cur = conn.cursor()

# abrir la planilla CSV e iterar sobre cada fila, cerrar el archivo al finalizar
with open('breweries.csv', 'r',encoding="latin1") as csvfile:
    # intentar determinar automaticamente formato del archivo:
    dialect = csv.Sniffer().sniff(csvfile.read(100))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect, delimiter=",")
    # saltear encabezado (primera fila
    encabezado = next(reader)
    # recorrer las filas de los datos en el CSV:
    for linea in reader:
        print (linea)
        # convertir el texto de cada campo a valores python:
        val_id = int(linea[0])
        val_nombre = linea[1]
        val_calle1 = linea[2]
        val_calle2 = linea[3]
        city = linea[4]
        state = linea[5]
        zipcode = linea[6]
        country = linea[7]
        tel = linea[8]
        website = linea[9]
        desc = linea[11]
      
        # evitar clave duplicada!
        if val_id in (30095, 26327,):
            continue
        # insertar datos, evitar inyección SQL separando sentencias de parámetros
        parametros = [val_id, val_nombre, val_calle1, val_calle2, city, state, country, website,zipcode, desc]
        cur.execute("INSERT INTO cervecerias "
                    " (idCerveceria, nombre, calle1, calle2, city, state,"
                    " contry, website, zipcode, descripcion)"
                    " VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)",
                    parametros)
                    
conn.commit()  
