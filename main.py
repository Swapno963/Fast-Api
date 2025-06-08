from fastapi import FastAPI, HTTPException
from schemas import Band, GenreUrlChoices
app = FastAPI()

BAND = [
    {"id": 1, "name": "Band A", "genre": "Rock"},
    {"id": 2, "name": "Band B", "genre": "Pop", "albutms": [
        {"title": "Album 1", "release_date": "2020-03-24"}
        ]
    },
    {"id": 3, "name": "Band C", "genre": "Jazz"},
    {"id": 4, "name": "Band D", "genre": "Classical"},
    {"id": 5, "name": "Band E", "genre": "Hip Hop"},
]

@app.get("/bands")
async def index() -> list[Band]:
    return [Band(**b) for b in BAND]



@app.get("/bands/{band_id}")
async def band(band_id: int) -> Band:
    band = next((Band(**b) for b in BAND if b["id"] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band 





# Get all bands by genra
@app.get("/bands/genre/{genre}")
async def get_bands_by_genre(genre: GenreUrlChoices) -> list[dict]:
    filtered_bands = [b for b in BAND if b["genre"].lower() == genre.value.lower()]
    print(f"Genra : {genre}, Filtered bands: {filtered_bands}")  # Debugging line
    if not filtered_bands:
        raise HTTPException(status_code=404, detail="No bands found for this genre")
    return filtered_bands