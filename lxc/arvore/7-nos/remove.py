#!/usr/bin/python3
import lxc
import sys
import os


i = 0
s = 7

if not os.geteuid() == 0:
    print("The use of overlayfs requires privileged containers.")
    sys.exit(1)


print("Inciando a Remoção da Configuracao dos switch's \n")

while(i<s):
   
  c = lxc.Container("sw"+str(i)) 
  c.start()
  c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "del-br", "s"+str(i)])
  c.stop()
  #c.stop()
  i = i+1

i=0
h=5
while(i<h):
   
  c = lxc.Container("h"+str(i)) 
  c.start()
  #c.stop()
   #c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "net-tools"])
  c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "del-br", "h"+str(i)])
  c.stop()
  i = i+1  

print("Configuracao removida")