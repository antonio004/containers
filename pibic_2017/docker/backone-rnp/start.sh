#!/bin/bash
start(){
docker start sw0 sw1 sw2 sw3 sw4 sw5 sw6 sw7 sw8 sw9 sw10 sw11 sw12 sw13 sw14 sw15 sw16 sw17 sw18 sw19 sw20 sw21 sw22 sw23 sw24 sw25 sw26 sw27 sw28 sw29 sw30 h0 h1 h2 h3 h4
}

run(){
i=0
s=31
#laço que cria os switchs
while [ $i -lt $s ]
do
   echo "Criando Switch sw$i"
   echo ""
   if [ ! "$(docker ps -a | grep sw$i)" ]; then
   docker run --name sw$i --net=sdn -itd --cap-add NET_ADMIN --cap-add SYS_MODULE -v /lib/modules:/lib/modules socketplane/openvswitch
   else
   echo "O container sw$i já existe"
   echo ""
   i=`expr $i + 1`
   fi
done
echo "****** Atualizando Repositório ******"
echo ""
apt-get update
echo ""
echo "Switch's Criados com Sucesso"
echo ""


#laço que cria os hosts
h=5
i=0 #seta variavel como zero novamente
while [ $i -lt $h ]
do
   echo "Criando host h$i"
   echo ""
   if [ ! "$(docker ps -a | grep h$i)" ]; then
   docker run --name h$i --net=sdn -itd --cap-add NET_ADMIN --cap-add SYS_MODULE -v /lib/modules:/lib/modules socketplane/openvswitch
   else
   echo "O container sw$i já existe"
   echo ""
   fi
   i=`expr $i + 1`
done
echo ""
echo "Host's Criados com Sucesso"
echo ""
}
 
conf-sw(){
s=31
i=0 #seta variavel como zero novamente
echo "Configurando Switch's"
echo ""
while [ $i -lt $s ]
do
  docker exec sw$i ovs-vsctl add-br s$i
  docker exec sw$i ovs-vsctl set-controller s$i tcp:172.28.5.0:6653
  docker exec sw$i ovs-vsctl set-fail-mode s$i secure
   i=`expr $i + 1`
done
echo "Switch's Configurados"
echo ""
}

conf-host(){
h=5
i=0
echo "Configurando Host's"
echo ""

while [ $i -lt $h ]
do
  docker exec h$i ovs-vsctl add-br h$i
  docker exec h$i ifconfig h$i 192.0.1.$i netmask 255.255.0.0 up
   i=`expr $i + 1`
done

echo "Host's Configurados"
echo ""
}

