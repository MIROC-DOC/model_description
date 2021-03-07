
all: a-setup.pdf d-basic.pdf d-time.pdf d-vert.pdf

.SUFFIXES: .md .pdf

.md.pdf:
	pandoc $< -o $@ --pdf-engine=lualatex -V documentclass=ltjsarticle -V luatexjapresetoptions=noembed
