# /bin/bash
echo "Contador Consumo" >>"topologia-tree-memoria".ods
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
s30=`echo $sw30`
h0=`echo $ht0`
h1=`echo $ht1`
h2=`echo $ht2`
h3=`echo $ht3`
h4=`echo $ht4`
h5=`echo $ht5`
h6=`echo $ht6`
h7=`echo $ht7`
h8=`echo $ht8`
h9=`echo $ht9`
h10=`echo $ht10`
h11=`echo $ht11`
h12=`echo $ht12`
h13=`echo $ht13`
h14=`echo $ht14`
h15=`echo $ht15`

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


	resul=`echo "scale=4 ; (($val0+$val1+$val2+$val3+$val4+$val5+$val6+$val7+$val8+$val9+$val10+$val11+$val12+$val13+$val14+$val15+$val16+$val17+$val18+$val19+$val20+$val21+$val22+$val23+$val24+$val25+$val26+$val27+$val28+$val29+$val30+$val31+$val32+$val33+$val34+$val35+$val36+$val37+$val38+$val39+$val40+$val41+$val42+$val43+$val44+$val45+$val46+$val47)/$intervalo)"  | bc`
	#echo $i $(cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s5/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s6/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s7/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s8/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s9/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s10/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s11/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s12/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s13/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s14/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s15/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s16/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s17/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s18/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s19/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s20/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s21/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s22/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s23/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s24/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h5/memory.usage_in_bytes | awk '{print $1/1048576}') >>"controlando".ods
	echo $resul >>"topologia-tree-memoria".ods

	sleep 2
	i=`expr $i + 1`
done
