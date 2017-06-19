#!/usr/bin/python
import getopt, json, os.path, sys, urllib.request
from urllib.request import urlopen
from ipaddress import ip_network, ip_address

# Ayuda
def usage():
   print ('Usage: check_ip_amazon [-hd] [-ip Direccion IP]')
   print
   print ('-h --help			Imprimir Ayuda')
   print ('-d				Descargar el fichero JSON de Amazon ip-ranges.json')
   print ('-p				Amazon Host para comprobar')

# Descargar JSON data de Amazon
def downloadJSONdata_ip_amazon():
	#descargar la ultima version del fichero json con todas las ip's de amazon
	#crear el fichero ip-ranges.json, que se importara despues
	print ("Descargand Json....")
	url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
	outfile = "ip-ranges.json"
	urllib.request.urlretrieve(url, outfile)

try:
    opts, args = getopt.getopt(sys.argv[1:], "hdi:", ["help","d","input"])
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
    elif o in ('-i', '--input'):
        ip_check = a
    else:
         assert False, "Error parametro no valido"

data = json.load(open('ip-ranges.json'))
for d in data["prefixes"]:
	#print (d["ip_prefix"])
	#aIpamazon.append(d["ip_prefix"])
	net = ip_network(d["ip_prefix"])
	#print(ip_address(ip_check) in net)
	if ip_address(ip_check) in net:
		print ("encontrado")
		print ("La ip", ip_check , " pertenece al rango" , d["ip_prefix"])







