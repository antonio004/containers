# /bin/bash
echo "Contador cpu$" >>"cpu-pcont-linear5-containers".ods
i=0
c="ff02d2f802a0c217bcc6dee525432754f8d6dc897867a7302d2afea288a2811c"
s0="c1a5687257beff51c67b4057ddfaf96eb55459b8dbd9241cc24f4e9fbe110441"
s1="489c50e5237a5a12774ee73b125d4162bf8b844d3b2323188c4b2ebe158d6a6a"
s2="1413315ae9fd3777aa9be86686f80978ecf0fdac967bea340adfb0574c808115"
s3="28445e43fca4503dde4ba0eaaae0de69d51344d28b43e301ea7f31f3eb23fe11"
s4="f05dbea2e4f0b2229ae3c2c0fed0dd2c22622aa542d504291015edd0d7f6901f"
h0="43e28a9bb302f35b0830b3535241f179ed1b27c6c836662df7c0b033edd7c130"
h1="fe54361aa53db138ae440bb37027e5212791cd84da947a19ac20b462c688cd41"



intervalo=1000000000


while true 
do	
	c1=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw0=`cat /sys/fs/cgroup/cpuacct/docker/$s0/cpuacct.usage`
	sw1=`cat /sys/fs/cgroup/cpuacct/docker/$s1/cpuacct.usage`
	sw2=`cat /sys/fs/cgroup/cpuacct/docker/$s2/cpuacct.usage`
	sw3=`cat /sys/fs/cgroup/cpuacct/docker/$s3/cpuacct.usage`
	sw4=`cat /sys/fs/cgroup/cpuacct/docker/$s4/cpuacct.usage`


	ht0=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht1=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`


	sleep 1

	c2=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw00=`cat /sys/fs/cgroup/cpuacct/docker/$s0/cpuacct.usage`
	sw01=`cat /sys/fs/cgroup/cpuacct/docker/$s1/cpuacct.usage`
	sw02=`cat /sys/fs/cgroup/cpuacct/docker/$s2/cpuacct.usage`
	sw03=`cat /sys/fs/cgroup/cpuacct/docker/$s3/cpuacct.usage`
	sw04=`cat /sys/fs/cgroup/cpuacct/docker/$s4/cpuacct.usage`

	ht00=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht01=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`

	
	contr=`echo "scale=4 ; (($c2 - $c1)/$intervalo)*100"  | bc`
	stch0=`echo "scale=4 ; (($sw00 - $sw0)/$intervalo)*100"  | bc`
	stch1=`echo "scale=4 ; (($sw01 - $sw1)/$intervalo)*100"  | bc`
	stch2=`echo "scale=4 ; (($sw02 - $sw2)/$intervalo)*100"  | bc`
	stch3=`echo "scale=4 ; (($sw03 - $sw3)/$intervalo)*100"  | bc`
	stch4=`echo "scale=4 ; (($sw04 - $sw4)/$intervalo)*100"  | bc`

	host0=`echo "scale=4 ; (($ht00 - $ht0)/$intervalo)*100"  | bc`
	host1=`echo "scale=4 ; (($ht01 - $ht1)/$intervalo)*100"  | bc`


	echo $contr $stch0 $stch1 $stch2 $stch3 $stch4 $host0 $host1>>"cpu-pcont-linear5-containers".ods

	#echo $i $contr $stch0 $stch1 $stch2 $stch3 $stch4 $stch5 $stch6 $stch7 $stch8 $stch9 $stch10 $stch11 $stch12 $stch13 $stch14 $stch15 $stch16 $stch17 $stch18 $stch19 $stch20 $stch21 $stch22 $stch23 $stch24 $stch25 $stch26 $stch27 $stch28 $stch29 $stch30 $host0 $host1 $host2 $host3 $host4 $host5 $host6 $host7 $host8 $host9 $host10 $host11 $host12 $host13 $host14 $host15 >>"cpu-tree-containers".ods
	i=`expr $i + 1`
done
