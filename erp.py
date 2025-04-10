#Script de Python para una ERP con Oddo

#Paquetes y Librerias para Win
import os
import subprocess
import platform
import distro
import sys
import requests
#from time import monotonic
from tqdm import tqdm
import time

#funciones Generales

urlDescargas = ['https://aka.ms/vs/17/release/vs_BuildTools.exe','https://sbp.enterprisedb.com/getfile.jsp?fileid=1259402']

odooDescargas = ['https://nightly.odoo.com/16.0/nightly/windows/odoo_16.0.latest.exe','https://nightly.odoo.com/17.0/nightly/windows/odoo_17.0.latest.exe','https://nightly.odoo.com/18.0/nightly/windows/odoo_18.0.latest.exe']

def descargar_archivo(link, nombre_archivo):
    respuesta = requests.get(link, stream=True)
    size_total = int(respuesta.headers.get("content-length", 0))
    bloque_size = 1024

    with open(nombre_archivo, "wb") as archivo, tqdm(
        desc=nombre_archivo,
        total=size_total,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as barra:
        for datos in respuesta.iter_content(bloque_size):
            archivo.write(datos)
            barra.update(len(datos))


posturl = ["C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\BuildTools","C:\\Program Files\\PostgreSQL\\17\\bin",""]
#Imprime y retorna el valor del sistema operativo

System = platform.system()

if System == "Windows":
    print("Sistema operativo:", platform.system(), end="\n\n")
    print("Version:", platform.win32_ver(release=''), end="\n\n")
    print("Edicion:", platform.win32_edition(), end="\n\n")

    if os.path.exists(posturl[0]):
        print("VsBuildTools Instalado...")
        time.sleep(1.5)
    else:
    #instala las Buildtools de C++ Necesarias para Odoo
        print("Quieres descargar e Instalar Vs_BuildTools [s/n]")
        Res = input()

        if Res == "s":
            descargar_archivo(urlDescargas[0], "Vs_BuildTools.exe")
            os.system("Vs_BuildTools.exe")
            #os.system("cls")

        elif Res == "n":
            print("El paquete es necesario")
            sys.exit()

        else:
            print("Opcion no Valida")
            sys.exit()

    if os.path.exists(posturl[1]):
        print("PostgreSQL Instalado...")
        time.sleep(1.5)
    else:
        #Descarga PostgreSql para Odoo
        print("Quieres descargar e Instalar PosgreSQL [s/n]")
        Res = input()

        if Res == "s":
            descargar_archivo(urlDescargas[1], "PostgreSql.exe")
            os.system("PostgreSql.exe")
            os.system("cls")
        elif Res == "n":
            print("El paquete es necesario")
            sys.exit()

    if os.path.exists(posturl[2]):
        print("Odoo Instalado...")
        time.sleep(1.5)
        os.system("cls")
    else:
        #Descarga El instalador de odoo
        print("""Que version de Odoo quieres instalar
        [1]Odoo 16
        [2]Odoo 17
        [3]Odoo 18""")
        Res = int(input())

        if Res == 1 or Res == 2 or Res == 3:
            descargar_archivo(odooDescargas[Res], "Odoo.exe")
            os.system("Odoo.exe")
            os.system("cls")
        else:
            print("El paquete es necesario")
            sys.exit()






#Ejecucion en la distribuciones Linux
else:
    print("Sistema operativo:", platform.system(), end="\n\n")
    print("Distro:", distro.name())
    print("Versión:", distro.version())
    print("ID:", distro.id())


#Descargar("", "Postgre.exe", stream=True)
#os.system("Postgre.exe")

#Descargar("", "Odoo.exe")
#os.system("Odoo.exe")

