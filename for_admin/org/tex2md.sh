#!/bin/bash -e
cd tex_jpx
filelist=$(ls *.tex | rev | cut -c 5-| rev)
echo ${filelist}
cd ..

for name in ${filelist}
do
	pandoc -f latex -t markdown -t gfm --wrap=none -o md_jpx/${name}.md tex_jpx/${name}.tex
done
