% factorial(N, F)
factorial(0,1).
factorial(N,F) :-
    N>0,
    N1 is N-1,
    factorial(N1,F1),
    F is N * F1.

% length_list(List,Len)
length_list([],0).
length_list([_|T],N) :-
    length_list(T,N1),
    N is N1 + 1.

% sum_list(List,Sum)
sum_list([],0).
sum_list([H|T],S) :-
    sum_list(T,ST),
    S is H + ST.

% pow(Base,Exp,Result)
pow(_,0,1).
pow(B,E,R) :-
    E>0,
    E1 is E-1,
    pow(B,E1,R1),
    R is B * R1.

% pair_sum(List,Sum,A,B) devuelve pares A,B distintos con A+B=Sum
pair_sum(List,Sum,A,B) :-
    member(A,List),
    member(B,List),
    A < B,                 % evita duplicados (A,B) y (B,A)
    A + B =:= Sum.

% distinto_inequivalencia(X,Y) usa \=
distinto_inequivalencia(X,Y) :- X \= Y.

% distinto_dif(X,Y) usa dif/2 (mejor para variables)

distinto_dif(X,Y) :- dif(X,Y).

% buscar en BST: bst_search(Tree,Key)
bst_search(node(K,_,_),K).
bst_search(node(Root,L,_),K) :- K < Root, bst_search(L,K).
bst_search(node(Root,_,R),K) :- K > Root, bst_search(R,K).

% insertar en BST: bst_insert(Tree,Key,NewTree)
bst_insert(empty,K,node(K,empty,empty)).
bst_insert(node(Root,L,R),K,node(Root,NewL,R)) :-
    K < Root, bst_insert(L,K,NewL).
bst_insert(node(Root,L,R),K,node(Root,L,NewR)) :-
    K > Root, bst_insert(R,K,NewR).
bst_insert(node(Root,L,R),K,node(Root,L,R)) :- K =:= Root. % sin duplicados

% inorder traversal: bst_inorder(Tree, List)
bst_inorder(empty,[]).
bst_inorder(node(K,L,R),List) :-
    bst_inorder(L,LL),
    bst_inorder(R,RL),
    append(LL,[K|RL],List).

