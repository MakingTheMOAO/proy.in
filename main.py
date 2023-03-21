from fastapi import FastAPI
from Etl_script import amazon, disney, hulu, netflix, df_amazon, df_disney, df_hulu, df_netflix, df_ratings
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import gradio as gr
app = FastAPI()


@app.get('/get_max_duration/{year}/{platform}/{duration_type}')
async def get_max_duration(year: int, platform: str, duration_type: str):
    if platform == "amazon":
        movie = amazon.query('release_year == @year and duration_type == @duration_type')
        
        titulo = movie.sort_values('duration_int', ascending=False)['title'].iloc[0]
        
        return f'La pelicula de amazon del año {str(year)} con más duración en {duration_type} es: {titulo}'
    
    elif platform == "disney":
        
        movie = disney.query('release_year == @year and duration_type == @duration_type')
        
        titulo = movie.sort_values('duration_int', ascending=False)['title'].iloc[0]
        
        return f'La pelicula de disney del año {str(year)} con más duración en {duration_type} es: {titulo}'
    
    elif platform == "hulu":
        
        movie = hulu.query('release_year == @year and duration_type == @duration_type')
        
        titulo = movie.sort_values('duration_int', ascending=False)['title'].iloc[0]
       
        return f'La pelicula de hulu del año {str(year)} con más duración en {duration_type} es: {titulo}'
    
    elif platform == "netflix":
        
        movie = netflix.query('release_year == @year and duration_type == @duration_type')
       
        titulo = movie.sort_values('duration_int', ascending=False)['title'].iloc[0]
        
        return f'La pelicula de netflix del año {year} con más duración en {duration_type} es: {titulo}'
    
    else:
        return 'Plataformas disponibles: "amazon", "disney", "hulu" y "netflix"'

@app.get('/get_score_count/{platform}/{scored}/{year}')
async def get_score_count(platform: str, scored: float, year: int):
    if platform == "amazon":
       
        df_mean = df_amazon.groupby(['movieId'])['rating'].mean().reset_index()
        
        df_final = pd.merge(df_mean, df_amazon[['movieId', 'release_year']], on='movieId')
       
        cantidad = df_final.query('rating > @scored and release_year == @year')['movieId'].count()
       
        return f'La cantidad de peliculas arriba de {scored} puntos del año {year} son: {cantidad}'
    elif platform == "disney":
       
        df_mean = df_disney.groupby(['movieId'])['rating'].mean().reset_index()
       
        df_final = pd.merge(df_mean, df_disney[['movieId', 'release_year']], on='movieId')
       
        cantidad = df_final.query('rating > @scored and release_year == @year')['movieId'].count()
       
        return f'La cantidad de peliculas arriba de {scored} puntos del año {year} son: {cantidad}'
    elif platform == "hulu":
       
        df_mean = df_hulu.groupby(['movieId'])['rating'].mean().reset_index()
       
        df_final = pd.merge(df_mean, df_hulu[['movieId', 'release_year']], on='movieId')
       
        cantidad = df_final.query('rating > @scored and release_year == @year')['movieId'].count()
       
        return f'La cantidad de peliculas arriba de {scored} puntos del año {year} son: {cantidad}'
    elif platform == "netflix":
       
        df_mean = df_netflix.groupby(['movieId'])['rating'].mean().reset_index()
       
        df_final = pd.merge(df_mean, df_netflix[['movieId', 'release_year']], on='movieId')
       
        cantidad = df_final.query('rating > @scored and release_year == @year')['movieId'].count()
       
        return f'La cantidad de peliculas arriba de {scored} puntos del año {year} son: {cantidad}'
    else:
       
        return 'Plataformas disponibles: "amazon", "disney", "hulu" y "netflix"'

@app.get('/get_count_platform/{platform}')
async def get_count_platfrom(platform: str):
    if platform == 'amazon':
        
        Cant = amazon.movieId.count()
        
        return f'La cantidad de peliculas de {platform} es: {Cant}'
   
    elif platform == 'disney':
        
        Cant = disney.movieId.count()

        return f'La cantidad de peliculas de {platform} es: {Cant}'
   
    elif platform == 'hulu':
        
        Cant = hulu.movieId.count()

        return f'La cantidad de peliculas de {platform} es: {Cant}'
  
    elif platform == 'netflix':
        
        Cant = netflix.movieId.count()

        return f'La cantidad de peliculas de {platform} es: {Cant}'
    
    else:
        
        return 'Plataformas disponibles: "amazon", "disney", "hulu" y "netflix"'



