#!/usr/bin/python3
import lxc
import sys
import os

# $s = numero de switch's
# $h = numero de host's
# $i = contador
i = 0
s = 30

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




print("\n Conectando os Switches \n")

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

#sw3 x sw4
c = lxc.Container("sw3")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s3", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.14"])
c = lxc.Container("sw4")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s4", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.13"])

#sw0 x sw5
c = lxc.Container("sw0")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s0", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.15"])
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.10"])

#sw1 x sw6
c = lxc.Container("sw1")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s1", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.16"])
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.11"])

#sw2 x sw7
c = lxc.Container("sw2")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s2", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.17"])
c = lxc.Container("sw7")
c.start()
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.12"])

#sw3 x sw8
c = lxc.Container("sw3")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s3", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.18"])
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.13"])

#sw4 x sw9
c = lxc.Container("sw4")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s4", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.19"])
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.14"])


#sw5 x sw6 
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.16"])
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.15"])

#sw6 x sw7
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.17"])
c = lxc.Container("sw7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.16"])

#sw7 x sw8
c = lxc.Container("sw7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.18"])
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.17"])

#sw8 x sw9
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.19"])
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.18"])

#sw5 x sw10
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.20"])
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.15"])

#sw6 x sw11
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.21"])
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.16"])

#sw7 x sw12
c = lxc.Container("sw7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.22"])
c = lxc.Container("sw12")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s12", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.17"])

#sw8 x sw13
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.23"])
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.18"])

#sw9 x sw14
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.24"])
c = lxc.Container("sw14")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s14", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.19"])

#sw10 x sw11
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.21"])
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.20"])

#sw11 x sw12
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.22"])
c = lxc.Container("sw12")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s12", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.21"])

#sw12 x sw13
c = lxc.Container("sw12")
c.start()
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s12", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.23"])
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.22"])


#sw13 x sw14
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.24"])
c = lxc.Container("sw14")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s14", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.23"])

#sw10 x sw15
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.25"])
c = lxc.Container("sw15")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s15", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.20"])

#sw11 x sw16
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.26"])
c = lxc.Container("sw16")
c.start()
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s16", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.21"])

#sw12 x sw17
c = lxc.Container("sw12")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s12", "gre4", "--", "set", "interface", "gre4", "type=gre", "options:remote_ip=10.0.3.27"])
c = lxc.Container("sw17")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s17", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.22"])

#sw13 x sw18
c = lxc.Container("sw13")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.28"])
c = lxc.Container("sw18")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s18", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.23"])

#sw14 x sw19
c = lxc.Container("sw14")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s14", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.29"])
c = lxc.Container("sw19")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s19", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.24"])

#sw15 x sw16
c = lxc.Container("sw15")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s15", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.26"])
c = lxc.Container("sw16")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s16", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.25"])

#sw16 x sw17
c = lxc.Container("sw16")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s16", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.27"])
c = lxc.Container("sw17")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s17", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.26"])

#sw17 x sw18
c = lxc.Container("sw17")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s17", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.28"])
c = lxc.Container("sw18")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s18", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.27"])

#sw18 x sw19
c = lxc.Container("sw18")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s18", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.29"])
c = lxc.Container("sw19")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s19", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.28"])

#sw15 x sw20
c = lxc.Container("sw15")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s15", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.30"])
c = lxc.Container("sw20")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s20", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.25"])

#sw16 x sw21
c = lxc.Container("sw16")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s16", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.31"])
c = lxc.Container("sw21")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s21", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.26"])

#sw17 x sw22
c = lxc.Container("sw17")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s17", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.32"])
c = lxc.Container("sw22")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s22", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.27"])

#sw18 x sw23
c = lxc.Container("sw18")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s18", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.33"])
c = lxc.Container("sw23")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s23", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.28"])

#sw19 x sw24
c = lxc.Container("sw19")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s19", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.34"])
c = lxc.Container("sw24")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s24", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.29"])

#sw20 x sw21
c = lxc.Container("sw20")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s20", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.31"])
c = lxc.Container("sw21")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s21", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.30"])

#sw21 x sw22
c = lxc.Container("sw21")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s21", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.32"])
c = lxc.Container("sw22")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s22", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.31"])

#sw22 x sw23
c = lxc.Container("sw22")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s22", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.33"])
c = lxc.Container("sw23")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s23", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.32"])

#sw23 x sw24
c = lxc.Container("sw23")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s23", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.34"])
c = lxc.Container("sw24")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s24", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.33"])

#sw20 x sw25
c = lxc.Container("sw20")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s20", "gre5", "--", "set", "interface", "gre5", "type=gre", "options:remote_ip=10.0.3.35"])
c = lxc.Container("sw25")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s25", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.30"])

#sw21 x sw26
c = lxc.Container("sw21")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s21", "gre5", "--", "set", "interface", "gre5", "type=gre", "options:remote_ip=10.0.3.36"])
c = lxc.Container("sw26")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s26", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.31"])

#sw22 x sw27
c = lxc.Container("sw22")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s22", "gre5", "--", "set", "interface", "gre5", "type=gre", "options:remote_ip=10.0.3.37"])
c = lxc.Container("sw27")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s27", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.32"])

