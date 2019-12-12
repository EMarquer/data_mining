#!/bin/sh
#
#
#
#
#

mkdir -p DecodedPatterns

for filename in $(ls ./Patterns/)
do
   python Src/spmf_encoding.py decode Patterns/$filename le.pickle DecodedPatterns/$filename

done




