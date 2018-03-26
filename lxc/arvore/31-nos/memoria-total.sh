# /bin/bash
echo "Contador Consumo" #>>"topologia-rnp-memoria".ods
i=0
tempo=300
c="d8ab679bb88170486549a833e45b13501259173ff4355a7833c4957e2fe0e858"

intervalo=1073741824


while [ $i -lt $tempo ]
do
	val0=`cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes`
	val1=`cat /sys/fs/cgroup/memory/lxc/sw0/memory.usage_in_bytes`
	val2=`cat /sys/fs/cgroup/memory/lxc/sw1/memory.usage_in_bytes`
	val3=`cat /sys/fs/cgroup/memory/lxc/sw2/memory.usage_in_bytes`
	val4=`cat /sys/fs/cgroup/memory/lxc/sw3/memory.usage_in_bytes`
	val5=`cat /sys/fs/cgroup/memory/lxc/sw4/memory.usage_in_bytes`
	val6=`cat /sys/fs/cgroup/memory/lxc/sw5/memory.usage_in_bytes`
	val7=`cat /sys/fs/cgroup/memory/lxc/sw6/memory.usage_in_bytes`
	val8=`cat /sys/fs/cgroup/memory/lxc/sw7/memory.usage_in_bytes`
	val9=`cat /sys/fs/cgroup/memory/lxc/sw8/memory.usage_in_bytes`
	val10=`cat /sys/fs/cgroup/memory/lxc/sw9/memory.usage_in_bytes`
	val11=`cat /sys/fs/cgroup/memory/lxc/sw10/memory.usage_in_bytes`
	val12=`cat /sys/fs/cgroup/memory/lxc/sw11/memory.usage_in_bytes`
	val13=`cat /sys/fs/cgroup/memory/lxc/sw12/memory.usage_in_bytes`
	val14=`cat /sys/fs/cgroup/memory/lxc/sw13/memory.usage_in_bytes`
	val15=`cat /sys/fs/cgroup/memory/lxc/sw14/memory.usage_in_bytes`
	val16=`cat /sys/fs/cgroup/memory/lxc/sw15/memory.usage_in_bytes`
	val17=`cat /sys/fs/cgroup/memory/lxc/sw16/memory.usage_in_bytes`
	val18=`cat /sys/fs/cgroup/memory/lxc/sw17/memory.usage_in_bytes`
	val19=`cat /sys/fs/cgroup/memory/lxc/sw18/memory.usage_in_bytes`
	val20=`cat /sys/fs/cgroup/memory/lxc/sw19/memory.usage_in_bytes`
	val21=`cat /sys/fs/cgroup/memory/lxc/sw20/memory.usage_in_bytes`
	val22=`cat /sys/fs/cgroup/memory/lxc/sw21/memory.usage_in_bytes`
	val23=`cat /sys/fs/cgroup/memory/lxc/sw22/memory.usage_in_bytes`
	val24=`cat /sys/fs/cgroup/memory/lxc/sw23/memory.usage_in_bytes`
	val25=`cat /sys/fs/cgroup/memory/lxc/sw24/memory.usage_in_bytes`
	val26=`cat /sys/fs/cgroup/memory/lxc/sw25/memory.usage_in_bytes`
	val27=`cat /sys/fs/cgroup/memory/lxc/sw26/memory.usage_in_bytes`
	val28=`cat /sys/fs/cgroup/memory/lxc/sw27/memory.usage_in_bytes`
	val29=`cat /sys/fs/cgroup/memory/lxc/sw28/memory.usage_in_bytes`
	val30=`cat /sys/fs/cgroup/memory/lxc/sw29/memory.usage_in_bytes`
	val31=`cat /sys/fs/cgroup/memory/lxc/sw30/memory.usage_in_bytes`
	val32=`cat /sys/fs/cgroup/memory/lxc/h0/memory.usage_in_bytes`
	val33=`cat /sys/fs/cgroup/memory/lxc/h1/memory.usage_in_bytes`
	val34=`cat /sys/fs/cgroup/memory/lxc/h2/memory.usage_in_bytes`
	val35=`cat /sys/fs/cgroup/memory/lxc/h3/memory.usage_in_bytes`
	val36=`cat /sys/fs/cgroup/memory/lxc/h4/memory.usage_in_bytes`
	val37=`cat /sys/fs/cgroup/memory/lxc/h5/memory.usage_in_bytes`
	val38=`cat /sys/fs/cgroup/memory/lxc/h6/memory.usage_in_bytes`
	val39=`cat /sys/fs/cgroup/memory/lxc/h7/memory.usage_in_bytes`
	val40=`cat /sys/fs/cgroup/memory/lxc/h8/memory.usage_in_bytes`
	val41=`cat /sys/fs/cgroup/memory/lxc/h9/memory.usage_in_bytes`
	val42=`cat /sys/fs/cgroup/memory/lxc/h10/memory.usage_in_bytes`
	val43=`cat /sys/fs/cgroup/memory/lxc/h11/memory.usage_in_bytes`
	val44=`cat /sys/fs/cgroup/memory/lxc/h12/memory.usage_in_bytes`
	val45=`cat /sys/fs/cgroup/memory/lxc/h13/memory.usage_in_bytes`
	val46=`cat /sys/fs/cgroup/memory/lxc/h14/memory.usage_in_bytes`
	val47=`cat /sys/fs/cgroup/memory/lxc/h15/memory.usage_in_bytes`

	resul=`echo "scale=4 ; (($val0+$val1+$val2+$val3+$val4+$val5+$val6+$val7+$val8+$val9+$val10+$val11+$val12+$val13+$val14+$val15+$val16+$val17+$val18+$val19+$val20+$val21+$val22+$val23+$val24+$val25+$val26+$val27+$val28+$val29+$val30+$val31+$val32+$val33+$val34+$val35+$val36+$val37+$val38+$val39+$val40+$val41+$val42+$val43+$val44+$val45+$val46+$val47)/$intervalo)"  | bc`
	#echo $i $(cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s5/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s6/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s7/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s8/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s9/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s10/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s11/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s12/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s13/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s14/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s15/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s16/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s17/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s18/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s19/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s20/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s21/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s22/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s23/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s24/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h5/memory.usage_in_bytes | awk '{print $1/1048576}') >>"controlando".ods
	echo $resul >>"memoria-arvore-31".ods

	sleep 2
	i=`expr $i + 1`
done
