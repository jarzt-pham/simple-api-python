from fastapi import FastAPI
from endpoints import item

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(item.router)