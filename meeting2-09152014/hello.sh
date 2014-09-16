#!/bin/bash

use quotes to preserve newlines. EX: 
    x=$(ifconfig)
    echo $x # no new lines
    echo "$x" # new lines 
# having new lines is useful for grep

# spaces matter in bash scripts b.c if bash sees x = 5 it will run the
# program x and pass in the arguments = and 5

x="hello"

if [ "$x" == "hello" ]; then # Note the 4 spaces between []
    echo "If statement pass!"
else
    echo "if statement fail."
fi