links(){


echo "Estabelecendo Conexão entre os Switch's"
echo ""
#sw0 x sw2
docker exec sw0 ovs-vsctl add-port s0 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.3
docker exec sw2 ovs-vsctl add-port s2 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw0 x sw21
docker exec sw0 ovs-vsctl add-port s0 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.22
docker exec sw21 ovs-vsctl add-port s21 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw1 x sw6
docker exec sw1 ovs-vsctl add-port s1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.7
docker exec sw6 ovs-vsctl add-port s6 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.2

#sw2 x sw3
docker exec sw2 ovs-vsctl add-port s2 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.4
docker exec sw3 ovs-vsctl add-port s3 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.3

#sw3 x sw22
docker exec sw3 ovs-vsctl add-port s3 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.23
docker exec sw22 ovs-vsctl add-port s22 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.4

#sw4 sw9
docker exec sw4 ovs-vsctl add-port s4 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.10
docker exec sw9 ovs-vsctl add-port s9 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5

#sw4 x sw26
docker exec sw4 ovs-vsctl add-port s4 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.27
docker exec sw26 ovs-vsctl add-port s26 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5

#sw4 x sw27
docker exec sw4 ovs-vsctl add-port s4 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.28
docker exec sw27 ovs-vsctl add-port s27 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5

#sw4 x sw10
docker exec sw4 ovs-vsctl add-port s4 gre3 -- set interface gre3 type=gre options:remote_ip=172.28.5.11
docker exec sw10 ovs-vsctl add-port s10 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5

#sw4 x sw5
docker exec sw4 ovs-vsctl add-port s4 gre4 -- set interface gre4 type=gre options:remote_ip=172.28.5.6
docker exec sw5 ovs-vsctl add-port s5 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5

#sw5 sw16
docker exec sw5 ovs-vsctl add-port s5 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.17
docker exec sw16 ovs-vsctl add-port s16 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.6

#sw5 x sw30
docker exec sw5 ovs-vsctl add-port s5 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.31
docker exec sw30 ovs-vsctl add-port s30 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.6

#sw5 x sw7
docker exec sw5 ovs-vsctl add-port s5 gre3 -- set interface gre3 type=gre options:remote_ip=172.28.5.8
docker exec sw7 ovs-vsctl add-port s7 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.6

#sw6 x sw7
docker exec sw6 ovs-vsctl add-port s6 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.8
docker exec sw7 ovs-vsctl add-port s7 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.7

#sw7 x sw8
docker exec sw7 ovs-vsctl add-port s7 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.9
docker exec sw8 ovs-vsctl add-port s8 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.8

#sw8 x sw9
docker exec sw8 ovs-vsctl add-port s8 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.10
docker exec sw9 ovs-vsctl add-port s9 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.9

#sw9 x sw16
docker exec sw9 ovs-vsctl add-port s9 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.17
docker exec sw16 ovs-vsctl add-port s16 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.10

#sw11 x sw19
docker exec sw11 ovs-vsctl add-port s11 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.20
docker exec sw19 ovs-vsctl add-port s19 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.12

#sw11 x sw12
docker exec sw11 ovs-vsctl add-port s11 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.13
docker exec sw12 ovs-vsctl add-port s12 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.12

#sw12 x sw17
docker exec sw12 ovs-vsctl add-port s12 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.18
docker exec sw17 ovs-vsctl add-port s17 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.13

#sw12 x sw20
docker exec sw12 ovs-vsctl add-port s12 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.21
docker exec sw20 ovs-vsctl add-port s20 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.13

#sw13 x sw16
docker exec sw13 ovs-vsctl add-port s13 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.17
docker exec sw16 ovs-vsctl add-port s16 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.14

#sw13 x sw20
docker exec sw13 ovs-vsctl add-port s13 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.21
docker exec sw20 ovs-vsctl add-port s20 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.14

#sw13 x sw14
docker exec sw13 ovs-vsctl add-port s13 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.15
docker exec sw14 ovs-vsctl add-port s14 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.14

#sw14 x sw15
docker exec sw14 ovs-vsctl add-port s14 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.16
docker exec sw15 ovs-vsctl add-port s15 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.15

#sw15 x sw16
docker exec sw15 ovs-vsctl add-port s15 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.17
docker exec sw16 ovs-vsctl add-port s16 gre3 -- set interface gre3 type=gre options:remote_ip=172.28.5.16

#sw16 x sw23
docker exec sw16 ovs-vsctl add-port s16 gre4 -- set interface gre4 type=gre options:remote_ip=172.28.5.24
docker exec sw23 ovs-vsctl add-port s23 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.17

#sw16 x sw24
docker exec sw16 ovs-vsctl add-port s16 gre5 -- set interface gre5 type=gre options:remote_ip=172.28.5.25
docker exec sw24 ovs-vsctl add-port s24 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.17

#sw16 x sw25
docker exec sw16 ovs-vsctl add-port s16 gre6 -- set interface gre6 type=gre options:remote_ip=172.28.5.26
docker exec sw25 ovs-vsctl add-port s25 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.17

#sw17 x sw18
docker exec sw17 ovs-vsctl add-port s17 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.19
docker exec sw18 ovs-vsctl add-port s18 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.18

#sw21 x sw28
docker exec sw21 ovs-vsctl add-port s21 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.29
docker exec sw28 ovs-vsctl add-port s28 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.22

#sw22 x sw30
docker exec sw22 ovs-vsctl add-port s22 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.31
docker exec sw30 ovs-vsctl add-port s30 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.23

#sw28 x sw29
docker exec sw28 ovs-vsctl add-port s28 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.30
docker exec sw29 ovs-vsctl add-port s29 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.29

#sw29 x sw30
docker exec sw29 ovs-vsctl add-port s29 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.31
docker exec sw30 ovs-vsctl add-port s30 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.30


echo "Estabelecendo Link com os Host's"
echo ""

#sw0 x h0
docker exec sw0 ovs-vsctl add-port s0 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.32
docker exec h0 ovs-vsctl add-port h0 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw10 x h1
docker exec sw10 ovs-vsctl add-port s10 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.33
docker exec h1 ovs-vsctl add-port h1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.11

#sw16 x h2
docker exec sw16 ovs-vsctl add-port s16 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.34
docker exec h2 ovs-vsctl add-port h2 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.17

#sw20 x h3
docker exec sw20 ovs-vsctl add-port s20 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.35
docker exec h3 ovs-vsctl add-port h3 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.21

#sw29 x h4
docker exec sw29 ovs-vsctl add-port s29 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.36
docker exec h4 ovs-vsctl add-port h4 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.30






##sw1 x h1
#docker exec sw1 ovs-vsctl add-port s1 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.33
#docker exec h1 ovs-vsctl add-port h1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.2
#
##sw2 x h2
#docker exec sw2 ovs-vsctl add-port s2 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.34
#docker exec h2 ovs-vsctl add-port h2 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.3
#
##sw3 x h3
#docker exec sw3 ovs-vsctl add-port s3 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.35
#docker exec h3 ovs-vsctl add-port h3 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.4
#
##sw4 x h4 
#docker exec sw4 ovs-vsctl add-port s4 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.36
#docker exec h4 ovs-vsctl add-port h4 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5
#
##sw5 x h5
#docker exec sw5 ovs-vsctl add-port s5 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.37
#docker exec h5 ovs-vsctl add-port h5 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.6
#
##sw6 x h6
#docker exec sw6 ovs-vsctl add-port s6 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.38
#docker exec h6 ovs-vsctl add-port h6 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.7
#
##sw7 x h7
#docker exec sw7 ovs-vsctl add-port s7 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.39
#docker exec h7 ovs-vsctl add-port h7 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.8
#
##sw8 x h8
#docker exec sw8 ovs-vsctl add-port s8 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.40
#docker exec h8 ovs-vsctl add-port h8 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.9
#
##sw9 x h9
#docker exec sw9 ovs-vsctl add-port s9 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.41
#docker exec h9 ovs-vsctl add-port h9 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.10
#
##sw10 x h10
#docker exec sw10 ovs-vsctl add-port s10 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.42
#docker exec h10 ovs-vsctl add-port h10 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.11
#
##sw11 x h11
#docker exec sw11 ovs-vsctl add-port s11 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.43
#docker exec h11 ovs-vsctl add-port h11 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.12
#
##sw12 x h12
#docker exec sw12 ovs-vsctl add-port s12 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.44
#docker exec h12 ovs-vsctl add-port h12 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.13
#
##sw13 x h13
#docker exec sw13 ovs-vsctl add-port s13 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.45
#docker exec h13 ovs-vsctl add-port h13 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.14
#
##sw14 x h14
#docker exec sw14 ovs-vsctl add-port s14 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.46
#docker exec h14 ovs-vsctl add-port h14 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.15
#
##sw15 x h15 
#docker exec sw15 ovs-vsctl add-port s15 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.47
#docker exec h15 ovs-vsctl add-port h15 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.16
#
##sw16 x h16
#docker exec sw16 ovs-vsctl add-port s16 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.48
#docker exec h16 ovs-vsctl add-port h16 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.17
#
##sw17 x h17
#docker exec sw17 ovs-vsctl add-port s17 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.49
#docker exec h17 ovs-vsctl add-port h17 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.18
#
##sw18 x h18
#docker exec sw18 ovs-vsctl add-port s18 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.50
#docker exec h18 ovs-vsctl add-port h18 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.19
##
###sw19x h19
##docker exec sw19 ovs-vsctl add-port s19 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.51
##docker exec h19 ovs-vsctl add-port h19 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.20
##
###sw20 x h20
##docker exec sw20 ovs-vsctl add-port s20 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.52
##docker exec h20 ovs-vsctl add-port h20 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.21
##
###sw21 x h21
##docker exec sw21 ovs-vsctl add-port s21 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.53
##docker exec h21 ovs-vsctl add-port h21 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.22
##
###sw22 x h22
##docker exec sw22 ovs-vsctl add-port s22 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.54
##docker exec h22 ovs-vsctl add-port h22 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.23
#
##sw23 x h23
#docker exec sw23 ovs-vsctl add-port s23 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.55
#docker exec h23 ovs-vsctl add-port h23 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.24
#
##sw24 x h24
#docker exec sw24 ovs-vsctl add-port s24 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.56
#docker exec h24 ovs-vsctl add-port h24 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.25
#
##sw25 x h25
#docker exec sw25 ovs-vsctl add-port s25 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.57
#docker exec h25 ovs-vsctl add-port h25 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.26
#
##sw26 x h26
#docker exec sw26 ovs-vsctl add-port s26 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.58
#docker exec h26 ovs-vsctl add-port h26 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.27
#
##sw27 x h27
#docker exec sw27 ovs-vsctl add-port s27 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.59
#docker exec h27 ovs-vsctl add-port h27 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.28
#
##sw28 x h28
#docker exec sw28 ovs-vsctl add-port s28 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.60
#docker exec h28 ovs-vsctl add-port h28 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.29
#
##sw29 x h29
#docker exec sw29 ovs-vsctl add-port s29 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.61
#docker exec h29 ovs-vsctl add-port h29 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.30
#
##sw30 x h30
#docker exec sw30 ovs-vsctl add-port s30 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.62
#docker exec h30 ovs-vsctl add-port h30 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.31

}


