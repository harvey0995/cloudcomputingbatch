    from fastapi import fastAPI

    app = FastAPI()

@app.get("/helloworld")
async def read_root():
    return{"Message":"Hello world
    Congrats"}

    