
all: a-setup.pdf d-basic.pdf d-time.pdf d-vert.pdf d-ref.pdf

.SUFFIXES: .tex .pdf

.tex.pdf:
	sed -e "s/__file__/$*/g" template.tex >$*_tmp.tex
	platex $*_tmp.tex
	dvipdfmx $*_tmp.dvi
	mv $*_tmp.pdf $@
