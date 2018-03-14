# /bin/bash
echo "Contador Consumo" >>"topologia-linear5-containers".ods
i=0
tempo=300
c="ff02d2f802a0c217bcc6dee525432754f8d6dc897867a7302d2afea288a2811c"
s0="c1a5687257beff51c67b4057ddfaf96eb55459b8dbd9241cc24f4e9fbe110441"
s1="489c50e5237a5a12774ee73b125d4162bf8b844d3b2323188c4b2ebe158d6a6a"
s2="1413315ae9fd3777aa9be86686f80978ecf0fdac967bea340adfb0574c808115"
s3="28445e43fca4503dde4ba0eaaae0de69d51344d28b43e301ea7f31f3eb23fe11"
s4="f05dbea2e4f0b2229ae3c2c0fed0dd2c22622aa542d504291015edd0d7f6901f"

h0="43e28a9bb302f35b0830b3535241f179ed1b27c6c836662df7c0b033edd7c130"
h1="fe54361aa53db138ae440bb37027e5212791cd84da947a19ac20b462c688cd41"


intervalo=1048576


while [ $i -lt $tempo ]
do
	val0=`cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes`
	val1=`cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes`
	val2=`cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes`
	val3=`cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes`
	val4=`cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes`
	val5=`cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes`

	val32=`cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes`
	val33=`cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes`


	resul0=`echo "scale=4 ; (($val0)/$intervalo)" | bc`
	resul1=`echo "scale=4 ; (($val1)/$intervalo)" | bc`
	resul2=`echo "scale=4 ; (($val2)/$intervalo)" | bc`
	resul3=`echo "scale=4 ; (($val3)/$intervalo)" | bc`
	resul4=`echo "scale=4 ; (($val4)/$intervalo)" | bc`
	resul5=`echo "scale=4 ; (($val5)/$intervalo)" | bc`

	resul32=`echo "scale=4 ; (($val32)/$intervalo)" | bc`
	resul33=`echo "scale=4 ; (($val33)/$intervalo)" | bc`




	echo $i $resul0 $resul1 $resul2 $resul3 $resul4 $resul5 $resul32 >>"topologia-linear5-containers".ods
	sleep 2
	i=`expr $i + 1`
done
