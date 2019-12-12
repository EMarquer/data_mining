#!/bin/sh

x=(40 50 60 70 80)

for i in  ${x[@]}
do
    j=$((i + 10))
    sort DecodedPatterns/FPG_$i.txt DecodedPatterns/FPG_$j.txt DecodedPatterns/FPG_$j.txt | uniq -u > DecodedPatterns/Diff/diff_"$i"_"$j".txt
done
