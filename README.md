## Proyecto de APIs y Machine Learning (ft. soyHenry)
Este es un proyecto basado en python que tiene como objetivo construir una API y un sistema de recomendación de películas para usuarios

link del vídeo DEMO: https://www.canva.com/design/DAFdw6m6T6s/YSCyXKs-_Jh-rgBO3aN5dA/edit?utm_content=DAFdw6m6T6s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Descripción
El proyecto utiliza datasets con información de calificaciones de películas de varios usuarios, y con información general de las peliculas existentes en las plataformas Amazon, Disney, Hulu, Netflix. 
A partir de estos datasets, se construyen cuatro funciones:

* Get_max_duration: Tiene como función retornar la pelicula con mayor duración tomando como argumentos el año de lanzamiento de la pelicula, la plataforma donde se lanzó y el tipo de duración (minutos o temporada/s).
* Get_score_count: Esta función devuelve la cantidad de peliculas que superan el puntaje otorgado según la plataforma escogida en un año determinado.
* Get_count_platform: Devuelve la cantidad de peliculas en una plataforma.
* Get_actor: Toma como argumentos una plataforma y un año determinado, y devuelve al actor de esa época con máyor apariciones cinematograficas.

Además de estas funciones, utilizando los datasets con las calificaciones de películas de los usuarios, se construye una matriz de usuarios y películas, donde cada fila representa a un usuario y cada columna representa una película.
El valor en cada celda de la matriz corresponde a la calificación que el usuario le dio a la película.

Esto es con la intención de crear un modelo de Machine Learning que prediga si a un usuario en concreto se le recomienda o no una pelicula en particular.
Para construir el modelo, se utiliza un algoritmo de KNN (K-Nearest Neighbors) o K-Vecinos más cercanos
El modelo KNN se basa en la premisa de que si a un usuario le gustaron ciertas películas en el pasado, es probable que le gusten películas similares en el futuro.  

En este enfoque, las similitudes entre los usuarios y las películas se calculan a partir de las interacciones pasadas entre ellos. Por ejemplo, si dos usuarios han visto y puntuado positivamente las mismas películas en el pasado, es probable que compartan gustos similares.

Finalmente, se utiliza Gradio para construir una interfaz web que permite al usuario ingresar su id de usuario y el id de la película que desea consultar, y el sistema devuelve si la película es recomendada o no para dicho usuario.


## Requerimientos
* Python 3.7 o superior
* Pandas
* Scikit-learn
* Gradio

## Uso
Para utilizar el sistema de recomendación o las funciones API, sigue los siguientes pasos:

1. Clona el repositorio desde GitHub: git clone https://github.com/MakingTheMOAO/proy.in.git
2. Instala los requerimientos: pip install -r requirements.txt
3. Ejecuta el archivo main.py: python main.py
4. Ingresa a la interfaz de gradio http://127.0.0.1:7860 (aparecerá en tu terminal una vez ejecutes main.py).
5. Elige entre las funciones de la API o el sistema de recomendación: Get_recommendation.
6. Ingresa tu id de usuario y el id de la película que deseas consultar.
7. El sistema te indicará si la película es recomendada o no para ti.
![image](https://user-images.githubusercontent.com/106265124/226214107-98f6a695-da4c-4a43-9f18-4c5cc14fafbd.png)


# Valores a ingresar:
- Al ingresar años, preferentemente usar valores mayores a 1950, a veces puede dar error a causa de la carencia de títulos en años anteriores.
- Al ingresar usuarios, usar números del 1 al 270896.
- Al ingresar plataformas, los únicos valores aceptados son: amazon, disney, hulu y netflix.
- Al ingresar puntajes, valores del 1 al 5.
- Al ingresar tipo de duracion, los únicos valores aceptados son: min, season, seasons.
- Al ingresar peliculas, as1234: amazon, ds1234: disney, hs1234: hulu, ns1234: netflix. 

# Autor
Emiliano David Tisera  
Correo: tisera.emilianodavid@gmail.com  
Linked In :https://www.linkedin.com/in/emiliano-tisera-aa8337224/