@app.get('/get_actor/{platform}/{year}')
async def get_actor(platform: str, year: int):
    if platform == 'amazon':
        
        df_filtered = amazon[(amazon['release_year'] == year)]
        
        actor_list = [actor.strip() for cast in df_filtered['cast'] if not pd.isna(cast) for actor in cast.split(',')]
        
        actor_count = {}
        
        for actor in actor_list:
            actor_count[actor] = actor_count.get(actor, 0) + 1

        max_actor = max(actor_count, key=actor_count.get)
        
        return f'El actor con más apariciones de {platform} en el año {year} es {max_actor}'
   
    elif platform == 'disney':
        
        df_filtered = disney[(disney['release_year'] == year)]
        
        actor_list = [actor.strip() for cast in df_filtered['cast'] if not pd.isna(cast) for actor in cast.split(',')]
        
        actor_count = {}
        
        for actor in actor_list:
            actor_count[actor] = actor_count.get(actor, 0) + 1

        max_actor = max(actor_count, key=actor_count.get)
        
        return f'El actor con más apariciones de {platform} en el año {year} es {max_actor}'
   
    elif platform == 'hulu':
        
        return 'No hay registro de actores es la plataforma de hulu'
  
    elif platform == 'netflix':
        
        df_filtered = netflix[(netflix['release_year'] == year)]
        
        actor_list = [actor.strip() for cast in df_filtered['cast'] if not pd.isna(cast) for actor in cast.split(',')]
        
        actor_count = {}
        
        for actor in actor_list:
            actor_count[actor] = actor_count.get(actor, 0) + 1

        max_actor = max(actor_count, key=actor_count.get)
        
        return f'El actor con más apariciones de {platform} en el año {year} es {max_actor}'
    
    else:
        
        return 'Plataformas disponibles: "amazon", "disney", "hulu" y "netflix"'
@app.get('/get_recommendation/{user_id}/{movie_id}')
def get_recommendation(user_id, movie_id):
    # Obtener los datos de ratings de los usuarios
    user_ratings = df_ratings[df_ratings['userId'] == user_id]
    # Obtener los datos de ratings de otros usuarios para la misma película
    other_ratings = df_ratings[(df_ratings['userId'] != user_id) & (df_ratings['movieId'] == movie_id)]
    # Unir los datos
    combined_data = pd.concat([user_ratings, other_ratings], axis=0)
    # Pivotear los datos para que las filas representen usuarios y las columnas a las películas
    pivoted_data = combined_data.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    # Entrenar el modelo de K Vecinos más cercanos
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(pivoted_data.values, pivoted_data.index)
    # Predecir la recomendación para la película y usuario dados
    user_row = pivoted_data.loc[user_id].values.reshape(1, -1)
    predicted_rating = knn_model.predict(user_row)
    if predicted_rating > 3:
        return 'Recomendada'
    else:
        return 'No recomendada'

with gr.Blocks() as demo:
    gr.Markdown("""
    # Haga consultas acerca de peliculas con esta demo:
      Por favor coloque años superiores a 1950

                """)
    with gr.Tab("Get_max_count"):
        release_year = gr.Number(label= "Año")
        platform = gr.Textbox(label="Plataforma", placeholder= "amazon, disney, hulu o netflix...")
        duration_type = gr.Textbox(label="Tipo de duración", placeholder= "min, season o seasons...")
        output = gr.Textbox(label="Output")
        button = gr.Button("Consultar")
    with gr.Tab("Get_score_count"):
        platform2 = gr.Textbox(label= "Plataforma",placeholder= "amazon, disney, hulu o netflix...")
        score = gr.Number(label="Puntaje", placeholder="Puntaje...", float=True)
        year = gr.Number(label="Año",placeholder= "Desde 1920 en adelante...")
        output2= gr.Textbox(label="Output")
        button2 = gr.Button("Consultar")
    with gr.Tab("Get_count_platform"):
        platform3 = gr.Textbox(label="Plataforma",placeholder= "amazon, disney, hulu o netflix...")
        output3 = gr.Textbox(label="Output")
        button3 = gr.Button("Consultar")
    with gr.Tab("Get_actor"):
        platform4 = gr.Textbox(label="Plataforma",placeholder= "amazon, disney, hulu o netflix...")
        year4 = gr.Number(label="Año")
        output4 = gr.Textbox(label="Output")
        button4 = gr.Button("Consultar")
    with gr.Tab("Get_recommenation"):
        user_id = gr.Number(label="id de usuario...")
        movie_id = gr.Textbox(label="id de pelicula...")
        output5 = gr.Textbox(label="Output")
        button5 = gr.Button("Predecir")
    button.click(get_max_duration, inputs=[release_year,platform,duration_type], outputs=output)
    button2.click(get_score_count, inputs=[platform2,score,year], outputs=output2)
    button3.click(get_count_platfrom, inputs=platform3, outputs=output3)
    button4.click(get_actor, inputs=[platform4, year4], outputs=output4)
    button5.click(get_recommendation, inputs=[user_id,movie_id], outputs=output5)
    
demo.launch()

