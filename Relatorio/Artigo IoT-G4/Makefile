all: *.tex
	latexmk -pdf -bibtex-cond -quiet

clean:
	latexmk  -c
	rm  -rf *.out *.log *.fls *.aux *.fdb_latexmk *.bbl
