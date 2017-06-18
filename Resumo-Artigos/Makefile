all: *.tex
	# latexmk -pdf -bibtex-cond IoT-G4.tex
	latexmk -pdf -bibtex-cond resumo_artigos.tex -quiet
	# remove -quiet for better verbose

clean:
	latexmk  -c
	rm  -rf *.out *.log *.fls *.aux *.fdb_latexmk *.bbl
