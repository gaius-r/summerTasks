#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

field = cgi.FieldStorage()
cmd = field.getvalue("cmd")
out = subprocess.getoutput('sudo docker '+ cmd)
print("<pre>" + out + "</pre>")
