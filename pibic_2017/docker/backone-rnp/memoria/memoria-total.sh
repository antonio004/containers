# /bin/bash
echo "Contador Consumo" >>"topologia-tree-memoria".ods
i=0
tempo=300
c="ff02d2f802a0c217bcc6dee525432754f8d6dc897867a7302d2afea288a2811c"
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


intervalo=1073741824


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



	resul=`echo "scale=4 ; (($val0+$val1+$val2+$val3+$val4+$val5+$val6+$val7+$val8+$val9+$val10+$val11+$val12+$val13+$val14+$val15+$val16+$val17+$val18+$val19+$val20+$val21+$val22+$val23+$val24+$val25+$val26+$val27+$val28+$val29+$val30+$val31+$val32+$val33+$val34+$val35+$val36)/$intervalo)"  | bc`
	#echo $i $(cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s5/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s6/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s7/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s8/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s9/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s10/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s11/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s12/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s13/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s14/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s15/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s16/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s17/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s18/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s19/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s20/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s21/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s22/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s23/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s24/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h5/memory.usage_in_bytes | awk '{print $1/1048576}') >>"controlando".ods
	echo $resul >>"topologia-tree-memoria".ods

	sleep 2
	i=`expr $i + 1`
done
