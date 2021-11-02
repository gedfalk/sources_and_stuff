#!/bin/bash

calc ()
{
	if  [[ "$1" == "exit" ]]
	then
		echo "bye"
		exit
	elif [[ $# -eq 1 ]]
	then
		echo "error"
		exit
	else
		case $2 in
			"+")
				let "result=$1+$3"
				echo "$result"
				;;
			"-")
				let "result=$1-$3"
				echo "$result"
				;;
			"*")
				let "result=$1*$3"
				echo "$result"
				;;
			"/")
				let "result=$1/$3"
				echo "$result"
				;;
			"%")
				let "result=$1%$3"
				echo "$result"
				;;
			"**")
				let "result=$1**$3"
				echo "$result"
				;;
			*)
				echo "error"
				exit
		esac
	fi
}

while true
do
	read x op y
	calc "${x}" "${op}" "${y}"
done
