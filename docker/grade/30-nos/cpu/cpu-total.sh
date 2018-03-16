# /bin/bash
echo "Contador cpu$" >>"cpu-grade30-pcont-docker".ods
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
s7=`echo $sw7`
s8=`echo $sw8`
s9=`echo $sw9`
s10=`echo $sw10`
s11=`echo $sw11`
s12=`echo $sw12`
s13=`echo $sw13`
s14=`echo $sw14`
s15=`echo $sw15`
s16=`echo $sw16`
s17=`echo $sw17`
s18=`echo $sw18`
s19=`echo $sw19`
s20=`echo $sw20`
s21=`echo $sw21`
s22=`echo $sw22`
s23=`echo $sw23`
s24=`echo $sw24`
s25=`echo $sw25`
s26=`echo $sw26`
s27=`echo $sw27`
s28=`echo $sw28`
s29=`echo $sw29`

h0=`echo $ht0`
h1=`echo $ht1`



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
	sw7=`cat /sys/fs/cgroup/cpuacct/docker/$s7/cpuacct.usage`
	sw8=`cat /sys/fs/cgroup/cpuacct/docker/$s8/cpuacct.usage`
	sw9=`cat /sys/fs/cgroup/cpuacct/docker/$s9/cpuacct.usage`
	sw10=`cat /sys/fs/cgroup/cpuacct/docker/$s10/cpuacct.usage`
	sw11=`cat /sys/fs/cgroup/cpuacct/docker/$s11/cpuacct.usage`
	sw12=`cat /sys/fs/cgroup/cpuacct/docker/$s12/cpuacct.usage`
	sw13=`cat /sys/fs/cgroup/cpuacct/docker/$s13/cpuacct.usage`
	sw14=`cat /sys/fs/cgroup/cpuacct/docker/$s14/cpuacct.usage`
	sw15=`cat /sys/fs/cgroup/cpuacct/docker/$s15/cpuacct.usage`
	sw16=`cat /sys/fs/cgroup/cpuacct/docker/$s16/cpuacct.usage`
	sw17=`cat /sys/fs/cgroup/cpuacct/docker/$s17/cpuacct.usage`
	sw18=`cat /sys/fs/cgroup/cpuacct/docker/$s18/cpuacct.usage`
	sw19=`cat /sys/fs/cgroup/cpuacct/docker/$s19/cpuacct.usage`
	sw20=`cat /sys/fs/cgroup/cpuacct/docker/$s20/cpuacct.usage`
	sw21=`cat /sys/fs/cgroup/cpuacct/docker/$s21/cpuacct.usage`
	sw22=`cat /sys/fs/cgroup/cpuacct/docker/$s22/cpuacct.usage`
	sw23=`cat /sys/fs/cgroup/cpuacct/docker/$s23/cpuacct.usage`
	sw24=`cat /sys/fs/cgroup/cpuacct/docker/$s24/cpuacct.usage`
	sw25=`cat /sys/fs/cgroup/cpuacct/docker/$s25/cpuacct.usage`
	sw26=`cat /sys/fs/cgroup/cpuacct/docker/$s26/cpuacct.usage`
	sw27=`cat /sys/fs/cgroup/cpuacct/docker/$s27/cpuacct.usage`
	sw28=`cat /sys/fs/cgroup/cpuacct/docker/$s28/cpuacct.usage`
	sw29=`cat /sys/fs/cgroup/cpuacct/docker/$s29/cpuacct.usage`

	ht0=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht1=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`


	sleep 1

	c2=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw00=`cat /sys/fs/cgroup/cpuacct/docker/$s0/cpuacct.usage`
	sw01=`cat /sys/fs/cgroup/cpuacct/docker/$s1/cpuacct.usage`
	sw02=`cat /sys/fs/cgroup/cpuacct/docker/$s2/cpuacct.usage`
	sw03=`cat /sys/fs/cgroup/cpuacct/docker/$s3/cpuacct.usage`
	sw04=`cat /sys/fs/cgroup/cpuacct/docker/$s4/cpuacct.usage`
	sw05=`cat /sys/fs/cgroup/cpuacct/docker/$s5/cpuacct.usage`
	sw06=`cat /sys/fs/cgroup/cpuacct/docker/$s6/cpuacct.usage`
	sw07=`cat /sys/fs/cgroup/cpuacct/docker/$s7/cpuacct.usage`
	sw08=`cat /sys/fs/cgroup/cpuacct/docker/$s8/cpuacct.usage`
	sw09=`cat /sys/fs/cgroup/cpuacct/docker/$s9/cpuacct.usage`
	sw010=`cat /sys/fs/cgroup/cpuacct/docker/$s10/cpuacct.usage`
	sw011=`cat /sys/fs/cgroup/cpuacct/docker/$s11/cpuacct.usage`
	sw012=`cat /sys/fs/cgroup/cpuacct/docker/$s12/cpuacct.usage`
	sw013=`cat /sys/fs/cgroup/cpuacct/docker/$s13/cpuacct.usage`
	sw014=`cat /sys/fs/cgroup/cpuacct/docker/$s14/cpuacct.usage`
	sw015=`cat /sys/fs/cgroup/cpuacct/docker/$s15/cpuacct.usage`
	sw016=`cat /sys/fs/cgroup/cpuacct/docker/$s16/cpuacct.usage`
	sw017=`cat /sys/fs/cgroup/cpuacct/docker/$s17/cpuacct.usage`
	sw018=`cat /sys/fs/cgroup/cpuacct/docker/$s18/cpuacct.usage`
	sw019=`cat /sys/fs/cgroup/cpuacct/docker/$s19/cpuacct.usage`
	sw020=`cat /sys/fs/cgroup/cpuacct/docker/$s20/cpuacct.usage`
	sw021=`cat /sys/fs/cgroup/cpuacct/docker/$s21/cpuacct.usage`
	sw022=`cat /sys/fs/cgroup/cpuacct/docker/$s22/cpuacct.usage`
	sw023=`cat /sys/fs/cgroup/cpuacct/docker/$s23/cpuacct.usage`
	sw024=`cat /sys/fs/cgroup/cpuacct/docker/$s24/cpuacct.usage`
	sw025=`cat /sys/fs/cgroup/cpuacct/docker/$s25/cpuacct.usage`
	sw026=`cat /sys/fs/cgroup/cpuacct/docker/$s26/cpuacct.usage`
	sw027=`cat /sys/fs/cgroup/cpuacct/docker/$s27/cpuacct.usage`
	sw028=`cat /sys/fs/cgroup/cpuacct/docker/$s28/cpuacct.usage`
	sw029=`cat /sys/fs/cgroup/cpuacct/docker/$s29/cpuacct.usage`

	ht00=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht01=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`

	
	contr=`echo "scale=4 ; (($c2 - $c1)/$intervalo)*100"  | bc`
	stch0=`echo "scale=4 ; (($sw00 - $sw0)/$intervalo)*100"  | bc`
	stch1=`echo "scale=4 ; (($sw01 - $sw1)/$intervalo)*100"  | bc`
	stch2=`echo "scale=4 ; (($sw02 - $sw2)/$intervalo)*100"  | bc`
	stch3=`echo "scale=4 ; (($sw03 - $sw3)/$intervalo)*100"  | bc`
	stch4=`echo "scale=4 ; (($sw04 - $sw4)/$intervalo)*100"  | bc`
	stch5=`echo "scale=4 ; (($sw05 - $sw5)/$intervalo)*100"  | bc`
	stch6=`echo "scale=4 ; (($sw06 - $sw6)/$intervalo)*100"  | bc`
	stch7=`echo "scale=4 ; (($sw07 - $sw7)/$intervalo)*100"  | bc`
	stch8=`echo "scale=4 ; (($sw08 - $sw8)/$intervalo)*100"  | bc`
	stch9=`echo "scale=4 ; (($sw09 - $sw9)/$intervalo)*100"  | bc`
	stch10=`echo "scale=4 ; (($sw010 - $sw10)/$intervalo)*100"  | bc`
	stch11=`echo "scale=4 ; (($sw011 - $sw11)/$intervalo)*100"  | bc`
	stch12=`echo "scale=4 ; (($sw012 - $sw12)/$intervalo)*100"  | bc`
	stch13=`echo "scale=4 ; (($sw013 - $sw13)/$intervalo)*100"  | bc`
	stch14=`echo "scale=4 ; (($sw014 - $sw14)/$intervalo)*100"  | bc`
	stch15=`echo "scale=4 ; (($sw015 - $sw15)/$intervalo)*100"  | bc`
	stch16=`echo "scale=4 ; (($sw016 - $sw16)/$intervalo)*100"  | bc`
	stch17=`echo "scale=4 ; (($sw017 - $sw17)/$intervalo)*100"  | bc`
	stch18=`echo "scale=4 ; (($sw018 - $sw18)/$intervalo)*100"  | bc`
	stch19=`echo "scale=4 ; (($sw019 - $sw19)/$intervalo)*100"  | bc`
	stch20=`echo "scale=4 ; (($sw020 - $sw20)/$intervalo)*100"  | bc`
	stch21=`echo "scale=4 ; (($sw021 - $sw21)/$intervalo)*100"  | bc`
	stch22=`echo "scale=4 ; (($sw022 - $sw22)/$intervalo)*100"  | bc`
	stch23=`echo "scale=4 ; (($sw023 - $sw23)/$intervalo)*100"  | bc`
	stch24=`echo "scale=4 ; (($sw024 - $sw24)/$intervalo)*100"  | bc`
	stch25=`echo "scale=4 ; (($sw025 - $sw25)/$intervalo)*100"  | bc`
	stch26=`echo "scale=4 ; (($sw026 - $sw26)/$intervalo)*100"  | bc`
	stch27=`echo "scale=4 ; (($sw027 - $sw27)/$intervalo)*100"  | bc`
	stch28=`echo "scale=4 ; (($sw028 - $sw28)/$intervalo)*100"  | bc`
	stch29=`echo "scale=4 ; (($sw029 - $sw29)/$intervalo)*100"  | bc`

	host0=`echo "scale=4 ; (($ht00 - $ht0)/$intervalo)*100"  | bc`
	host1=`echo "scale=4 ; (($ht01 - $ht1)/$intervalo)*100"  | bc`


	#cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$stch7+$stch8+$stch9+$stch10+$stch11+$stch012+$stch13+$stch14+$stch15+$stch16+$stch17+$stch18+$stch19+$stch20+$stch21+$stch22+$stch23+$stch24+$stch25+$stch26+$stch27+$stch28+$stch29+$stch30+$host0+$host1+$host2+$host3+$host4+$host5+$host6+$host7+$host8+$host9+$host10+$host11+$host12+$host13+$host14+$host15)"  | bc`
	cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$stch7+$stch8+$stch9+$stch10+$stch11+$stch12+$stch13+$stch14+$stch15+$stch16+$stch17+$stch18+$stch19+$stch20+$stch21+$stch22+$stch23+$stch24+$stch25+$stch26+$stch27+$stch28+$stch29+$host0+$host1)" | bc`
	echo $cpu_total >>"cpu-grade30-pcont-docker".ods
	i=`expr $i + 1`
done
