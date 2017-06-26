all: *.tex
	latexmk -pdf -bibtex-cond main.tex
	# latexmk -pdf -bibtex-cond main.tex -quiet
	# remove -quiet for better verbose

clean:
	latexmk  -c
	rm  -rf *.out *.log *.fls *.aux *.fdb_latexmk *.bbl *.vrb *.snm *.nav
