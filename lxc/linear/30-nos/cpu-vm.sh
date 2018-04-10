# /bin/bash
i=0
tempo=600

intervalo=1073741824


while [ $i -lt $tempo ]
do
	val=`mpstat`	
	echo $val  #>>"cpu-VM".ods

	sleep 2
	i=`expr $i + 1`
done
