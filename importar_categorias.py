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
with open('categories.csv', 'r',encoding="latin1") as csvfile:
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
      
        # evitar clave duplicada!
        if val_id in (30095, 26327,):
            continue
        # insertar datos, evitar inyección SQL separando sentencias de parámetros
        parametros = [val_id, val_nombre]
        cur.execute("INSERT INTO categorias "
                    " (idCategoria, nombre)"
                    "VALUES(%s, %s)",
                    parametros)
                    
conn.commit()  
