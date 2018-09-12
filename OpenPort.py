#version python 3.6
from socket import *
import os
import time
def port():
    w = input ("say me a site you want scann and find free port:")
    o = gethostbyname(w)
    time.sleep(3)
    print()
    print ("site" , w , "IP" , "=" , o)
    print()
    time.sleep(2)
    print("Scann open Port" , w  )
    print()
    time.sleep(2)
    print("Watting")
    for i in range (1 , 1025):
        s = socket(AF_INET , SOCK_STREAM)
        a = s.connect_ex((o , i))
        if a == 0:
            print ("Port" , i ,  "Open")
        if a != 0:
            print ("port", i , "not open")
        s.close()
port()
