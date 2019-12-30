#!/bin/sh

mkdir -p FilteredRules

for filename in $(ls ./DecodedRules/)
do
  echo $filename

  python3 Src/filter_rules.py DecodedRules/$filename FilteredRules/$filename

done;
