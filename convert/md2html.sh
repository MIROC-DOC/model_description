#!/bin/bash -e

cd ./md_en
filelist=$(ls *.md | rev | cut -c 4-| rev)
echo ${filelist}
cd ..
for name in ${filelist}
do
#	sed -e s/'\\('/'$'/g   ../md_en/${name}.md >tmp.md
#	sed -e s/'\\)'/'$'/g   tmp.md >tmp2.md
pandoc -f markdown ./md_en/${name}.md  -t html --template=template.html -o html_en/${name}.html --metadata title="MIROC-DOC ${name}" -c github-markdown.css
done

rm tmp*
