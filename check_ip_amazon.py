#!/usr/bin/python
import getopt, json, os.path, sys, urllib.request
from urllib.request import urlopen
from ipaddress import ip_network, ip_address
from pathlib import Path

# Mostrar Ayuda
def usage():
   print ('Uso: check_ip_amazon [-h] [-d] [-i]')
   print
   print ('-h --help			Imprimir Ayuda')
   print ('-d				Descargar el fichero JSON de Amazon ip-ranges.json')
   print ('-i				Amazon Host para comprobar')

# Descargar JSON data de Amazon
def downloadJSONdata_ip_amazon():
	#Descargar la ultima version del fichero json con todas las ip's de amazon
	#crear el fichero ip-ranges.json, que se importara despues
	print ("Descargando Json....")
	url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
	outfile = "ip-ranges.json"
	urllib.request.urlretrieve(url, outfile)

ip_check = ""
	
try:
    opts, args = getopt.getopt(sys.argv[1:], "hdi:", ["help","d"])
except getopt.GetoptError as err:
    # print help information and exit
    print (str(err))
    usage()
    sys.exit(2)
	
for o, a in opts:
    if o in ('-h', '--help'):
       usage()
       sys.exit()
    elif o in ('-d'):
        downloadJSONdata_ip_amazon()
    elif o in ('-i'):
        ip_check = a
    else:
         assert False, "Error parametro no valido"

#Si no se define una ip para comprobar salimos
if not ip_check:
	sys.exit()
	
#Comprobar si ya existe el fichero en local
file_ip_range = Path("ip-ranges.json")
if not file_ip_range.is_file():
    downloadJSONdata_ip_amazon()
	
data = json.load(open('ip-ranges.json'))
for d in data["prefixes"]:
	net = ip_network(d["ip_prefix"])
	if ip_address(ip_check) in net:
		print ("Encontrado")
		print ("La ip", ip_check , " pertenece al rango" , d["ip_prefix"])
		print ("service:",d["service"])
		print ("region:", d["region"])


