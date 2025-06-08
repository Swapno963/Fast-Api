from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "hello this is swapno"}



@app.get("/about")
async def about() -> str:
    return "This is a simple FastAPI application."