from fastapi import FastAPI
from Etl_script import amazon, disney, hulu, netflix
app = FastAPI()


@app.get("/get_max_duration/{year}/{platform}/{duration_type}")
async def get_max_duration(year: int, platform: str, duration_type: int):
    if platform == "amazon":
        movie = amazon.query('release_year == @year and duration_type == @duration_type and duration_int == @amazon["duration_int"].max()')["title"].iloc[0]
        return movie