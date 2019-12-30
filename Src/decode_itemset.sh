#!/bin/sh

# use Src/spmf_encoding.py to encode all the pattern files in Patterns

mkdir -p DecodedPatterns

for filename in $(ls ./Patterns/)
do
   python3 Src/spmf_encoding.py decode Patterns/$filename le.pickle DecodedPatterns/$filename

done
