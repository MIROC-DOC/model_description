#!/bin/bash -e
#
# Test environment
## pandoc
# pandoc 2.11.3.2
# Compiled with pandoc-types 1.22, texmath 0.12.1, skylighting 0.10.2,
# citeproc 0.3.0.3, ipynb 0.1.0.1
# Copyright (C) 2006-2020 John MacFarlane. Web:  https://pandoc.org

# Specify the directory markdown file existed
dir=../../descript_files

# Get markdown file names to be compiled
filelist=($(ls ${dir}/*.md | rev | cut -c 4-| rev))
# Conversion from markdown to LaTeX
for name in ${filelist[@]}
do
	echo ${name}
	sed -e s/'\\('/'$'/g ${name}.md | \
	sed -e s/'\\)'/'$'/g | \
	sed -e s/'<div style="text-align: right;"><!\\begin{flushright}>'/'\\begin{flushright}'/g | \
	sed -e s/'<\/div> <!\\end{flushright}>'/'\\end{flushright}'/g | \
	sed -e s/'<!--beginlandscape-->'/'\n beginlandscape \n'/g | \
	sed -e s/'<!--endlandscape-->'/'\n endlandscape \n'/g | \
	sed -e s/'ä'/'tmpaum'/g | \
	sed -e s/'\[\(.*\)\](\(#.*\))'/'\[\]\(\2\)'/g >tmp.md
	pandoc -t latex --columns=200 tmp.md| \
	sed -e s/'\\\['/'\\begin\{eqnarray\}'/g | \
	sed -e s/'\\\]'/'\\end\{eqnarray\}'/g | \
	sed -e s/'\\tag'/'\\label'/g | \
	sed -e s/'beginlandscape'/'\\begin{landscape}'/g | \
	sed -e s/'endlandscape'/'\\end{landscape}'/g | \
	sed -e s/'tmpaum'/'\\"{a}'/g | \
	sed -e s/'\\protect\\hyperlink'/'\\ref'/g | \
	sed -e 's/\(\\ref{.*}\)\({}\)/\1/g' \
	> ${name}.tex
	python tex2tex.py ${name}.tex
	mv ${name}.tex ../../descript_files/tex/
done

rm tmp.md
