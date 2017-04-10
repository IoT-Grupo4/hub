all: *.tex
	latexmk -pdf -bibtex-cond -quiet
	# remove -quiet for better verbose

clean:
	latexmk  -c
	rm  -rf *.out *.log *.fls *.aux *.fdb_latexmk *.bbl
