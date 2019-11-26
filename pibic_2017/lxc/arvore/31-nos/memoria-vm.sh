# /bin/bash
i=0
tempo=300

intervalo=1073741824


while [ $i -lt $tempo ]
do
	val=`free -hm`	
	echo $val  >>"memoria-VM".ods

	sleep 2
	i=`expr $i + 1`
done
