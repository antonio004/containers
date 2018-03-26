#!/bin/bash

remove-switches(){
i=0 
s=16
while [ $i -lt $s ]
do
	docker exec sw$i ovs-vsctl del-br s$i
	docker stop sw$i
	#docker stop h$i
	docker rm sw$i
   i=`expr $i + 1`
done
}
remove-hosts(){
i=0 
h=2
while [ $i -lt $h ]
do
	docker exec h$i ovs-vsctl del-br h$i
	#docker stop sw$i h$i
	docker stop h$i
	docker rm h$i
   i=`expr $i + 1`
done
}
remove-switches
remove-hosts
clear
