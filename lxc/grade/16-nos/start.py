#!/usr/bin/python3
import lxc
import sys
import os


# $s = numero de switch's
# $h = numero de host's
# $i = contador

i = 0
s = 16

if not os.geteuid() == 0:
    print("The use of overlayfs requires privileged containers.")
    sys.exit(1)


print("Inciando a Criação dos switch's \n")

while(i<s):
   
  c = lxc.Container("sw"+str(i))
   
  if not c.defined:
    c.create("download", lxc.LXC_CREATE_QUIET, {"dist": "ubuntu","release": "xenial","arch": "amd64"})
    print("Container Criado sw"+str(i)+"\n")
    print("Configurando o ovs do  sw"+str(i)+"\n")
  else:
    c.start()
    print("Container SW"+str(i)+" iniciado.")
    c.get_ips(timeout=30)
    #c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "-y", "openvswitch-switch"])
    #c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "-y", "iputils-ping"])
    #c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "net-tools"]
    c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-br", "s"+str(i)])
    c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "set-controller", "s"+str(i), "tcp:172.28.5.0:6653"])
    c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "set-fail-mode", "s"+str(i), "secure"])
  i = i+1

i=0
h=2
while(i<h):
   
  c = lxc.Container("h"+str(i))
   
  if not c.defined:
    c.create("download", lxc.LXC_CREATE_QUIET, {"dist": "ubuntu","release": "xenial","arch": "amd64"})
    print("Container Criado h"+str(i)+"\n")
    print("Configurando host_"+str(i)+"\n")
    c.start()
    c.get_ips(timeout=30)
    c.attach_wait(lxc.attach_run_command, ["apt-get", "update"])
    c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "-y", "openvswitch-switch"])
  else:
    c.start()
    print("Container H"+str(i)+" iniciado.")
    c.get_ips(timeout=30)
    #c.attach_wait(lxc.attach_run_command, ["apt-get", "update"])
    #c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "-y", "openvswitch-switch"])
    #c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "-y", "iputils-ping"])
    #c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "net-tools"])
    c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-br", "h"+str(i)])
    c.attach_wait(lxc.attach_run_command, ["ifconfig","h"+str(i),"192.0.1."+str(i),"netmask","255.255.0.0", ])
  i = i+1  

print("Estabelendo Link entre os Switches"+"\n")
# ---------------- FOLHA 1  --------------------

#sw0 x sw1
c = lxc.Container("sw0")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s0", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.11"])
c = lxc.Container("sw1")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s1", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.10"])

#sw1 x sw2
c = lxc.Container("sw1")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s1", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.12"])
c = lxc.Container("sw2")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s2", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.11"])

#sw2 x sw3
c = lxc.Container("sw2")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s2", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.13"])
c = lxc.Container("sw3")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s3", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.12"])

#sw0 x sw4
c = lxc.Container("sw0")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s0", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.14"])
c = lxc.Container("sw4")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s4", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.10"])

#sw1 x sw5
c = lxc.Container("sw1")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s1", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.15"])
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.11"])

#sw2 x sw6
c = lxc.Container("sw2")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s2", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.16"])
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.12"])

#sw3 x sw7
c = lxc.Container("sw3")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s3", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.17"])
c = lxc.Container("sw7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.13"])

#sw4 x sw5
c = lxc.Container("sw4")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s4", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.15"])
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.14"])

#sw5 x sw6
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.16"])
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.15"])

#sw6 x sw7
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.17"])
c = lxc.Container("sw7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.16"])

#sw4 x sw8
c = lxc.Container("sw4")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s4", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.18"])
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.14"])

#sw5 x sw9
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.19"])
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.15"])

#sw6 x sw10
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.20"])
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.16"])

#sw7 x sw11
c = lxc.Container("sw7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.21"])
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.17"])

#sw8 x sw9
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.19"])
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.18"])

#sw9 x sw10
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.20"])
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.19"])

#sw10 x sw11
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.21"])
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.20"])

#sw8 x sw12
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.22"])
c = lxc.Container("sw12")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s12", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.18"])

#sw9 x sw13
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.23"])
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.19"])

#sw10 x sw14
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.24"])
c = lxc.Container("sw14")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s14", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.20"])

#sw11 x sw15
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.25"])
c = lxc.Container("sw15")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s15", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.21"])

#sw12 x sw13
c = lxc.Container("sw12")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s12", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.23"])
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.22"])

#sw13 x sw14
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.24"])
c = lxc.Container("sw14")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s14", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.23"])

#sw14 x sw15
c = lxc.Container("sw14")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s14", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.25"])
c = lxc.Container("sw15")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s15", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.24"])



print("Estabelendo Link Com os Hosts \n")

#sw0 x h0
c = lxc.Container("sw0")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s0", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.50"])
c = lxc.Container("h0")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h0", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.10"])

#sw4 x h1
c = lxc.Container("sw15")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s15", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.51"])
c = lxc.Container("h1")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h1", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.25"])