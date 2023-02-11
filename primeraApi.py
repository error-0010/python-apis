from fastapi import FastAPI
app = FastAPI()

@app.get("/my-first-api")
def hola():
    return {"hola apis mundo!"}