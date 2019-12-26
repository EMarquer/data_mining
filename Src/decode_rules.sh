#!/bin/bash

# use Src/spmf_encoding.py to encode all the pattern files in Patterns

mkdir -p DecodedRules


for filename in $(ls ./Rules/)
do
  python Src/spmf_encoding.py decode Rules/$filename le.pickle DecodedRules/$filename
done;





