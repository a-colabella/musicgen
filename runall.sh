#!/bin/bash

cd inputfiles/midis

for i in *.mid
do
    name=$(echo $i | cut -f 1 -d '.')
    midicsv $i ../csvs/$name.csv
done

cd ../csvs

for i in *.csv
do
    name=$(echo $i | cut -f 1 -d '.')
    python ../editCSV.py $i ../txts/$name.txt
done

cd ../txts

cat *.txt > ../../masterFile.txt
