#!/bin/bash

name=f
age=1

while [[ -n $name && $age -ne 0 ]]
do
  echo "enter your name:"
  read name
  if [[ -z $name ]] 
  then
    echo "bye"
    exit
  fi


  echo "enter your age:"
  read age
  if [[ $age -eq 0 ]]
  then
    echo "bye"
    exit 
  fi


  if [[ $age -le 16 ]]
  then
    echo "$name, your group is child"
  elif [[ $age -gt 25 ]]
  then
    echo "$name, your group is adult"
  else
    echo "$name, your group is youth"
  fi
done



