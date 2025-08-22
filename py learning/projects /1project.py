#!/bin/python3

import sys 
import socket 
from datetime import datetime 

#define our target 
if len(sys.argv) == 2:
       target = socket.gethostbyname(sys.argv[1])#translate hostname to ipv4

else:
      print("invalid amount of arguments")
      print("syntax: python3 scanner.py <ip>")

#add a pretty banner 
print("-" * 50)
print("Scanning target: "+target)
print("time started: "+str(datetime.now()))
print("-" * 50)

try:
        for port in range(400,500):
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               socket.setdefaulttimeout(1)
               result = s.connect_ex((target,port))
               if result == 0:
                         print(f"Port {port} is open")
               s.close() 

except KeyboardInterrupt:
         print("\nExiting program.")
         sys.exit()          
 
except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

except socket.error:
       print("coult not connect to server.")
       sys.exit() 