#!/bin/bash
mkdir -p $HOME/Pictures/Screenshot
cd $HOME/Pictures/Screenshot
if [ ! -e "0000s.png" ] ; then
    touch "0000s.png"
fi
files=( *s.png )
largest=${files[${#files[@]} - 1]}
largest=${largest%%[^[:digit:]]*}
largest=$((10#$largest))
now=$(date +"%m-%d-%Y")
printf -v filename '%04ds.%ss.png' "$((largest + 1))" "$now"
/usr/bin/scrot -q 80 -d .2 -s $filename
python $HOME/dotfiles/bin/imgclip2.py $HOME/Pictures/Screenshot/$filename