#sw23 x sw28
c = lxc.Container("sw23")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s23", "gre5", "--", "set", "interface", "gre5", "type=gre", "options:remote_ip=10.0.3.38"])
c = lxc.Container("sw28")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s28", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.33"])

#sw24 x sw29
c = lxc.Container("sw24")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s24", "gre5", "--", "set", "interface", "gre5", "type=gre", "options:remote_ip=10.0.3.39"])
c = lxc.Container("sw29")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s29", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.34"])

#sw25 x sw26
c = lxc.Container("sw25")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s25", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.36"])
c = lxc.Container("sw26")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s26", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.35"])

#sw26 x sw27
c = lxc.Container("sw26")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s26", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.37"])
c = lxc.Container("sw27")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s27", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.36"])

#sw27 x sw28
c = lxc.Container("sw27")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s27", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.38"])
c = lxc.Container("sw28")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s28", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.37"])

#sw28 x sw29
c = lxc.Container("sw28")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s28", "gre3", "--", "set", "interface", "gre3", "type=gre", "options:remote_ip=10.0.3.38"])
c = lxc.Container("sw29")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s29", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.39"])


print("\n Criando Link com os Host's \n")

#sw0 x h0
c = lxc.Container("sw0")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s0", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.50"])
c = lxc.Container("h0")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h0", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.10"])

#sw29 x h1
c = lxc.Container("sw29")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s29", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.51"])
c = lxc.Container("h1")
c.start()
c.get_ips(timeout=30)
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h1", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.39"])

#h0   = 10.0.3.18, 192.0.1.0      
#h1   = 10.0.3.116, 192.0.1.1     
#sw0  = 10.0.3.229                
#sw1  = 10.0.3.107                
#sw10 = 10.0.3.65                 
#sw11 = 10.0.3.166                
#sw12 = 10.0.3.179                
#sw13 = 10.0.3.239                
#sw14 = 10.0.3.118                
#sw15 = 10.0.3.79                 
#sw16 = 10.0.3.25                 
#sw17 = 10.0.3.4                  
#sw18 = 10.0.3.168                
#sw19 = 10.0.3.140                
#sw2  = 10.0.3.14                 
#sw20 = 10.0.3.115                
#sw21 = 10.0.3.46                 
#sw22 = 10.0.3.246                
#sw23 = 10.0.3.175                
#sw24 = 10.0.3.248                
#sw3  = 10.0.3.152                
#sw4  = 10.0.3.160                
#sw5  = 10.0.3.247                
#sw6  = 10.0.3.103                
#sw7  = 10.0.3.70                 
#sw8  = 10.0.3.128                
#sw9  = 10.0.3.207   


'''
h0   RUNNING 0         -      10.0.3.192 -    
h1   RUNNING 0         -      10.0.3.116 -    
h10  STOPPED 0         -      -          -    
h11  STOPPED 0         -      -          -    
h12  STOPPED 0         -      -          -    
h13  STOPPED 0         -      -          -    
h14  STOPPED 0         -      -          -    
h15  STOPPED 0         -      -          -    
h2   RUNNING 0         -      10.0.3.225 -    
h3   RUNNING 0         -      -          -    
h4   RUNNING 0         -      -          -    
h5   RUNNING 0         -      -          -    
h6   RUNNING 0         -      -          -    
h7   STOPPED 0         -      -          -    
h8   STOPPED 0         -      -          -    
h9   STOPPED 0         -      -          -    
sw0  RUNNING 0         -      10.0.3.95  -    
sw1  RUNNING 0         -      10.0.3.170 -    
sw10 RUNNING 0         -      10.0.3.188 -    
sw11 RUNNING 0         -      10.0.3.77  -    
sw12 RUNNING 0         -      10.0.3.251 -    
sw13 RUNNING 0         -      10.0.3.75  -    
sw14 RUNNING 0         -      10.0.3.178 -    
sw15 RUNNING 0         -      10.0.3.180 -    
sw16 RUNNING 0         -      10.0.3.24  -    
sw17 RUNNING 0         -      10.0.3.193 -    
sw18 RUNNING 0         -      10.0.3.19  -    
sw19 RUNNING 0         -      10.0.3.204 -    
sw2  RUNNING 0         -      10.0.3.48  -    
sw20 RUNNING 0         -      10.0.3.58  -    
sw21 RUNNING 0         -      10.0.3.189 -    
sw22 RUNNING 0         -      10.0.3.207 -    
sw23 RUNNING 0         -      10.0.3.27  -    
sw24 RUNNING 0         -      10.0.3.179 -    
sw25 RUNNING 0         -      10.0.3.177 -    
sw26 RUNNING 0         -      10.0.3.25  -    
sw27 RUNNING 0         -      10.0.3.138 -    
sw28 RUNNING 0         -      10.0.3.59  -    
sw29 RUNNING 0         -      10.0.3.206 -    
sw3  RUNNING 0         -      10.0.3.28  -    
sw30 RUNNING 0         -      10.0.3.87  -    
sw4  RUNNING 0         -      10.0.3.51  -    
sw5  RUNNING 0         -      10.0.3.127 -    
sw6  RUNNING 0         -      10.0.3.81  -    
sw7  RUNNING 0         -      10.0.3.5   -    
sw8  RUNNING 0         -      10.0.3.171 -    
sw9  RUNNING 0         -      10.0.3.186 - 
'''