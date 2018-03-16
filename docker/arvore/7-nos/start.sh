run(){
# $s = numero de switch's
# $h = numero de host's
# $i = contador

i=0
s=7
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
h=4
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
docker start sw0 sw1 sw2 sw3 sw4 sw5 sw6 h0 h1 h2 h3
}



conf-sw(){
s=7
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
h=4
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
# ----- FOLHA 1 -------
#sw0 x sw1
docker exec sw0 ovs-vsctl add-port s0 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.2
docker exec sw1 ovs-vsctl add-port s1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw1 x sw2
docker exec sw1 ovs-vsctl add-port s1 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.3
docker exec sw2 ovs-vsctl add-port s2 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.2

#sw1 x sw3
docker exec sw1 ovs-vsctl add-port s1 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.4
docker exec sw3 ovs-vsctl add-port s3 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.2

#sw0 x sw4
docker exec sw0 ovs-vsctl add-port s0 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.5
docker exec sw4 ovs-vsctl add-port s4 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw4 x sw5
docker exec sw4 ovs-vsctl add-port s4 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.6
docker exec sw5 ovs-vsctl add-port s5 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5

#sw4 x sw6
docker exec sw4 ovs-vsctl add-port s4 gre2 -- set interface gre2 type=gre options:remote_ip=172.28.5.7
docker exec sw6 ovs-vsctl add-port s6 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5

echo "Estabelecendo links com os Hosts"
echo ""

#sw3 x h0
docker exec sw3 ovs-vsctl add-port s3 gre5 -- set interface gre5 type=gre options:remote_ip=172.28.5.8
docker exec h0 ovs-vsctl add-port h0 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.4

#sw2 x h1
docker exec sw2 ovs-vsctl add-port s2 gre5 -- set interface gre5 type=gre options:remote_ip=172.28.5.9
docker exec h1 ovs-vsctl add-port h1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.3

#sw5 x h2
docker exec sw5 ovs-vsctl add-port s5 gre5 -- set interface gre5 type=gre options:remote_ip=172.28.5.10
docker exec h2 ovs-vsctl add-port h2 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.6

#sw6 x h3
docker exec sw6 ovs-vsctl add-port s6 gre5 -- set interface gre5 type=gre options:remote_ip=172.28.5.11
docker exec h3 ovs-vsctl add-port h3 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.7
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
