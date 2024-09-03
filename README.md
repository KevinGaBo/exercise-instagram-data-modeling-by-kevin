<!--hide-->
# Create the database model for Instagram
<!--endhide-->

**Important**: To do this activity you need to `fork` [this repo](https://github.com/breatheco-de/exercise-instagram-data-modeling) into your **Github** account and then open the forked repo on Codespaces (recommended) or Gitpod.

### Project Description / Descripción del Proyecto

**English:**

This project aims to create a database model for Instagram using the SQLAlchemy library in Python. Through this exercise, developers will learn to design and structure a relational database that represents the main components of the Instagram application, such as users, posts, comments, and more.

The project includes creating an Entity Relationship Diagram (ERD) that visualizes the tables and their relationships. This diagram is essential for understanding how data is organized and connected in a complex application like Instagram.

Additionally, it provides the opportunity to use cloud development tools such as Codespaces or Gitpod, making coding and collaboration easier. It is ideal for those looking to learn about database modeling, using ORM with SQLAlchemy, and creating ERD and UML diagrams.

This exercise is part of the 4Geeks Academy curriculum, designed to prepare students for professional software development with a focus on practical application and real-world projects.

**Español:**

Este proyecto tiene como objetivo crear un modelo de base de datos para Instagram utilizando la biblioteca SQLAlchemy en Python. A través de este ejercicio, los desarrolladores aprenderán a diseñar y estructurar una base de datos relacional que represente los principales componentes de la aplicación Instagram, como usuarios, publicaciones y comentarios.

El proyecto incluye la creación de un Diagrama de Relaciones de Entidad (ERD) que visualiza las tablas y sus relaciones. Este diagrama es esencial para entender cómo se organizan y conectan los datos en una aplicación compleja como Instagram.

Además, permite usar herramientas en la nube como Codespaces o Gitpod, facilitando la codificación y la colaboración. Es ideal para quienes desean aprender sobre modelado de bases de datos, uso de ORM con SQLAlchemy, y creación de diagramas ERD y UML.

Este ejercicio forma parte del plan de estudios de 4Geeks Academy, diseñado para preparar a los estudiantes en el desarrollo de software profesional, con un enfoque en la práctica y la aplicación del conocimiento en proyectos reales.

Inside the `src/models.py` file, you will find a couple of classes describing an example database.

Here is a 10 min video explaining what UML is: [https://www.youtube.com/watch?v=UI6lqHOVHic](https://www.youtube.com/watch?v=UI6lqHOVHic)

The `diagram.png` file generates a database chart based on the classes that you will be creating. Such charts in Database Management are referred to as ERDs (Entity Relatonship Diagrams). 

Please watch these two short videos explaining ERDs: 
+ [https://www.youtube.com/watch?v=QpdhBUYk7Kk](https://www.youtube.com/watch?v=QpdhBUYk7Kk)
+ [https://www.youtube.com/watch?v=-CuY5ADwn24](https://www.youtube.com/watch?v=-CuY5ADwn24)

You will have to create the Entity Relationship Diagram for Instagram's Database - a very similar diagram to this one:

![Instagram Diagram](https://github.com/breatheco-de/exercise-instagram-data-modeling/blob/master/assets/example.png?raw=true)
[Click to open diagram](https://app.quickdatabasediagrams.com/#/d/LxNXQZ)

> 🔥 You can use this FREE tool to practice your diagram for the first time: https://app.quickdatabasediagrams.com/#/d/


## 💻 Installation / Instalación

1. Get inside the environment `$ pipenv shell` / Entra en el entorno virtual `$ pipenv shell`

2. Install all dependencies `$ pipenv install` / Instala todas las dependencias `$ pipenv install`

3. Generate the diagram as many times as you need `$ python src/models.py` / Genera el diagrama tantas veces como necesites `$ python src/models.py`

4. Open the file `diagram.png` to check out your ERD diagram! / Abre el archivo `diagram.png` para ver tu diagrama ERD!


## 📝 Instructions / Instrucciones

Your job is to update the `src/models.py` file with the code needed to replicate Instagram's data model. / Tu tarea es actualizar el archivo `src/models.py` con el código necesario para replicar el modelo de datos de Instagram.

The project is using the SQLAlchemy Python library to generate the database. / El proyecto utiliza la biblioteca Python SQLAlchemy para generar la base de datos.

- What tables do you think Instagram might have on its database: E.g: Post, User, etc.? / ¿Qué tablas crees que podría tener Instagram en su base de datos? Por ejemplo: Post, Usuario, etc.
- What properties should go inside the User? or inside the Post table? / ¿Qué propiedades deberían ir dentro de la tabla Usuario? ¿O dentro de la tabla Post?
- Please add at least 4 models with all of their properties. / Por favor, añade al menos 4 modelos con todas sus propiedades.
- Refresh the `diagram.png` file at the end by running `$ python src/models.py` on the console. / Actualiza el archivo `diagram.png` al final ejecutando `$ python src/models.py` en la consola.

This and many other projects are built by students as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning). / Este y muchos otros proyectos son desarrollados por estudiantes como parte del [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) de 4Geeks Academy, dirigido por [Alejandro Sánchez](https://twitter.com/alesanchezr) y muchos otros colaboradores. Descubre más sobre nuestro [Curso de Desarrollador Full Stack](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer) y el [Bootcamp de Ciencia de Datos](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).
