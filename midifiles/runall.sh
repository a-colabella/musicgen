#!/bin/bash

for i in *.mid
do
    name=$(echo $i | cut -f 1 -d '.')
    midicsv $i $name.csv
done

for i in *.csv
do
    name=$(echo $i | cut -f 1 -d '.')
    python editCSV.py $i $name.txt
done

cat *.txt > masterFile.txt
