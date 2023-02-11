from fastapi import FastAPI
app =from fastapi import FastAPI
app = FastAPI()

@app.get("/my-first-api")
def hola(name: str):
    return {"hola apis mundo!" + name + "!"}