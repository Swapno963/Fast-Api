from fastapi import FastAPI, HTTPException
from schemas import Band, GenreUrlChoices
app = FastAPI()

BAND = [
    {"id": 1, "name": "Band A", "genre": "Rock"},
    {"id": 6, "name": "Band B", "genre": "Pop"},
    {"id": 2, "name": "Band B", "genre": "Pop", "albutms": [
        {"title": "Album 1", "release_date": "2020-03-24"}
        ]
    },
    {"id": 3, "name": "Band C", "genre": "Jazz"},
    {"id": 4, "name": "Band D", "genre": "Classical"},
    {"id": 5, "name": "Band E", "genre": "Hip Hop"},
]

@app.get("/bands")
async def index(
    genre: GenreUrlChoices | None = None,
    has_albums: bool = False
    ) -> list[Band]:
    
    bands_list = [Band(**b) for b in BAND]
    if genre:
        filtered_bands = [b for b in bands_list if b.genre.value.lower() == genre.value.lower()]
        print(f"Genre: {genre}, Filtered bands: {filtered_bands}")  # Debugging line
        if not filtered_bands:
            raise HTTPException(status_code=404, detail="No bands found for this genre")
        bands_list = filtered_bands


    if has_albums:
        filtered_bands = [b for b in bands_list if len(b.albutms) > 0]
    else:
        filtered_bands = [b for b in bands_list if len(b.albutms) == 0]

        if not filtered_bands:
            raise HTTPException(status_code=404, detail="No bands with albums found")
        bands_list = filtered_bands
    return bands_list



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