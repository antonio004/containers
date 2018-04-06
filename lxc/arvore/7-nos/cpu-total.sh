# /bin/bash
echo "Contador cpu$" #>>"cpu-rnp".ods
i=0
c="6c3c64348b28733acbc22108e9bdc53293bf7b018f79e03c901aa6270553aa75"



intervalo=1000000000


while true 
do	
	c1=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw0=`cat /sys/fs/cgroup/cpuacct/lxc/sw0/cpuacct.usage`
	sw1=`cat /sys/fs/cgroup/cpuacct/lxc/sw1/cpuacct.usage`
	sw2=`cat /sys/fs/cgroup/cpuacct/lxc/sw2/cpuacct.usage`
	sw3=`cat /sys/fs/cgroup/cpuacct/lxc/sw3/cpuacct.usage`
	sw4=`cat /sys/fs/cgroup/cpuacct/lxc/sw4/cpuacct.usage`
	sw5=`cat /sys/fs/cgroup/cpuacct/lxc/sw5/cpuacct.usage`
	sw6=`cat /sys/fs/cgroup/cpuacct/lxc/sw6/cpuacct.usage`
	#sw7=`cat /sys/fs/cgroup/cpuacct/lxc/sw7/cpuacct.usage`
	#sw8=`cat /sys/fs/cgroup/cpuacct/lxc/sw8/cpuacct.usage`
	#sw9=`cat /sys/fs/cgroup/cpuacct/lxc/sw9/cpuacct.usage`
	#sw10=`cat /sys/fs/cgroup/cpuacct/lxc/sw10/cpuacct.usage`
	#sw11=`cat /sys/fs/cgroup/cpuacct/lxc/sw11/cpuacct.usage`
	#sw12=`cat /sys/fs/cgroup/cpuacct/lxc/sw12/cpuacct.usage`
	#sw13=`cat /sys/fs/cgroup/cpuacct/lxc/sw13/cpuacct.usage`
	#sw14=`cat /sys/fs/cgroup/cpuacct/lxc/sw14/cpuacct.usage`
	#sw15=`cat /sys/fs/cgroup/cpuacct/lxc/sw15/cpuacct.usage`
	#sw16=`cat /sys/fs/cgroup/cpuacct/lxc/sw16/cpuacct.usage`
	#sw17=`cat /sys/fs/cgroup/cpuacct/lxc/sw17/cpuacct.usage`
	#sw18=`cat /sys/fs/cgroup/cpuacct/lxc/sw18/cpuacct.usage`
	#sw19=`cat /sys/fs/cgroup/cpuacct/lxc/sw19/cpuacct.usage`
	#sw20=`cat /sys/fs/cgroup/cpuacct/lxc/sw20/cpuacct.usage`
	#sw21=`cat /sys/fs/cgroup/cpuacct/lxc/sw21/cpuacct.usage`
	#sw22=`cat /sys/fs/cgroup/cpuacct/lxc/sw22/cpuacct.usage`
	#sw23=`cat /sys/fs/cgroup/cpuacct/lxc/sw23/cpuacct.usage`
	#sw24=`cat /sys/fs/cgroup/cpuacct/lxc/sw24/cpuacct.usage`
	#sw25=`cat /sys/fs/cgroup/cpuacct/lxc/sw25/cpuacct.usage`
	#sw26=`cat /sys/fs/cgroup/cpuacct/lxc/sw26/cpuacct.usage`
	#sw27=`cat /sys/fs/cgroup/cpuacct/lxc/sw27/cpuacct.usage`
	#sw28=`cat /sys/fs/cgroup/cpuacct/lxc/sw28/cpuacct.usage`
	#sw29=`cat /sys/fs/cgroup/cpuacct/lxc/sw29/cpuacct.usage`
	#sw30=`cat /sys/fs/cgroup/cpuacct/lxc/sw30/cpuacct.usage`
	ht0=`cat /sys/fs/cgroup/cpuacct/lxc/h0/cpuacct.usage`
	ht1=`cat /sys/fs/cgroup/cpuacct/lxc/h1/cpuacct.usage`
	ht2=`cat /sys/fs/cgroup/cpuacct/lxc/h2/cpuacct.usage`
	ht3=`cat /sys/fs/cgroup/cpuacct/lxc/h3/cpuacct.usage`
	#ht4=`cat /sys/fs/cgroup/cpuacct/lxc/h4/cpuacct.usage`
	#ht5=`cat /sys/fs/cgroup/cpuacct/lxc/h5/cpuacct.usage`
	#ht6=`cat /sys/fs/cgroup/cpuacct/lxc/h6/cpuacct.usage`
	#ht7=`cat /sys/fs/cgroup/cpuacct/lxc/h7/cpuacct.usage`
	#ht8=`cat /sys/fs/cgroup/cpuacct/lxc/h8/cpuacct.usage`
	#ht9=`cat /sys/fs/cgroup/cpuacct/lxc/h9/cpuacct.usage`
	#ht10=`cat /sys/fs/cgroup/cpuacct/lxc/h10/cpuacct.usage`
	#ht11=`cat /sys/fs/cgroup/cpuacct/lxc/h11/cpuacct.usage`
	#ht12=`cat /sys/fs/cgroup/cpuacct/lxc/h12/cpuacct.usage`
	#ht13=`cat /sys/fs/cgroup/cpuacct/lxc/h13/cpuacct.usage`
	#ht14=`cat /sys/fs/cgroup/cpuacct/lxc/h14/cpuacct.usage`
	#ht15=`cat /sys/fs/cgroup/cpuacct/lxc/h15/cpuacct.usage`

	sleep 1

	c2=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw00=`cat /sys/fs/cgroup/cpuacct/lxc/sw0/cpuacct.usage`
	sw01=`cat /sys/fs/cgroup/cpuacct/lxc/sw1/cpuacct.usage`
	sw02=`cat /sys/fs/cgroup/cpuacct/lxc/sw2/cpuacct.usage`
	sw03=`cat /sys/fs/cgroup/cpuacct/lxc/sw3/cpuacct.usage`
	sw04=`cat /sys/fs/cgroup/cpuacct/lxc/sw4/cpuacct.usage`
	sw05=`cat /sys/fs/cgroup/cpuacct/lxc/sw5/cpuacct.usage`
	sw06=`cat /sys/fs/cgroup/cpuacct/lxc/sw6/cpuacct.usage`
	#sw07=`cat /sys/fs/cgroup/cpuacct/lxc/sw7/cpuacct.usage`
	#sw08=`cat /sys/fs/cgroup/cpuacct/lxc/sw8/cpuacct.usage`
	#sw09=`cat /sys/fs/cgroup/cpuacct/lxc/sw9/cpuacct.usage`
	#sw010=`cat /sys/fs/cgroup/cpuacct/lxc/sw10/cpuacct.usage`
	#sw011=`cat /sys/fs/cgroup/cpuacct/lxc/sw11/cpuacct.usage`
	#sw012=`cat /sys/fs/cgroup/cpuacct/lxc/sw12/cpuacct.usage`
	#sw013=`cat /sys/fs/cgroup/cpuacct/lxc/sw13/cpuacct.usage`
	#sw014=`cat /sys/fs/cgroup/cpuacct/lxc/sw14/cpuacct.usage`
	#sw015=`cat /sys/fs/cgroup/cpuacct/lxc/sw15/cpuacct.usage`
	#sw016=`cat /sys/fs/cgroup/cpuacct/lxc/sw16/cpuacct.usage`
	#sw017=`cat /sys/fs/cgroup/cpuacct/lxc/sw17/cpuacct.usage`
	#sw018=`cat /sys/fs/cgroup/cpuacct/lxc/sw18/cpuacct.usage`
	#sw019=`cat /sys/fs/cgroup/cpuacct/lxc/sw19/cpuacct.usage`
	#sw020=`cat /sys/fs/cgroup/cpuacct/lxc/sw20/cpuacct.usage`
	#sw021=`cat /sys/fs/cgroup/cpuacct/lxc/sw21/cpuacct.usage`
	#sw022=`cat /sys/fs/cgroup/cpuacct/lxc/sw22/cpuacct.usage`
	#sw023=`cat /sys/fs/cgroup/cpuacct/lxc/sw23/cpuacct.usage`
	#sw024=`cat /sys/fs/cgroup/cpuacct/lxc/sw24/cpuacct.usage`
	#sw025=`cat /sys/fs/cgroup/cpuacct/lxc/sw25/cpuacct.usage`
	#sw026=`cat /sys/fs/cgroup/cpuacct/lxc/sw26/cpuacct.usage`
	#sw027=`cat /sys/fs/cgroup/cpuacct/lxc/sw27/cpuacct.usage`
	#sw028=`cat /sys/fs/cgroup/cpuacct/lxc/sw28/cpuacct.usage`
	#sw029=`cat /sys/fs/cgroup/cpuacct/lxc/sw29/cpuacct.usage`
	#sw030=`cat /sys/fs/cgroup/cpuacct/lxc/sw30/cpuacct.usage`
	ht00=`cat /sys/fs/cgroup/cpuacct/lxc/h0/cpuacct.usage`
	ht01=`cat /sys/fs/cgroup/cpuacct/lxc/h1/cpuacct.usage`
	ht02=`cat /sys/fs/cgroup/cpuacct/lxc/h2/cpuacct.usage`
	ht03=`cat /sys/fs/cgroup/cpuacct/lxc/h3/cpuacct.usage`
	#ht04=`cat /sys/fs/cgroup/cpuacct/lxc/h4/cpuacct.usage`
	#ht05=`cat /sys/fs/cgroup/cpuacct/lxc/h5/cpuacct.usage`
	#ht06=`cat /sys/fs/cgroup/cpuacct/lxc/h6/cpuacct.usage`
	#ht07=`cat /sys/fs/cgroup/cpuacct/lxc/h7/cpuacct.usage`
	#ht08=`cat /sys/fs/cgroup/cpuacct/lxc/h8/cpuacct.usage`
	#ht09=`cat /sys/fs/cgroup/cpuacct/lxc/h9/cpuacct.usage`
	#ht010=`cat /sys/fs/cgroup/cpuacct/lxc/h10/cpuacct.usage`
	#ht011=`cat /sys/fs/cgroup/cpuacct/lxc/h11/cpuacct.usage`
	#ht012=`cat /sys/fs/cgroup/cpuacct/lxc/h12/cpuacct.usage`
	#ht013=`cat /sys/fs/cgroup/cpuacct/lxc/h13/cpuacct.usage`
	#ht014=`cat /sys/fs/cgroup/cpuacct/lxc/h14/cpuacct.usage`
	#ht015=`cat /sys/fs/cgroup/cpuacct/lxc/h15/cpuacct.usage`
	
	contr=`echo "scale=4 ; (($c2 - $c1)/$intervalo)*100"  | bc`
	stch0=`echo "scale=4 ; (($sw00 - $sw0)/$intervalo)*100"  | bc`
	stch1=`echo "scale=4 ; (($sw01 - $sw1)/$intervalo)*100"  | bc`
	stch2=`echo "scale=4 ; (($sw02 - $sw2)/$intervalo)*100"  | bc`
	stch3=`echo "scale=4 ; (($sw03 - $sw3)/$intervalo)*100"  | bc`
	stch4=`echo "scale=4 ; (($sw04 - $sw4)/$intervalo)*100"  | bc`
	stch5=`echo "scale=4 ; (($sw05 - $sw5)/$intervalo)*100"  | bc`
	stch6=`echo "scale=4 ; (($sw06 - $sw6)/$intervalo)*100"  | bc`
	#stch7=`echo "scale=4 ; (($sw07 - $sw7)/$intervalo)*100"  | bc`
	#stch8=`echo "scale=4 ; (($sw08 - $sw8)/$intervalo)*100"  | bc`
	#stch9=`echo "scale=4 ; (($sw09 - $sw9)/$intervalo)*100"  | bc`
	#stch10=`echo "scale=4 ; (($sw010 - $sw10)/$intervalo)*100"  | bc`
	#stch11=`echo "scale=4 ; (($sw011 - $sw11)/$intervalo)*100"  | bc`
	#stch12=`echo "scale=4 ; (($sw012 - $sw12)/$intervalo)*100"  | bc`
	#stch13=`echo "scale=4 ; (($sw013 - $sw13)/$intervalo)*100"  | bc`
	#stch14=`echo "scale=4 ; (($sw014 - $sw14)/$intervalo)*100"  | bc`
	#stch15=`echo "scale=4 ; (($sw015 - $sw15)/$intervalo)*100"  | bc`
	#stch16=`echo "scale=4 ; (($sw016 - $sw16)/$intervalo)*100"  | bc`
	#stch17=`echo "scale=4 ; (($sw017 - $sw17)/$intervalo)*100"  | bc`
	#stch18=`echo "scale=4 ; (($sw018 - $sw18)/$intervalo)*100"  | bc`
	#stch19=`echo "scale=4 ; (($sw019 - $sw19)/$intervalo)*100"  | bc`
	#stch20=`echo "scale=4 ; (($sw020 - $sw20)/$intervalo)*100"  | bc`
	#stch21=`echo "scale=4 ; (($sw021 - $sw21)/$intervalo)*100"  | bc`
	#stch22=`echo "scale=4 ; (($sw022 - $sw22)/$intervalo)*100"  | bc`
	#stch23=`echo "scale=4 ; (($sw023 - $sw23)/$intervalo)*100"  | bc`
	#stch24=`echo "scale=4 ; (($sw024 - $sw24)/$intervalo)*100"  | bc`
	#stch25=`echo "scale=4 ; (($sw025 - $sw25)/$intervalo)*100"  | bc`
	#stch26=`echo "scale=4 ; (($sw026 - $sw26)/$intervalo)*100"  | bc`
	#stch27=`echo "scale=4 ; (($sw027 - $sw27)/$intervalo)*100"  | bc`
	#stch28=`echo "scale=4 ; (($sw028 - $sw28)/$intervalo)*100"  | bc`
	#stch29=`echo "scale=4 ; (($sw029 - $sw29)/$intervalo)*100"  | bc`
	#stch30=`echo "scale=4 ; (($sw030 - $sw30)/$intervalo)*100"  | bc`
	host0=`echo "scale=4 ; (($ht00 - $ht0)/$intervalo)*100"  | bc`
	host1=`echo "scale=4 ; (($ht01 - $ht1)/$intervalo)*100"  | bc`
	host2=`echo "scale=4 ; (($ht02 - $ht2)/$intervalo)*100"  | bc`
	host3=`echo "scale=4 ; (($ht03 - $ht3)/$intervalo)*100"  | bc`
	#host4=`echo "scale=4 ; (($ht04 - $ht4)/$intervalo)*100"  | bc`
	#host5=`echo "scale=4 ; (($ht05 - $ht5)/$intervalo)*100"  | bc`
	#host6=`echo "scale=4 ; (($ht06 - $ht6)/$intervalo)*100"  | bc`
	#host7=`echo "scale=4 ; (($ht07 - $ht7)/$intervalo)*100"  | bc`
	#host8=`echo "scale=4 ; (($ht08 - $ht8)/$intervalo)*100"  | bc`
	#host9=`echo "scale=4 ; (($ht09 - $ht9)/$intervalo)*100"  | bc`
	#host10=`echo "scale=4 ; (($ht010 - $ht10)/$intervalo)*100"  | bc`
	#host11=`echo "scale=4 ; (($ht011 - $ht11)/$intervalo)*100"  | bc`
	#host12=`echo "scale=4 ; (($ht012 - $ht12)/$intervalo)*100"  | bc`
	#host13=`echo "scale=4 ; (($ht013 - $ht13)/$intervalo)*100"  | bc`
	#host14=`echo "scale=4 ; (($ht014 - $ht14)/$intervalo)*100"  | bc`
	#host15=`echo "scale=4 ; (($ht015 - $ht15)/$intervalo)*100"  | bc`
	
	cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$host0+$host1+$host2+$host3)"  | bc`
	echo $cpu_total >>"cpu-arvore-7".ods
	i=`expr $i + 1`
done
