#!/usr/bin/env python

import pynotify
import socket
import sys
import os

def notify(title,message,icon="icon.png") :
    pynotify.init("SUDO") # the app name is the argument given
    notify = pynotify.Notification(title,message,icon)
    notify.show()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def show_on_systems(start,subnet,end) :
    count = 0
    for i in range(start,end+1) :
        ip_addr = "192.168."+str(subnet)+"."+str(i)
        ret = os.system("ping -c1 "+str(ip_addr)+" > /dev/null")
        if ret == 0 :
            print ip_addr
            count = count + 1
    return count

def check_network_access(hostname="8.8.8.8") :
    a = os.system("ping -c1 "+hostname+" > /dev/null")
    if a == 0 :
        notify("Network Access","successful")
    else :
        notify("Network Access","unsuccessful")
    yield a
