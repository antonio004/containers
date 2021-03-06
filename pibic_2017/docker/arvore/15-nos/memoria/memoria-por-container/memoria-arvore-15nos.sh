# /bin/bash
echo "Contador Consumo" >>"topologia-tree-containers-memoria-lxc".ods
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


intervalo=1048576


while [ $i -lt $tempo ]
do
	val0=`cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes`
	val1=`cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes`
	val2=`cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes`
	val3=`cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes`
	val4=`cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes`
	val5=`cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes`
	val6=`cat /sys/fs/cgroup/memory/docker/$s5/memory.usage_in_bytes`
	val7=`cat /sys/fs/cgroup/memory/docker/$s6/memory.usage_in_bytes`
	val8=`cat /sys/fs/cgroup/memory/docker/$s7/memory.usage_in_bytes`
	val9=`cat /sys/fs/cgroup/memory/docker/$s8/memory.usage_in_bytes`
	val10=`cat /sys/fs/cgroup/memory/docker/$s9/memory.usage_in_bytes`
	val11=`cat /sys/fs/cgroup/memory/docker/$s10/memory.usage_in_bytes`
	val12=`cat /sys/fs/cgroup/memory/docker/$s11/memory.usage_in_bytes`
	val13=`cat /sys/fs/cgroup/memory/docker/$s12/memory.usage_in_bytes`
	val14=`cat /sys/fs/cgroup/memory/docker/$s13/memory.usage_in_bytes`
	val15=`cat /sys/fs/cgroup/memory/docker/$s14/memory.usage_in_bytes`

	val32=`cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes`
	val33=`cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes`
	val34=`cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes`
	val35=`cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes`
	val36=`cat /sys/fs/cgroup/memory/docker/$h4/memory.usage_in_bytes`
	val37=`cat /sys/fs/cgroup/memory/docker/$h5/memory.usage_in_bytes`
	val38=`cat /sys/fs/cgroup/memory/docker/$h6/memory.usage_in_bytes`
	val39=`cat /sys/fs/cgroup/memory/docker/$h7/memory.usage_in_bytes`


	resul0=`echo "scale=4 ; (($val0)/$intervalo)" | bc`
	resul1=`echo "scale=4 ; (($val1)/$intervalo)" | bc`
	resul2=`echo "scale=4 ; (($val2)/$intervalo)" | bc`
	resul3=`echo "scale=4 ; (($val3)/$intervalo)" | bc`
	resul4=`echo "scale=4 ; (($val4)/$intervalo)" | bc`
	resul5=`echo "scale=4 ; (($val5)/$intervalo)" | bc`
	resul6=`echo "scale=4 ; (($val6)/$intervalo)" | bc`
	resul7=`echo "scale=4 ; (($val7)/$intervalo)" | bc`
	resul8=`echo "scale=4 ; (($val8)/$intervalo)" | bc`
	resul9=`echo "scale=4 ; (($val9)/$intervalo)" | bc`
	resul10=`echo "scale=4 ; (($val10)/$intervalo)" | bc`
	resul11=`echo "scale=4 ; (($val11)/$intervalo)" | bc`
	resul12=`echo "scale=4 ; (($val12)/$intervalo)" | bc`
	resul13=`echo "scale=4 ; (($val13)/$intervalo)" | bc`
	resul14=`echo "scale=4 ; (($val14)/$intervalo)" | bc`
	resul15=`echo "scale=4 ; (($val15)/$intervalo)" | bc`

	resul32=`echo "scale=4 ; (($val32)/$intervalo)" | bc`
	resul33=`echo "scale=4 ; (($val33)/$intervalo)" | bc`
	resul34=`echo "scale=4 ; (($val34)/$intervalo)" | bc`
	resul35=`echo "scale=4 ; (($val35)/$intervalo)" | bc`
	resul36=`echo "scale=4 ; (($val36)/$intervalo)" | bc`
	resul37=`echo "scale=4 ; (($val37)/$intervalo)" | bc`
	resul38=`echo "scale=4 ; (($val38)/$intervalo)" | bc`
	resul39=`echo "scale=4 ; (($val39)/$intervalo)" | bc`




	echo $i $resul0 $resul1 $resul2 $resul3 $resul4 $resul5 $resul6 $resul7 $resul8 $resul9 $resul10 $resul11 $resul12 $resul13 $resul14 $resul15 $resul32 $resul33 $resul34 $resul35 $resul36 $resul37 $resul38 $resul39 >>"topologia-tree-containers-memoria-lxc".ods
	sleep 2
	i=`expr $i + 1`
done
