#!/bin/bash -e
cd md_en
filelist=$(ls *.md | rev | cut -c 4-| rev)
echo ${filelist}
cd ..

for name in ${filelist}
do
	sed -e s/'\\('/'$'/g   md_en/${name}.md >tmp.md
	sed -e s/'\\)'/'$'/g   tmp.md >tmp2.md
	pandoc tmp2.md -o tmp2.tex
  #sed -e s/'\\\['/''/g   tmp2.tex >tmp3.tex
	#sed -e s/'\\\]'/''/g   tmp3.tex >tmp4.tex
  #sed -e s/'aligned'/'eqnarray'/g   tmp4.tex >tex_en/${name}.tex
	sed -e s/'\\\['/'\\begin\{eqnarray\}'/g   tmp2.tex >tmp3.tex
	sed -e s/'\\\]'/'\\end\{eqnarray\}'/g    tmp3.tex>tex_en/${name}.tex
# なぜかうまくいかなかった(必須な変換ではないが、数式1行ずつに式番号をふりたいなら取り除くと良い)
#	sed -e s/''\\begin\{aligned\}'/''/g   tmp4.tex >tmp5.tex
#	sed -e s/''\\end\{aligned\}'/''/g   tmp4.tex >tex_en/${name}.tex
done

rm tmp*
