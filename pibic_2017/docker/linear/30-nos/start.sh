
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

start(){
docker start sw0 sw1 sw2 sw3 sw4 sw5 sw6 sw7 sw8 sw9 sw10 sw11 sw12 sw13 sw14 sw15 sw16 sw17 sw18 sw19 sw20 sw21 sw22 sw23 sw24 sw25 sw26 sw27 sw28 sw29 h0 h1
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

#sw14 x sw15
docker exec sw14 ovs-vsctl add-port s14 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.16
docker exec sw15 ovs-vsctl add-port s15 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.15

#sw15 x sw16
docker exec sw15 ovs-vsctl add-port s15 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.17
docker exec sw16 ovs-vsctl add-port s16 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.16

#sw16 x sw17
docker exec sw16 ovs-vsctl add-port s16 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.18
docker exec sw17 ovs-vsctl add-port s17 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.17

#sw17 x sw18
docker exec sw17 ovs-vsctl add-port s17 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.19
docker exec sw18 ovs-vsctl add-port s18 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.18

#sw18 x sw19
docker exec sw18 ovs-vsctl add-port s18 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.20
docker exec sw19 ovs-vsctl add-port s19 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.19

#sw19 x sw20
docker exec sw19 ovs-vsctl add-port s19 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.21
docker exec sw20 ovs-vsctl add-port s20 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.20

#sw20 x sw21
docker exec sw20 ovs-vsctl add-port s20 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.22
docker exec sw21 ovs-vsctl add-port s21 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.21

#sw21 x sw22
docker exec sw21 ovs-vsctl add-port s21 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.23
docker exec sw22 ovs-vsctl add-port s22 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.22

#sw22 x sw23
docker exec sw22 ovs-vsctl add-port s22 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.24
docker exec sw23 ovs-vsctl add-port s23 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.23

#sw23 x sw24
docker exec sw23 ovs-vsctl add-port s23 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.25
docker exec sw24 ovs-vsctl add-port s24 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.24

#sw24 x sw25
docker exec sw24 ovs-vsctl add-port s24 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.26
docker exec sw25 ovs-vsctl add-port s25 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.25

#sw25 x sw26
docker exec sw25 ovs-vsctl add-port s25 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.27
docker exec sw26 ovs-vsctl add-port s26 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.26

#sw26 x sw27
docker exec sw26 ovs-vsctl add-port s26 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.28
docker exec sw27 ovs-vsctl add-port s27 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.27

#sw27 x sw28
docker exec sw27 ovs-vsctl add-port s27 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.29
docker exec sw28 ovs-vsctl add-port s28 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.28

#sw28 x sw29
docker exec sw28 ovs-vsctl add-port s28 gre1 -- set interface gre1 type=gre options:remote_ip=172.28.5.30
docker exec sw29 ovs-vsctl add-port s29 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.29


echo "Estabelecendo Link com os Host's"
echo ""

#sw0 x h0
docker exec sw0 ovs-vsctl add-port s0 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.31
docker exec h0 ovs-vsctl add-port h0 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.1

#sw29 x h1
docker exec sw29 ovs-vsctl add-port s29 gre10 -- set interface gre10 type=gre options:remote_ip=172.28.5.32
docker exec h1 ovs-vsctl add-port h1 gre0 -- set interface gre0 type=gre options:remote_ip=172.28.5.30


}

teste(){
sleep 15
echo "Verificando Conexão"
echo ""
   docker exec h0 ping -c 30 192.0.1.1 >> latencia-ping
}

teste4(){
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

run
start
conf-sw
conf-host
links
teste
