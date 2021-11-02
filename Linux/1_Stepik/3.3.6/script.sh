#!`/bin/bash

x=$1

if [[ x -eq 0 ]]
then
  echo "No students"
elif [[ x -ge 5 ]]
then
  echo "A lot of students"
elif [[ x -eq 1 ]]
then
  echo "1 student"
else
  echo "$x students"
fi





