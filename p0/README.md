
# Práctica 0: Uso de Repositorios  

**Alumno:** Hector Alfredo Vasquez Carpio  
**Profesor:** Carlos Gallegos  
**Fecha:** 10/09/2025  
**Materia:** Paradigmas de la programacion  

---

## Introducción  

El propósito de esta práctica es familiarizarnos con el uso de **Markdown**, **Git** y **GitHub**, así como con la creación de repositorios.  

Estas herramientas son fundamentales en el desarrollo profesional de software ya que permiten documentar, versionar y publicar proyectos de manera ordenada y colaborativa.  

---

## Desarrollo  

### 1. Markdown

**Markdown** es un lenguaje de marcado ligero que permite dar formato a texto de forma sencilla.  
Su sintaxis se basa en símbolos que representan títulos, listas, enlaces, imágenes y código.  

**Ejemplos de sintaxis en Markdown:**  

- `# Título` → Título grande
- `**negritas**` → **negritas**  
- `*cursiva*` → *cursiva*  
- `[enlace](https://github.com)` → [enlace](https://github.com)  

Markdown se utiliza principalmente en **documentación de proyectos** y archivos `README.md` en repositorios.  

#### Ejercicios en clase  

En clase practicamos con diferentes elementos de Markdown. A continuación el código que realizamos:  

```md
<!-- Comentario -->

# Encabezado 1

## Encabezado 2

### Encabezado 3

#### Encabezado 4

___

a __texto negrita__

a *italica 2010*

___

Imagen con tooltip y link
[![One piece](download.png)](https://www.google.com/search?q=siglas+html "One piece")

___

Tabla

| dias | meses | anios |
| - | - | - |
| Lunes| Enero | 10000000 |
| Miercoles | Febrero | 1990 |
| Viernes | Noviembre | 2004|

___

Lista

- [ ] tarea 1
- [x] tarea 3

___

Codigo en C

```c
#include <stdio.h>
int main()
{
    int x = 123;

    for(int i = 0; i<123)
}

---
```

### 2. Git y GitHub

**Git** es un sistema de control de versiones que permite llevar un historial de cambios en los proyectos.  
**GitHub** es una plataforma en la nube que almacena repositorios Git y facilita la colaboración entre desarrolladores.  

**Comandos esenciales de Git:**

```bash
git init                # Inicializar un repositorio
git status              # Ver el estado del repositorio
git add .               # Añadir archivos al área de preparación
git commit -m "mensaje" # Confirmar cambios
git remote add origin URL_REPO  # Enlazar con repositorio remoto
git push origin main    # Subir cambios a GitHub
git pull origin main    # Descargar cambios desde GitHub
```

### 3. Hugo y GitHub Actions

**Hugo** es un generador de sitios web estáticos. Esto significa que toma contenido escrito en archivos como Markdown y lo combina con plantillas o “themes” para generar páginas web completas en HTML, listas para publicarse en cualquier servidor. No necesita base de datos ni backend complejo, lo que lo hace muy rápido y eficiente. Es ideal para blogs, portafolios, documentación o cualquier sitio donde el contenido cambie con regularidad pero no requiera interacción dinámica del usuario.

Pagina estatica creada

![sitio](sitio_estatico.png)

**GitHub Actions** es la herramienta de automatización de GitHub. Permite definir flujos de trabajo, llamados workflows, que se ejecutan automáticamente cuando ocurre un evento en el repositorio, como un push de código. Con GitHub Actions se pueden automatizar tareas como compilar proyectos, ejecutar pruebas o desplegar sitios web, sin necesidad de intervención manual. Esto es especialmente útil para mantener actualizado un sitio web, ejecutar pruebas antes de publicar cambios o implementar procesos repetitivos de forma confiable y automática.

---

### Conclusiones

Aun no me acostumbro al uso de git, hago las cosas muy lento, pero solo es cosa de usarlo mas para tener mas confianza ejecutando los comandos. Batalle mucho con la parte de la pagina en GitPages, me fue bastante complicado hacerlo con la guia de la pagina de hugo, termine viendo un video que se me hizo mucho mas facil de entender.

[Link GitHub](https://github.com/HectorVasquez1931/Practica0/)

[Link pagina](https://hectorvasquez1931.github.io/Practica0/)
