.PHONY: all clean

all: README.tex

clean:
	rm -f *.tex

%.tex: %.md
	pandoc -f markdown -t latex $^ -o $@