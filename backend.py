#!/usr/bin/python3

import cgi
import subprocess
import time
from datetime import datetime

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
print("<h2> Your command is :-<h2>" ,cmd,"<h2> \n Output is :-</h2>")
print("<h3>Today's date and time is {:%Y-%m-%d %H:%M}</h3>".format(datetime.now()))
output = subprocess.getoutput("kubctl" + cmd + "--kubeconfig admin.conf")
print("*"*100)
print()
print(output)
print()
print("*"*100)
time.sleep(0)
print('<h1 style="background-color: green"> THANK YOU FOR USING THIS KUBERNETES UI PAGE</h1>')
