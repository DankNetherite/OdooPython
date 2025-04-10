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

#funciones Generales

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

# URL de ejemplo (puedes cambiarla por cualquier archivo real)
url = "https://aka.ms/vs/17/release/vs_BuildTools.exe"

posturl = "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Licenses\BuildTools\3082"
#Imprime y retorna el valor del sistema operativo

System = platform.system()

if System == "Windows":
    print("Sistema operativo:", platform.system(), end="\n\n")
    print("Version:", platform.win32_ver(release=''), end="\n\n")
    print("Edicion:", platform.win32_edition(), end="\n\n")

    if os.path.exists(posturl):
        print("PostgreSQL Instalado...")
        os.system("cls")
    else:
        print("Quieres descargar e Instalar Vs_BuildTools [s/n]")
        Res = input()

        if Res == "s":
            descargar_archivo(url, "Vs_BuildTools.exe")
            os.system("Vs_BuildTools.exe")
            #os.system("cls")

        elif Res == "n":
            print("El paquete es necesario")
            sys.exit()

        else:
            print("Opcion no Valida")
            sys.exit()

    if os.path.exists(posturl):
        print("PostgreSQL Instalado...")
        os.system("cls")
    else:
        print("Quieres descargar e Instalar PosgreSQL [s/n]")
        Res = input()

        if Res == "s":
            descargar_archivo(url, "PostgreSql.exe")
            os.system("PostgreSql.exe")
            os.system("cls")
        elif Res == "n":
            print("El paquete es necesario")
            sys.exit()
#Ejecucion en la distribuciones Linux
else:
    print("Sistema operativo:", platform.system(), end="\n\n")
    print("Distro:", distro.name())
    print("Versión:", distro.version())
    print("ID:", distro.id())


#Descargar("https://sbp.enterprisedb.com/getfile.jsp?fileid=1259402", "Postgre.exe", stream=True)
#os.system("Postgre.exe")

#Descargar("https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe", "pip3.13.2.exe")
#os.system("pip3.13.2.exe")

#Descargar("https://nightly.odoo.com/18.0/nightly/windows/odoo_18.0.latest.exe", "Odoo.exe")
#os.system("Odoo.exe")

