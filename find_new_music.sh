#!/bin/sh

cd new
find -iname "*.mp3" -exec sox -V3 {} {}.wav \;
../music/arss-script.sh *.wav
mogrify -format jpg *.bmp
rename 's/.mp3.wav.jpg$/.jpg/' *.mp3.wav.jpg
cd ..
mv new/* done/
