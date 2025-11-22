
    A \= B.

positivo(N) :-
    N > 0,
    N \= 0.

impar(N) :-
    \+ par(N).

par(N) :-
    0 is N mod 2.
permitido(X) :-
    \+ prohibido(X).

prohibido(arma).
prohibido(fuego).