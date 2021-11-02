#!/bin/bash

gcd ()
{
	if [[ $# -le 1 ]]
	then
		echo "bye"
		exit
	elif [[ $1 -eq $2 ]]
	then
		echo "res = $1"
		return
	elif [[ $1 -gt $2 ]]
	then
		let "A=$1-$2"
		gcd $A $2
	else
		let "B=$2-$1"
		gcd $1 $B
	fi
}

while true
do
	read a b
	gcd $a $b
done


