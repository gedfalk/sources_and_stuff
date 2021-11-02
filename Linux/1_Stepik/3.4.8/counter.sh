#!/bin/bash

counter ()
{
	local let "c1+=$1"
	let "c2+=${1}*2"
}

i=1
while [[ i -le 10 ]]
do
	counter i
	let "i+=1"
done 

echo "counter are $c1 and $c2"

