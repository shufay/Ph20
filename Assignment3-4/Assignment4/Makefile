# Generate plots
# phase space

SRC = phase.py
TEX = main.tex

DO_SRC = python $(SRC)
COMPILE = pdflatex -shell-escape $(TEX)

TXT = $(wildcard *.txt)
ARGS = phase_space symplectic_spring energy error


.PHONY : all
all : $(SRC) $(TEX) $(TXT)
	git log > git.txt

	for arg in $(ARGS) ; do \
		$(DO_SRC) $$arg > $$arg.pdf ; \
	done

	$(COMPILE) 	

.PHONY : clean
clean :
	rm -rf *.pdf *.aux *.log git.txt _minted-main main.mintedcmd
