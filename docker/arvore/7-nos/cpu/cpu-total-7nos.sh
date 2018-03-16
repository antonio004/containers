# /bin/bash
echo "Contador cpu$" >>"cpu-arvore7-docker".ods
i=0
tempo=300
c=`echo $cont`
s0=`echo $sw0`
s1=`echo $sw1`
s2=`echo $sw2`
s3=`echo $sw3`
s4=`echo $sw4`
s5=`echo $sw5`
s6=`echo $sw6`

h0=`echo $ht0`
h1=`echo $ht1`
h2=`echo $ht2`
h3=`echo $ht3`



intervalo=1000000000


while true 
do	
	c1=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw0=`cat /sys/fs/cgroup/cpuacct/docker/$s0/cpuacct.usage`
	sw1=`cat /sys/fs/cgroup/cpuacct/docker/$s1/cpuacct.usage`
	sw2=`cat /sys/fs/cgroup/cpuacct/docker/$s2/cpuacct.usage`
	sw3=`cat /sys/fs/cgroup/cpuacct/docker/$s3/cpuacct.usage`
	sw4=`cat /sys/fs/cgroup/cpuacct/docker/$s4/cpuacct.usage`
	sw5=`cat /sys/fs/cgroup/cpuacct/docker/$s5/cpuacct.usage`
	sw6=`cat /sys/fs/cgroup/cpuacct/docker/$s6/cpuacct.usage`

	ht0=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht1=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`
	ht2=`cat /sys/fs/cgroup/cpuacct/docker/$h2/cpuacct.usage`
	ht3=`cat /sys/fs/cgroup/cpuacct/docker/$h3/cpuacct.usage`


	sleep 1

	c2=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw00=`cat /sys/fs/cgroup/cpuacct/docker/$s0/cpuacct.usage`
	sw01=`cat /sys/fs/cgroup/cpuacct/docker/$s1/cpuacct.usage`
	sw02=`cat /sys/fs/cgroup/cpuacct/docker/$s2/cpuacct.usage`
	sw03=`cat /sys/fs/cgroup/cpuacct/docker/$s3/cpuacct.usage`
	sw04=`cat /sys/fs/cgroup/cpuacct/docker/$s4/cpuacct.usage`
	sw05=`cat /sys/fs/cgroup/cpuacct/docker/$s5/cpuacct.usage`
	sw06=`cat /sys/fs/cgroup/cpuacct/docker/$s6/cpuacct.usage`

	ht00=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht01=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`
	ht02=`cat /sys/fs/cgroup/cpuacct/docker/$h2/cpuacct.usage`
	ht03=`cat /sys/fs/cgroup/cpuacct/docker/$h3/cpuacct.usage`

	
	contr=`echo "scale=4 ; (($c2 - $c1)/$intervalo)*100"  | bc`
	stch0=`echo "scale=4 ; (($sw00 - $sw0)/$intervalo)*100"  | bc`
	stch1=`echo "scale=4 ; (($sw01 - $sw1)/$intervalo)*100"  | bc`
	stch2=`echo "scale=4 ; (($sw02 - $sw2)/$intervalo)*100"  | bc`
	stch3=`echo "scale=4 ; (($sw03 - $sw3)/$intervalo)*100"  | bc`
	stch4=`echo "scale=4 ; (($sw04 - $sw4)/$intervalo)*100"  | bc`
	stch5=`echo "scale=4 ; (($sw05 - $sw5)/$intervalo)*100"  | bc`
	stch6=`echo "scale=4 ; (($sw06 - $sw6)/$intervalo)*100"  | bc`

	host0=`echo "scale=4 ; (($ht00 - $ht0)/$intervalo)*100"  | bc`
	host1=`echo "scale=4 ; (($ht01 - $ht1)/$intervalo)*100"  | bc`
	host2=`echo "scale=4 ; (($ht02 - $ht2)/$intervalo)*100"  | bc`
	host3=`echo "scale=4 ; (($ht03 - $ht3)/$intervalo)*100"  | bc`


	#cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$stch7+$stch8+$stch9+$stch10+$stch11+$stch012+$stch13+$stch14+$stch15+$stch16+$stch17+$stch18+$stch19+$stch20+$stch21+$stch22+$stch23+$stch24+$stch25+$stch26+$stch27+$stch28+$stch29+$stch30+$host0+$host1+$host2+$host3+$host4+$host5+$host6+$host7+$host8+$host9+$host10+$host11+$host12+$host13+$host14+$host15)"  | bc`
	cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$host0+$host1+$host2+$host3)" | bc`
	echo $cpu_total >>"cpu-arvore7-docker".ods
	i=`expr $i + 1`
done
