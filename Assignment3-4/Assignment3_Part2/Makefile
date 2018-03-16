# Generate plots
# phase space

SRC = phase.py
DO_SRC = python $(SRC)

ARGS = phase_space symplectic_spring energy error

.PHONY : all
all : $(SRC)  
	for arg in $(ARGS) ; do \
		$(DO_SRC) $$arg > $$arg.pdf ; \
	done 	

.PHONY : clean
clean :
	rm -rf *.pdf