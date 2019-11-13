hombre(david).
hombre(juan).
hombre(andres).
hombre(alvaro).
hombre(emanuel).

mujer(paola).
mujer(daniela).
mujer(marlene).
mujer(angela).

% padres(X,P,M) => Los padres de X son P y M.
padres(david, alvaro, marlene).
padres(andres, alvaro, marlene).
padres(paola, alvaro, marlene).
padres(daniela, andres, angela).
padres(emanuel, juan, paola).

% P es padre de X
padre(P,X) :- padres(X,P,_).
% M es madre de X
madre(M,X) :- padres(X,_,M).

% El hermano de X es Y
hermano(X,Y) :- padres(X,P,M), padres(Y,P,M), X\==Y, hombre(Y).
% La hermana de X es Y
hermana(X,Y) :- padres(X,P,M), padres(Y,P,M), X\==Y, mujer(Y).
% Los hermanos de X son Y
hermanos(X,Y) :- hermano(X,Y);
		 hermana(X,Y).

% El hijo de X es Y
hijo(X,Y) :- padre(X,Y), hombre(Y);
             madre(X,Y), hombre(Y).
% La hija de X es Y
hija(X,Y) :- padre(X,Y), mujer(Y);
             madre(X,Y), mujer(Y).
% Los hijos de X son Y
hijos(X,Y) :- hijo(X,Y);
              hija(X,Y).

% El abuelo de X es Y
abuelo(X,Y) :- padre(A,X), padre(Y,A);
	       madre(A,X), padre(Y,A).
% La abuela de X es Y
abuela(X,Y) :- padre(A,X), madre(Y,A);
               madre(A,X), madre(Y,A).
% Los abuelos de X son Y
abuelos(X,Y) :- abuelo(X,Y);
		abuela(X,Y).

% El nieto de X es Y
nieto(X,Y) :- hijos(X,A), hijo(A,Y).
% La nieta de X es Y
nieta(X,Y) :- hijos(X,A), hija(A,Y).
% Los nietos de X son Y
nietos(X,Y) :- nieto(X,Y);
	       nieta(X,Y).

% El sobrino de X es Y
sobrino(X,Y) :- hermanos(X,A), hijo(A,Y).
% La sobrina de X es Y
sobrina(X,Y) :- hermanos(X,A), hija(A,Y).
% Los sobrinos de X son Y
sobrinos(X,Y) :- sobrino(X,Y);
		 sobrina(X,Y).

% El tio de X es Y
tio(X,Y) :- padres(X,P,_), hermano(P,Y);
	    padres(X,_,M), hermano(M,Y).
% La tia de X es Y
tia(X,Y) :- padres(X,P,_), hermana(P,Y);
	    padres(X,_,M), hermana(M,Y).
% Los tios de X son Y
tios(X,Y) :- tio(X,Y);
	     tia(X,Y).

% El primo de X es Y
primo(X,Y) :- tios(X,A), hijo(A,Y).
% La prima de X es Y
prima(X,Y) :- tios(X,A), hija(A,Y).
% Los primos de X son Y
primos(X,Y) :- primo(X,Y);
	       prima(X,Y).