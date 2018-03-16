# /bin/bash
echo "Contador Consumo" >>"topologia-grade9-memoria".ods
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

h0=`echo $ht0`
h1=`echo $ht1`



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

	val32=`cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes`
	val33=`cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes`



	resul=`echo "scale=4 ; (($val0+$val1+$val2+$val3+$val4+$val5+$val6+$val7+$val8+$val9+$val32+$val33)/$intervalo)"  | bc`
	#echo $i $(cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s5/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s6/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s7/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s8/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s9/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s10/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s11/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s12/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s13/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s14/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s15/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s16/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s17/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s18/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s19/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s20/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s21/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s22/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s23/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s24/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h5/memory.usage_in_bytes | awk '{print $1/1048576}') >>"controlando".ods
	echo $resul >>"topologia-grade9-memoria".ods

	sleep 2
	i=`expr $i + 1`
done
