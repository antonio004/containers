#!/usr/bin/python3
import lxc
import sys
import os


# $s = numero de switch's
# $h = numero de host's
# $i = contador

i = 0
s = 31

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
h=16
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

#sw3 x sw5
c = lxc.Container("sw3")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s3", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.15"])
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.13"])

#sw2 x sw6
c = lxc.Container("sw2")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s2", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.16"])
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.12"])

#sw6 x sw7
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.17"])
c = lxc.Container("sw7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.16"])

#sw6 x sw8
c = lxc.Container("sw6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s6", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.18"])
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.16"])

# ----- FIM FOLHA 1 ------

# ----- FOLHA 2 ----------

#sw1 x sw9
c = lxc.Container("sw1")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s1", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.19"])
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.11"])

#sw9 x sw10
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.20"])
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.19"])

#sw10 x sw11
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.21"])
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.20"])

#sw10 x sw12
c = lxc.Container("sw10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s10", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.22"])
c = lxc.Container("sw12")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s12", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.20"])

#sw9x sw13
c = lxc.Container("sw9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s9", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.23"])
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.19"])

#sw13 x sw14
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.24"])
c = lxc.Container("sw14")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s14", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.23"])

#sw13 x sw15
c = lxc.Container("sw13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s13", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.25"])
c = lxc.Container("sw15")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s15", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.23"])

# ------ FIM FOLHA 2 --------

# ------ FOLHA 3 ------------

#sw0 x sw16
c = lxc.Container("sw0")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s0", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.26"])
c = lxc.Container("sw16")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s16", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.10"])

#sw16 x sw17
c = lxc.Container("sw16")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s16", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.27"])
c = lxc.Container("sw17")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s17", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.26"])

#sw17 x sw18
c = lxc.Container("sw17")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s17", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.28"])
c = lxc.Container("sw18")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s18", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.27"])

#sw18 x sw19
c = lxc.Container("sw18")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s18", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.29"])
c = lxc.Container("sw19")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s19", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.28"])

#sw18 x sw20
c = lxc.Container("sw18")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s18", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.30"])
c = lxc.Container("sw20")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s20", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.28"])

#sw17 x sw21
c = lxc.Container("sw17")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s17", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.31"])
c = lxc.Container("sw21")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s21", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.27"])

#sw21 x sw22
c = lxc.Container("sw21")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s21", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.32"])
c = lxc.Container("sw22")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s22", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.31"])

#sw21 x sw23
c = lxc.Container("sw21")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s21", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.33"])
c = lxc.Container("sw23")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s23", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.31"])

# ----- FIM FOLHA 3 ------

# ----- FOLHA 4 ----------

#sw16 x sw24
c = lxc.Container("sw16")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s16", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.34"])
c = lxc.Container("sw24")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s24", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.26"])

#sw24 x sw25
c = lxc.Container("sw24")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s24", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.35"])
c = lxc.Container("sw25")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s25", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.34"])

#sw25 x sw26
c = lxc.Container("sw25")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s25", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.36"])
c = lxc.Container("sw26")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s26", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.35"])

#sw25 x sw27
c = lxc.Container("sw25")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s25", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.37"])
c = lxc.Container("sw27")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s27", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.35"])

#sw24 x sw28
c = lxc.Container("sw24")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s24", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.38"])
c = lxc.Container("sw28")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s28", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.34"])

#sw28 x sw29
c = lxc.Container("sw28")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s28", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.39"])
c = lxc.Container("sw29")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s29", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.38"])

#sw28 x s30
c = lxc.Container("sw28")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s28", "gre2", "--", "set", "interface", "gre2", "type=gre", "options:remote_ip=10.0.3.40"])
c = lxc.Container("sw30")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s30", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.38"])

# ----- FIM FOLHA 4 ------



print("Estabelendo Link entre os Hosts"+"\n")
#sw4 x h0
c = lxc.Container("sw4")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s4", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.50"])
c = lxc.Container("h0")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h0", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.14"])

#sw5 x h1
c = lxc.Container("sw5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s5", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.51"])
c = lxc.Container("h1")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h1", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.15"])

#sw7 x h2
c = lxc.Container("sw7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s7", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.52"])
c = lxc.Container("h2")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h2", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.17"])

#sw8 x h3
c = lxc.Container("sw8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s8", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.53"])
c = lxc.Container("h3")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h3", "gre0", "--", "set", "interface", "gre0", "type=gre", "options:remote_ip=10.0.3.18"])

#sw11 x h4
c = lxc.Container("sw11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s11", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.54"])
c = lxc.Container("h4")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h4", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.21"])

#sw12 x h5
c = lxc.Container("sw12")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s12", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.55"])
c = lxc.Container("h5")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h5", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.22"])

#sw14 x h6
c = lxc.Container("sw14")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s14", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.56"])
c = lxc.Container("h6")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h6", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.24"])

#sw15 x h7
c = lxc.Container("sw15")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s15", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.57"])
c = lxc.Container("h7")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h7", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.25"])

#sw19 x h8
c = lxc.Container("sw19")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s19", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.58"])
c = lxc.Container("h8")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h8", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.29"])

#sw20 x h9
c = lxc.Container("sw20")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s20", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.59"])
c = lxc.Container("h9")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h9", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.30"])

#sw22 x h10
c = lxc.Container("sw22")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s22", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.60"])
c = lxc.Container("h10")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h10", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.32"])

#sw23 x h11
c = lxc.Container("sw23")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s23", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.61"])
c = lxc.Container("h11")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h11", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.33"])

#sw26 x h12
c = lxc.Container("sw26")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s26", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.62"])
c = lxc.Container("h12")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h12", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.36"])

#sw27 x h13
c = lxc.Container("sw27")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s27", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.63"])
c = lxc.Container("h13")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h13", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.37"])

#sw29 x h14
c = lxc.Container("sw29")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s29", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.64"])
c = lxc.Container("h14")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h14", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.39"])

#sw30 x h15
c = lxc.Container("sw30")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "s30", "gre10", "--", "set", "interface", "gre10", "type=gre", "options:remote_ip=10.0.3.65"])
c = lxc.Container("h15")
c.attach_wait(lxc.attach_run_command, ["ovs-vsctl", "add-port", "h15", "gre1", "--", "set", "interface", "gre1", "type=gre", "options:remote_ip=10.0.3.40"])

