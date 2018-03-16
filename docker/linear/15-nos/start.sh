run(){
# $s = numero de switch's
# $h = numero de host's
# $i = contador

i=0
s=15
#laço que cria os switchs
docker stop onos
docker rm onos
cont=$(docker create --name onos -it --net=sdn onosproject/onos)
while [ $i -lt $s ]
do
   echo "Criando Switch sw$i"
   echo ""
   if [ ! "$(docker ps -a | grep sw$i)" ]; then
   
      sw$i=$(docker create --name sw$i --net=sdn -it --cap-add NET_ADMIN --cap-add SYS_MODULE -v /lib/modules:/lib/modules socketplane/openvswitch)
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
h=2
i=0 #seta variavel como zero novamente
while [ $i -lt $h ]
do
   echo "Criando host h$i"
   echo ""
   if [ ! "$(docker ps -a | grep h$i)" ]; then
      ht$i=$(docker create --name h$i --net=sdn -it --cap-add NET_ADMIN --cap-add SYS_MODULE -v /lib/modules:/lib/modules socketplane/openvswitch)
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

start(){
docker start sw0 sw1 sw2 sw3 sw4 sw5 sw6 sw7 sw8 sw9 sw10 sw11 sw12 sw13 sw14 h0 h1
}
 
conf-sw(){
s=15
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
h=2
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

#sw0 x sw1
docker exec sw0 ovs-vsctl add-port s0 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.2
docker exec sw1 ovs-vsctl add-port s1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw1 x sw2
docker exec sw1 ovs-vsctl add-port s1 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.3
docker exec sw2 ovs-vsctl add-port s2 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.2

#sw2 x sw3
docker exec sw2 ovs-vsctl add-port s2 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.4
docker exec sw3 ovs-vsctl add-port s3 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.3

#sw3 x sw4
docker exec sw3 ovs-vsctl add-port s3 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.5
docker exec sw4 ovs-vsctl add-port s4 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.4

#sw4 x sw5
docker exec sw4 ovs-vsctl add-port s4 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.6
docker exec sw5 ovs-vsctl add-port s5 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5

#sw5 x sw6
docker exec sw5 ovs-vsctl add-port s5 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.7
docker exec sw6 ovs-vsctl add-port s6 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.6

#sw6 x sw7
docker exec sw6 ovs-vsctl add-port s6 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.8
docker exec sw7 ovs-vsctl add-port s7 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.7

#sw7 x sw8
docker exec sw7 ovs-vsctl add-port s7 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.9
docker exec sw8 ovs-vsctl add-port s8 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.8

#sw8 x sw9
docker exec sw8 ovs-vsctl add-port s8 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.10
docker exec sw9 ovs-vsctl add-port s9 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.9

#sw9 x sw10
docker exec sw9 ovs-vsctl add-port s9 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.11
docker exec sw10 ovs-vsctl add-port s10 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.10

#sw10 x sw11
docker exec sw10 ovs-vsctl add-port s10 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.12
docker exec sw11 ovs-vsctl add-port s11 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.11

#sw11 x sw12
docker exec sw11 ovs-vsctl add-port s11 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.13
docker exec sw12 ovs-vsctl add-port s12 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.12

#sw12 x sw13
docker exec sw12 ovs-vsctl add-port s12 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.14
docker exec sw13 ovs-vsctl add-port s13 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.13

#sw13 x sw14
docker exec sw13 ovs-vsctl add-port s13 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.15
docker exec sw14 ovs-vsctl add-port s14 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.14


echo "Estabelecendo links Com os Hosts"
echo ""

#sw0 x h0
docker exec sw0 ovs-vsctl add-port s0 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.16
docker exec h0 ovs-vsctl add-port h0 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw14 x h1
docker exec sw14 ovs-vsctl add-port s14 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.17
docker exec h1 ovs-vsctl add-port h1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.15
}

teste(){
   docker exec h0 ping -c3 192.0.1.15
   docker exec h15 ping -c3 192.0.1.0

}

run
start
conf-sw
conf-host
links
#teste
