start(){
docker start sw0 sw1 sw2 sw3 sw4 sw5 sw6 sw7 sw8 sw9 sw10 sw11 sw12 sw13 sw14 sw15 sw16 sw17 sw18 sw19 sw20 sw21 sw22 sw23 sw24 sw25 sw26 sw27 sw28 sw29 sw30 h0 h1 
}

run(){
# $s = numero de switch's
# $h = numero de host's
# $i = contador

i=0
s=30
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
    docker start sw$i
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
#echo ""
#echo "Host's Criados com Sucesso"
#echo ""
}
 
conf-sw(){
s=30
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

echo "Estabelecendo Conexão entre os Switch's"
echo ""


echo "Estabelecendo Link com os Host's"
echo ""

#sw0 x h0
docker exec sw0 ovs-vsctl add-port s0 gre5 -- set interface gre5 type=gre options:remote_ip=172.28.5.32
docker exec h0 ovs-vsctl add-port h0 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.1

#sw29 x h1
docker exec sw29 ovs-vsctl add-port s29 gre5 -- set interface gre5 type=gre options:remote_ip=172.28.5.33
docker exec h1 ovs-vsctl add-port h1 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.30

}
teste1(){
	gnuplot -p -e "
    set xdata time;
    set timefmt '%s';
    set xrange [ '$(date +%s)' : '$(date -d 'now +20 seconds' +%s)' ];
    plot '-' using 1:2 with line title 'ping entre hosts (Controlador e Dispositivos Iniciados Simultaneamente);" < <(
  (
      docker exec h0 ping -c 100 -n 192.0.1.1 |
        sed -u 's/^64.*time=\([0-9.]\+\) .*$/\1/p;d' |
        tee >(sed -u 's/.*/now/'| stdbuf -oL date -f - +d%s)
  ) | sed -u 'N;s/\n/ /;s/\([0-9.]\+\) d\([0-9]\+\) */\2 \1/;s/d//' |
  tee >(printf "%(%T)T %s\n" $(</dev/stdin) |
  column -c $COLUMNS >&2 )
)
}

teste(){
docker exec h0 ping -c 30 192.0.1.1
docker exec h1 ping -c 30 192.0.1.0
}
#run
#start
#conf-sw
#conf-host
links
#teste
