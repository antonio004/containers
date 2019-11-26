run(){
# $s = numero de switch's
# $h = numero de host's
# $i = contador

i=0
s=5
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
h=2
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

start(){
docker start sw0 sw1 sw2 sw3 sw4 h0 h1
}
 
conf-sw(){
s=5
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


echo "Estabelecendo links Com os Hosts"
echo ""

#sw0 x h0
docker exec sw0 ovs-vsctl add-port s0 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.6
docker exec h0 ovs-vsctl add-port h0 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw4 x h1
docker exec sw4 ovs-vsctl add-port s4 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.7
docker exec h1 ovs-vsctl add-port h1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.5
}

teste(){
sleep 15
echo "Verificando Conexão"
echo ""
   docker exec h0 ping -c 30 192.0.1.1 >> latencia-ping


}

run
start
conf-sw
conf-host
links
teste
