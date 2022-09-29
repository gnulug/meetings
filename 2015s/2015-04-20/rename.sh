#!/bin/bash
for dir in *
do
  [[ -d $dir ]] || continue
  d=$(echo "$dir" | awk -F '-' '{ print $2 }')
  m=$(echo "$dir" | awk -F '-' '{ print $1 }')
  y=$(echo "$dir" | awk -F '-' '{ print $3 }')
  [[ ${#y} -eq 4 ]] || continue

  git mv $dir $y-$m-$d
done
