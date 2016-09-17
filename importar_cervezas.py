#!/bin/python3
#encode: utf8
import datetime
import csv
import json
import psycopg2


conn = psycopg2.connect("dbname=cervebase port=5432")

# crear un cursor para ejecutar consultas, y limpiar todos los registros:
cur = conn.cursor()
##cur.execute("TRUNCATE cervecerias;")

# abrir la planilla CSV e iterar sobre cada fila, cerrar el archivo al finalizar
with open('beers.csv', 'r',encoding="latin1") as csvfile:
    # intentar determinar automaticamente formato del archivo:
    dialect = csv.Sniffer().sniff(csvfile.read(100))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect, delimiter=",")
    # saltear encabezado (primera fila
    encabezado = next(reader)
    # recorrer las filas de los datos en el CSV:

    for linea in reader:
        #print (linea)
        # convertir el texto de cada campo a valores python:
        idCerveza = int(linea[0])
        idCerveceria = int(linea[1])
        nombre = linea[2]
        idCategoria = int(linea[3])
        idEstilo = int(linea[4])
        adv = float(linea[5])
        ibu = float(linea[6])
        srm = float(linea[7])
        upc = float(linea[8])
        descripcion = linea[10]

        if idCategoria == -1:
            idCategoria = None
            idEstilo = None
             
        if descripcion == '':
            descripcion = None
            
        # evitar clave duplicada!
        if idCerveza in (30095, 26327,):
            continue
        # insertar datos, evitar inyección SQL separando sentencias de parámetros
        parametros = [idCerveza, idCerveceria, nombre, idCategoria, idEstilo, adv, ibu, upc, srm, descripcion]
        cur.execute("INSERT INTO cervezas "
                    " (idCerveza, idCerveceria, nombre, idCategoria, idEstilo, adv, ibu, upc,"
                    " srm, descripcion)"
                    " VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)",
                    parametros)
                    
conn.commit()  
