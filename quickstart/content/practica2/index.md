+++
date = '2025-11-20T23:41:22-08:00'
draft = false
title = 'Practica 2: Programacion Orientada a Objetos'
+++

**Nombre:** Hector Vasquez  
**Matricula:** 378827  
**Materia:** Paradigmas de la programacion  
**Profesor:** Carlos Gallegos  

---

## **Introducción**  

En esta práctica se realizó la migración del programa de biblioteca desarrollado originalmente en lenguaje C hacia Python, aplicando los principios de la Programación Orientada a Objetos (POO).
En el presente reporte se da una explicación sobre los conceptos fundamentales de la programación orientada a objetos y se compara el programa nativo en C con el nuevo en python usando el paradigma POO.

---

### **Conceptos de POO**  

***Clase***  
Las clases son modelos o abstracciones de la realidad que representan un elemento de un conjunto de objetos como aviones, animales, personas, autos, computadoras, ecuaciones, figuras geométricas, elementos de una interfaz gráfica, archivos, etc. El modelado que se hace de la información y del comportamiento de los miembros de la clase se hace dentro del dominio del problema, es decir, sólo se incluyen las partes de son relevantes para poder resolver el problema planteado. Esto se conoce como principio de abstracción. Define las características (atributos) y comportamientos (métodos) de un tipo de objeto.  

```py
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
#Aquí, Usuario es una clase que define cómo son los usuarios de la biblioteca.
```

***Objeto***  
Un objeto es una instancia concreta de una clase, es decir, algo real que existe en memoria.  

```py
usuario1 = Usuario("María", 101)
#usuario1 es un objeto de la clase Usuario. Tiene su propio nombre e ID, independientes de otros usuarios.
```

***Encapsulación***

La encapsulación se refiere a la capacidad de ocultar los detalles de implementación de un objeto. Los objetos tienen datos y comportamientos, pero solo los comportamientos están disponibles para otros objetos. Los datos se mantienen privados y solo se pueden acceder a través de los métodos públicos de un objeto.  

```py
class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre  # atributo privado

    def get_nombre(self):
        return self.__nombre
#Así, el nombre no puede modificarse directamente desde fuera de la clase.
```

***Abstracción***  

La abstracción se refiere a la capacidad de un objeto para presentar solo los detalles relevantes a otros objetos. Un objeto solo muestra lo que es importante para otros objetos y oculta la complejidad interna.  

```py
from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass
```

***Herencia***

La herencia permite que un objeto adquiera propiedades de otro objeto. Una clase puede heredar propiedades y comportamientos de otra clase. Esto permite la reutilización del código y la creación de jerarquías de clases.  

```py
class Item:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Libro(Item):
    def __init__(self, titulo, autor, genero):
        super().__init__(titulo, autor)
        self.genero = genero
#Libro hereda los atributos titulo y autor de Item, y además agrega su propio atributo genero.
```

***Polimorfismo***

El polimorfismo se refiere a la capacidad de un objeto para tener más de una forma. Un objeto puede tener varias formas dependiendo del contexto en el que se utilice.

```py
class Libro(Item):
    def mostrar_info(self):
        print(f"Libro: {self.titulo} - Autor: {self.autor}")

class Revista(Item):
    def mostrar_info(self):
        print(f"Revista: {self.titulo} - Editor: {self.autor}")

# Ejemplo de polimorfismo
for item in [Libro("1984", "Orwell", "Ficción"), Revista("National Geographic", "NatGeo")]:
    item.mostrar_info()
#El método mostrar_info() se comporta distinto dependiendo del tipo de ítem, aunque se llame igual.
```

---

### **Comparación entre la versión en C y la versión en Python**  

| Aspecto  |  Versión en C | Versión en Python |
|-------------|----------|----------|
| Paradigma    | Programación estructurada | Programación orientada a objetos   |
| Extensibilidad | Agregar un nuevo tipo de ítem requiere modificar varias funciones.  | Basta con crear una nueva subclase que herede de Item.  |
| Manejo de datos   | Usa struct para representar datos y funciones separadas para operar sobre ellos.   | Cada clase combina datos y métodos, lo que mejora la organización.   |
|Gestión de memoria|Manual (malloc, free).|Automática (recolección de basura).|

---

### **Ventajas de la Programación Orientada a Objetos**

**Modularidad:**  
El código se organiza en clases, lo que facilita su mantenimiento y reutilización.

**Reutilización:**  
La herencia permite crear nuevas clases sin volver a escribir código repetido.

**Escalabilidad:**  
Es fácil agregar nuevas funcionalidades (por ejemplo, agregar una clase Pelicula que herede de Item).

**Abstracción y claridad:**  
El código se asemeja más al mundo real (Usuario, Biblioteca, Libro), por lo que es más intuitivo.

**Menor riesgo de errores:**  
El encapsulamiento protege los datos y mantiene un mejor control sobre su acceso.

### **Conclusiones**

En lo personal, considero que la Programación Orientada a Objetos facilita mucho la organización y el entendimiento del código. Siento que hace ver a la programacion como algo mas tangible por como se relacionan los objetos entre sí, lo que hace más intuitivo el proceso de diseñar soluciones. Ademas el codigo es mas reutilizable y fácil de mantener. Aunque hay conceptos que no tengo totalmente claros todavia, como los *subtipos*.

### **Referencias**

[A_Certitec. (2023, abril 26). Programación Orientada a Objetos (POO): Todo lo que necesitas saber. Certitec.](https://certitec.eu/programacion-orientada-a-objetos/)

[Ramos, J. A., & Segura, J. B. (2022, enero 11). Clases y objetos. Portal Académico del CCH.]( https://portalacademico.cch.unam.mx/cibernetica1/analisis-y-diseno-en-poo/clases-y-objetos)

[Sandoval, E. (2023, septiembre 21). ¿Qué es un objeto en programación? Ebac.](https://ebac.mx/blog/objeto-en-programacion)

GitHub:
[https://github.com/HectorVasquez1931/PORTAFOLIO_PP](https://github.com/HectorVasquez1931/PORTAFOLIO_PP/tree/main/content/docs)
