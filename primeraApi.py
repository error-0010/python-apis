from fastapi import FastAPI

app = FastAPI()

@app.get("/my-first-api")
def hola(name = None):

    if name is None:
        text = "Holaa!"

    else:
        text = "Holaa" + name + ""
    
    return text