#IPS


#sw0=172.28.5.1
#sw1=172.28.5.2
#sw2=172.28.5.3
#sw3=172.28.5.4
#sw4=172.28.5.5
#sw5=172.28.5.6
#sw6=172.28.5.7
#sw7=172.28.5.8
#sw8=172.28.5.9
#sw9=172.28.5.10
#sw10=172.28.5.11
#sw11=172.28.5.12
#sw12=172.28.5.13
#sw13=172.28.5.14
#sw14=172.28.5.15
#sw15=172.28.5.16
#sw16=172.28.5.17
#sw17=172.28.5.18
#sw18=172.28.5.19
#sw19=172.28.5.20
#sw20=172.28.5.21
#sw21=172.28.5.22
#sw22=172.28.5.23
#sw33=172.28.5.24
#sw24=172.28.5.25
#sw25=172.28.5.26
#sw26=172.28.5.26
#sw27=172.28.5.28
#sw28=172.28.5.29
#sw29=172.28.5.30
#sw30=172.28.5.31


#h0=172.28.5.32
#h1=172.28.5.33
#h2=172.28.5.34
#h3=172.28.5.35
#h4=172.28.5.36
#h5=172.28.5.37
#h6=172.28.5.38
#h7=172.28.5.39
#h8=172.28.5.40
#h9=172.28.5.41
#h10=172.28.5.42
#h11=172.28.5.43
#h12=172.28.5.44
#s13=172.28.5.45
#h14=172.28.5.46
#h15=172.28.5.47
#h16=172.28.5.48
#h17=172.28.5.49
#h18=172.28.5.50
#h19=172.28.5.51
#h20=172.28.5.52
#h21=172.28.5.53
#h22=172.28.5.54
#h23=172.28.5.55
#h24=172.28.5.56
#h25=172.28.5.57
#h26=172.28.5.58
#h27=172.28.5.59
#h28=172.28.5.60
#h29=172.28.5.61
#h30=172.28.5.62

#controller
#run
start
conf-sw
conf-host
links

