# /bin/bash
echo "Contador Consumo" >>"topologia-tree-memoria".ods
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

h0="43e28a9bb302f35b0830b3535241f179ed1b27c6c836662df7c0b033edd7c130"
h1="fe54361aa53db138ae440bb37027e5212791cd84da947a19ac20b462c688cd41"
h2="8deaa76ec9eadd58edc1846967475e5ef4af946793b4a4771898f1ece2527f20"
h3="34d4cf6eecb4ea6027cd46e4f100cd21ece7ccab3ba8c011ce17d6bc2560f576"


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

	val32=`cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes`
	val33=`cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes`
	val34=`cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes`
	val35=`cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes`



	resul=`echo "scale=4 ; (($val0+$val1+$val2+$val3+$val4+$val5+$val6+$val7+$val32+$val33+$val34+$val35)/$intervalo)"  | bc`
	#echo $i $(cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s5/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s6/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s7/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s8/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s9/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s10/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s11/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s12/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s13/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s14/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s15/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s16/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s17/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s18/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s19/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s20/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s21/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s22/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s23/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s24/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h5/memory.usage_in_bytes | awk '{print $1/1048576}') >>"controlando".ods
	echo $resul >>"topologia-tree-memoria".ods

	sleep 2
	i=`expr $i + 1`
done
