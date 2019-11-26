# /bin/bash
echo "Contador Consumo" >>"topologia-tree-containers-memoria31".ods
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
s15="7e238083a2b16d79564e69612375e2650f90dce7d0f2753cdec3a7c143ccf76f"
s16="ece2469bb98e43085ded1f1a292e0044f6c031711c8a293894a42c3569ca1a01"
s17="04637c05ee6a03212de8bf4fcd11d4676353d45fe4acf7672ff8e6d347d01906"
s18="d37a9d27d344d20c32fe3f2cc3a0e17bf8b2fef6238cc2175d55a21b178f2909"
s19="11adee749063b62ee561293bbb3255384db5a9f9fff62263203c1be40381d651"
s20="676ab7eadf07d3408974370a3db22b2f1244ce96015fa0782866de10d3e8111f"
s21="4d5a5595248adc0b6a32f92e0988a738df0937466417f76f54002715433c007b"
s22="8b507b7afa37e0205870e03353f1177a61ddf7b4ad86201bcae25ff4ac88a830"
s23="ba17e52bb0303b39d49b9e0b0afdf92afef9cb7eafb522501e70894ee16bba3e"
s24="ce6fc7bac7f3f743af725383e042d83784cb8871d999651c29a2f00f14e31b32"
s25="ead432a052d4114f89ca99229ce551699f9ac572c49daa482356b5735912881a"
s26="feb57aafb32dbc5af553a9753c250958914c6a804dacc4540d9c78c494820350"
s27="d03be7f1997051083ea8e4d619fab60901a3d305da24b274119d8ae962f2d43a"
s28="a95e77cac68beb584bc76722965c7a15b95223cabbac9e1651162d191fb1252a"
s29="464b810f0ec82c0d9f9c87a23ea2e91e25dc7878c2cb8d2fd24645a9ca007b63"
s30="3a98b93c89851d275d6b74c5f9fa262d723037752d91ca784b4932ec283c9c72"
h0="43e28a9bb302f35b0830b3535241f179ed1b27c6c836662df7c0b033edd7c130"
h1="fe54361aa53db138ae440bb37027e5212791cd84da947a19ac20b462c688cd41"
h2="8deaa76ec9eadd58edc1846967475e5ef4af946793b4a4771898f1ece2527f20"
h3="34d4cf6eecb4ea6027cd46e4f100cd21ece7ccab3ba8c011ce17d6bc2560f576"
h4="ce33dc1be2ee3b2f2a63bb0387a8167c01109dbb356e6f16b196aad95bdddc68"
h5="69448a622c4f7615def77971e3f37b47e729edca4dabdb0d6b032209d4f39539"
h6="1362b76b430d2a656f9030a849fbfd578eb439015072322fd584553cbc09f330"
h7="271c335888bb0d5de6302beef87c8e567cfc7aab1d228f1fa3f34e38f0192420"
h8="384b947ae57980043f61fcccef4dfa5cdb2892fe5ba4ec12e01ba810e613eb12"
h9="6581ed6b53527f3d86857cf0446b3b57a0278a1479de8a2131e219606b213927"
h10="a14c13f1bba87855b9982b7a206f4f799859f1e488b7390da7a66dec4a03000e"
h11="bce45eb5800d6b7b7f8735375022117cd225230083ded85efa1cb12e664a5d41"
h12="b921b18a70a5926fac91d573d56a6b58cc3c1946f51356559de537e5287da67b"
h13="0a7a44ac3ada372d95ff098503bf2a184be4cf1f3fd67719a67d90b19df6c77b"
h14="195256ea0f60e5622875ed16cb57491c2beb36fe845ba819cfc99b4e128ba518"
h15="be30b0889b3019345a91d296eedda36673e757a7bac37fd6c9fb56d389bd3661"

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
	val16=`cat /sys/fs/cgroup/memory/docker/$s15/memory.usage_in_bytes`
	val17=`cat /sys/fs/cgroup/memory/docker/$s16/memory.usage_in_bytes`
	val18=`cat /sys/fs/cgroup/memory/docker/$s17/memory.usage_in_bytes`
	val19=`cat /sys/fs/cgroup/memory/docker/$s18/memory.usage_in_bytes`
	val20=`cat /sys/fs/cgroup/memory/docker/$s19/memory.usage_in_bytes`
	val21=`cat /sys/fs/cgroup/memory/docker/$s20/memory.usage_in_bytes`
	val22=`cat /sys/fs/cgroup/memory/docker/$s21/memory.usage_in_bytes`
	val23=`cat /sys/fs/cgroup/memory/docker/$s22/memory.usage_in_bytes`
	val24=`cat /sys/fs/cgroup/memory/docker/$s23/memory.usage_in_bytes`
	val25=`cat /sys/fs/cgroup/memory/docker/$s24/memory.usage_in_bytes`
	val26=`cat /sys/fs/cgroup/memory/docker/$s25/memory.usage_in_bytes`
	val27=`cat /sys/fs/cgroup/memory/docker/$s26/memory.usage_in_bytes`
	val28=`cat /sys/fs/cgroup/memory/docker/$s27/memory.usage_in_bytes`
	val29=`cat /sys/fs/cgroup/memory/docker/$s28/memory.usage_in_bytes`
	val30=`cat /sys/fs/cgroup/memory/docker/$s29/memory.usage_in_bytes`
	val31=`cat /sys/fs/cgroup/memory/docker/$s30/memory.usage_in_bytes`
	val32=`cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes`
	val33=`cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes`
	val34=`cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes`
	val35=`cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes`
	val36=`cat /sys/fs/cgroup/memory/docker/$h4/memory.usage_in_bytes`
	val37=`cat /sys/fs/cgroup/memory/docker/$h5/memory.usage_in_bytes`
	val38=`cat /sys/fs/cgroup/memory/docker/$h6/memory.usage_in_bytes`
	val39=`cat /sys/fs/cgroup/memory/docker/$h7/memory.usage_in_bytes`
	val40=`cat /sys/fs/cgroup/memory/docker/$h8/memory.usage_in_bytes`
	val41=`cat /sys/fs/cgroup/memory/docker/$h9/memory.usage_in_bytes`
	val42=`cat /sys/fs/cgroup/memory/docker/$h10/memory.usage_in_bytes`
	val43=`cat /sys/fs/cgroup/memory/docker/$h11/memory.usage_in_bytes`
	val44=`cat /sys/fs/cgroup/memory/docker/$h12/memory.usage_in_bytes`
	val45=`cat /sys/fs/cgroup/memory/docker/$h13/memory.usage_in_bytes`
	val46=`cat /sys/fs/cgroup/memory/docker/$h14/memory.usage_in_bytes`
	val47=`cat /sys/fs/cgroup/memory/docker/$h15/memory.usage_in_bytes`

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
	resul16=`echo "scale=4 ; (($val16)/$intervalo)" | bc`
	resul17=`echo "scale=4 ; (($val17)/$intervalo)" | bc`
	resul18=`echo "scale=4 ; (($val18)/$intervalo)" | bc`
	resul19=`echo "scale=4 ; (($val19)/$intervalo)" | bc`
	resul20=`echo "scale=4 ; (($val20)/$intervalo)" | bc`
	resul21=`echo "scale=4 ; (($val21)/$intervalo)" | bc`
	resul22=`echo "scale=4 ; (($val22)/$intervalo)" | bc`
	resul23=`echo "scale=4 ; (($val23)/$intervalo)" | bc`
	resul24=`echo "scale=4 ; (($val24)/$intervalo)" | bc`
	resul25=`echo "scale=4 ; (($val25)/$intervalo)" | bc`
	resul26=`echo "scale=4 ; (($val26)/$intervalo)" | bc`
	resul27=`echo "scale=4 ; (($val27)/$intervalo)" | bc`
	resul28=`echo "scale=4 ; (($val28)/$intervalo)" | bc`
	resul29=`echo "scale=4 ; (($val29)/$intervalo)" | bc`
	resul30=`echo "scale=4 ; (($val30)/$intervalo)" | bc`
	resul31=`echo "scale=4 ; (($val31)/$intervalo)" | bc`
	resul32=`echo "scale=4 ; (($val32)/$intervalo)" | bc`
	resul33=`echo "scale=4 ; (($val33)/$intervalo)" | bc`
	resul34=`echo "scale=4 ; (($val34)/$intervalo)" | bc`
	resul35=`echo "scale=4 ; (($val35)/$intervalo)" | bc`
	resul36=`echo "scale=4 ; (($val36)/$intervalo)" | bc`
	resul37=`echo "scale=4 ; (($val37)/$intervalo)" | bc`
	resul38=`echo "scale=4 ; (($val38)/$intervalo)" | bc`
	resul39=`echo "scale=4 ; (($val39)/$intervalo)" | bc`
	resul40=`echo "scale=4 ; (($val40)/$intervalo)" | bc`
	resul41=`echo "scale=4 ; (($val41)/$intervalo)" | bc`
	resul42=`echo "scale=4 ; (($val42)/$intervalo)" | bc`
	resul43=`echo "scale=4 ; (($val43)/$intervalo)" | bc`
	resul44=`echo "scale=4 ; (($val44)/$intervalo)" | bc`
	resul45=`echo "scale=4 ; (($val45)/$intervalo)" | bc`
	resul46=`echo "scale=4 ; (($val46)/$intervalo)" | bc`
	resul47=`echo "scale=4 ; (($val47)/$intervalo)" | bc`



	echo $i $resul0 $resul1 $resul2 $resul3 $resul4 $resul5 $resul6 $resul7 $resul8 $resul9 $resul10 $resul11 $resul12 $resul13 $resul14 $resul15 $resul16 $resul17 $resul18 $resul19 $resul20 $resul21 $resul22 $resul23 $resul24 $resul25 $resul26 $resul27 $resul28 $resul29 $resul30 $resul31 $resul32 $resul33 $resul34 $resul35 $resul36 $resul37 $resul38 $resul39 $resul40 $resul41 $resul42 $resul43 $resul44 $resul45 $resul46 $resul47 >>"topologia-tree-containers-memoria31".ods
	sleep 2
	i=`expr $i + 1`
done
