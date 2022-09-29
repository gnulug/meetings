#!/bin/bash
cd ~/Pictures/Screenshot
if [ ! -e "0000s.png" ] ; then
    touch "0000s.png"
fi
files=( *s.png )
largest=${files[${#files[@]} - 1]}
eog $largest
