#!/bin/bash

echo '"C-style" FOR loop'
for ((n=1; n <= 10; n++)); do
	echo "n = $n"
done

echo 'Traditional Bash FOR loop'
for n in {1..10}; do
	echo "n = $n"
done
