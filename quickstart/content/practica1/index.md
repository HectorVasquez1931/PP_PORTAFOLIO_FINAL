+++
date = '2025-11-20T23:38:00-08:00'
draft = true
title = 'Practica 1: Elementos basicos de los lenguajes de programacion'
+++


## Práctica 1: Elementos básicos de los lenguajes de programación

**Alumno:** Hector Alfredo Vasquez Carpio  
**Profesor:** Carlos Gallegos  
**Fecha:** 26/09/2025  
**Materia:** Paradigmas de la programación  

---

## Introducción  

La presente práctica tiene como propósito identificar y analizar los elementos fundamentales de los lenguajes de programación dentro de un programa en C. A partir del código proporcionado, se revisaron aspectos como nombres, marcos de activación, bloques de alcance, administración de memoria, expresiones, comandos, control de secuencia, subprogramas y tipos de datos. De esta manera, se logró relacionar la teoría con un ejemplo práctico de aplicación.  

---

## Desarrollo  

**Descripcion de elementos**  

***Nombres (identificadores)***  

```c
    displayBooksRecursive 
    addMember
    _book
    publication_year 
```

Todos los nombres de variables, funciones, structs y enum.

***Marcos de activación***

```c
    addBook(&library, &bookCount);
    displayBooks(library);
    addMember(&members, &memberCount);
```

Estructuras en el stack que se crean cuando se llama una función y se destruyen al terminar. En addBook se crea un marco con los parámetros library, bookCount y variables locales como new_book.

***Bloques de alcance***  
Bloques de función:  
Son los cuerpos de las funciones.  

Ejemplo:  

```c
void addBook(parametros) { 
    // Este es un bloque de función
    int genre;   // variable local a este bloque
}
```

Todo lo declarado aquí solo existe dentro de la función.  

Bloques en línea:
No son funciones, sino secciones internas.

Ejemplo:

```c
if (bookFound) {
    // Este es un bloque en línea
    printf("Libro encontrado\n");
}
```

Lo declarado aquí vive solo dentro de este if.

***Administración de memoria***

Automática: choice, bookCount dentro de main().

Estática: static int static_var = 0;  se reserva en compilación y dura toda la ejecución.

Dinamica: Es la que se maneja con malloc y free  
Ejemplo en addBook:

```c
    book_t *new_book = (book_t *)malloc(sizeof(book_t));
    // Reserva memoria en el heap para un nuevo libro
    //(estructura book_t) y devuelve un puntero a esa memoria
```

En las funciones "freeLibrary" y "freeMembers" se libera memoria del heap antes reservada.

***Expresiones***

Una expresión es un fragmento de código que produce un valor.  
Ejemplos:

```c
new_book->title[strcspn(new_book->title, "\n")] = '\0'; 
//devuelve un valor de posición y se asigna.

memberFound->issued_count++ //expresión aritmética que incrementa.
```

***Comandos***
Son instrucciones que ejecutan acciones, sin necesariamente devolver un valor.  

Ejemplos:

Asignaciones:  

```c
bookFound->quantity--;
```

Entrada/salida:  

```c
printf("Ingresa el ID del libro: ");
```

Control de flujo:

```c
if (bookFound && memberFound) { 
    instrucciones 
}

while (current) { 
    instrucciones 
}

switch (choice) {
    instrucciones
}

```

***Control de secuencia (selección)***

```c
if (bookFound && memberFound) 
{ 
    instrucciones
} 
switch (choice) 
{ 
    case 1: addBook(); 
    break;
}
```

Son de selección porque dependen de una condición booleana o de escoger un camino en base a un numero entero.

***Control de secuencia (iteracion)***

```c
for (int i = 0; i < memberFound->issued_count; i++) 
{ 
    instruncciones 
}
while(current_book) 
{
    instrucciones 
}
```

Son de iteración porque se repite varias veces hasta que la condición booleana deja de cumplirse.

***Control de secuencia (recursion)***

```c
    void displayBooksRecursive(book_t *library) {
    if (!library) {
        return;
    }
    printf("\nID libro: %d\nTitulo: %s\nAutor: %s\nAno de publicacion: %d\nGenero: %s\nCantidad: %d\n",
        library->id, library->title, library->author, library->publication_year, genreToString(library->genre), library->quantity);
    displayBooksRecursive(library->next);
}
```

Es recursión porque en lugar de usar un bucle, el problema se resuelve dividiéndolo en subproblemas más pequeños hasta llegar al caso base (!library).

***Subprogramas***

```c
    addBook 
    issueBook
    returnBook  
    saveLibraryToFile
    searchMember
```

Cada función (subprograma) encapsula instrucciones, recibe parámetros y puede devolver valores.

---

## Conclusiones

En esta práctica se logró identificar y analizar los elementos fundamentales de los lenguajes de programación mediante un programa en C que simula un sistema de biblioteca. Se comprendió la función de los nombres, marcos de activación y bloques de alcance para organizar el código y definir la visibilidad de las variables, así como la importancia de la administración de memoria automática, estática y dinámica, incluyendo la correcta liberación de memoria para evitar fugas. Además, se evidenció el uso de expresiones y comandos, el control de secuencia mediante selección, iteración y recursión, y la relevancia de los subprogramas para modularizar y estructurar la lógica del programa, integrando teoría y práctica de manera efectiva.

Link GitHub:  

[Link GitHub](https://github.com/HectorVasquez1931/Practica0/)
