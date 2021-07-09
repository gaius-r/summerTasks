#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

field = cgi.FieldStorage()
cmd = field.getvalue("cmd")
conf_path = '~/admin.conf' # path to admin.conf for kubernetes 
out = subprocess.getoutput('sudo kubectl '+ cmd +' --kubeconfig '+ conf_path)
print("<pre>" + out + "</pre>")
