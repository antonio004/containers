# /bin/bash
echo "Contador cpu$" >>"cpu-tree-docker".ods
i=0
tempo=300
c="868960935bf91c47fb6ba447f7d06432242298dd88a13c59d0cfb5fdd1ea8473"
s0="c1a5687257beff51c67b4057ddfaf96eb55459b8dbd9241cc24f4e9fbe110441"
s1="489c50e5237a5a12774ee73b125d4162bf8b844d3b2323188c4b2ebe158d6a6a"
s2="1413315ae9fd3777aa9be86686f80978ecf0fdac967bea340adfb0574c808115"
s3="28445e43fca4503dde4ba0eaaae0de69d51344d28b43e301ea7f31f3eb23fe11"
s4="f05dbea2e4f0b2229ae3c2c0fed0dd2c22622aa542d504291015edd0d7f6901f"
s5="e594310b5d3a48664b2eb286d279fb3d197d3bc0f2bc0a3c038ea2395c455b67"
s6="fbb518f082d160162d723f234c2a6912ecd549ff5a86754ed1e814c41b8b6673"
s7="1edbc450c9c12224bbf842de0c3d2e4afce4f49406e91f7155abad8c3f68cd6d"
s8="9f1659a44b6192169e91dca5f1084a38a14050b51f74ed0fc28738e9fc23726c"
s9="0dbcebb3480aa374510db183d0f23c4bf8eef532420ccf21e33e4b7be8e12056"
s10="bf7b8e6f2f08ec25cb2359e4134a113d4132247656483c1e2b6629a558376812"
s11="69733974bc3a442f0af09e198bd6ca7dd70e609e8434774e7835028f2599af44"
s12="ba1436867ddd8c3cd1cb8de3fcfb992e3b4edaeea1fa1f1c963efa822313fe74"
s13="afa63ccac85c0437e98c51bcd58d98685366911a1a5f7d0f4a97b93a778c2e44"
s14="b6e34c60ae0cc74e0797dfcb258d673d41d7daa46661373af310647bf9c6232a"

h0="43e28a9bb302f35b0830b3535241f179ed1b27c6c836662df7c0b033edd7c130"
h1="fe54361aa53db138ae440bb37027e5212791cd84da947a19ac20b462c688cd41"
h2="8deaa76ec9eadd58edc1846967475e5ef4af946793b4a4771898f1ece2527f20"
h3="34d4cf6eecb4ea6027cd46e4f100cd21ece7ccab3ba8c011ce17d6bc2560f576"
h4="ce33dc1be2ee3b2f2a63bb0387a8167c01109dbb356e6f16b196aad95bdddc68"
h5="69448a622c4f7615def77971e3f37b47e729edca4dabdb0d6b032209d4f39539"
h6="1362b76b430d2a656f9030a849fbfd578eb439015072322fd584553cbc09f330"
h7="271c335888bb0d5de6302beef87c8e567cfc7aab1d228f1fa3f34e38f0192420"


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

	ht0=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht1=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`
	ht2=`cat /sys/fs/cgroup/cpuacct/docker/$h2/cpuacct.usage`
	ht3=`cat /sys/fs/cgroup/cpuacct/docker/$h3/cpuacct.usage`
	ht4=`cat /sys/fs/cgroup/cpuacct/docker/$h4/cpuacct.usage`
	ht5=`cat /sys/fs/cgroup/cpuacct/docker/$h5/cpuacct.usage`
	ht6=`cat /sys/fs/cgroup/cpuacct/docker/$h6/cpuacct.usage`
	ht7=`cat /sys/fs/cgroup/cpuacct/docker/$h7/cpuacct.usage`


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

	ht00=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht01=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`
	ht02=`cat /sys/fs/cgroup/cpuacct/docker/$h2/cpuacct.usage`
	ht03=`cat /sys/fs/cgroup/cpuacct/docker/$h3/cpuacct.usage`
	ht04=`cat /sys/fs/cgroup/cpuacct/docker/$h4/cpuacct.usage`
	ht05=`cat /sys/fs/cgroup/cpuacct/docker/$h5/cpuacct.usage`
	ht06=`cat /sys/fs/cgroup/cpuacct/docker/$h6/cpuacct.usage`
	ht07=`cat /sys/fs/cgroup/cpuacct/docker/$h7/cpuacct.usage`

	
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
	
	host0=`echo "scale=4 ; (($ht00 - $ht0)/$intervalo)*100"  | bc`
	host1=`echo "scale=4 ; (($ht01 - $ht1)/$intervalo)*100"  | bc`
	host2=`echo "scale=4 ; (($ht02 - $ht2)/$intervalo)*100"  | bc`
	host3=`echo "scale=4 ; (($ht03 - $ht3)/$intervalo)*100"  | bc`
	host4=`echo "scale=4 ; (($ht04 - $ht4)/$intervalo)*100"  | bc`
	host5=`echo "scale=4 ; (($ht05 - $ht5)/$intervalo)*100"  | bc`
	host6=`echo "scale=4 ; (($ht06 - $ht6)/$intervalo)*100"  | bc`
	host7=`echo "scale=4 ; (($ht07 - $ht7)/$intervalo)*100"  | bc`


	#cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$stch7+$stch8+$stch9+$stch10+$stch11+$stch012+$stch13+$stch14+$stch15+$stch16+$stch17+$stch18+$stch19+$stch20+$stch21+$stch22+$stch23+$stch24+$stch25+$stch26+$stch27+$stch28+$stch29+$stch30+$host0+$host1+$host2+$host3+$host4+$host5+$host6+$host7+$host8+$host9+$host10+$host11+$host12+$host13+$host14+$host15)"  | bc`
	cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$stch7+$stch8+$stch9+$stch10+$stch11+$stch12+$stch13+$stch14+$host0+$host1+$host2+$host3+$host4+$host5+$host6+$host7)" | bc`
	echo $i $cpu_total >>"cpu-tree-docker".ods
	i=`expr $i + 1`
done
