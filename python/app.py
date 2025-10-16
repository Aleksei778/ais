import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

language = 'Python'

@app.get("/")
async def index():
    return HTMLResponse(content=f"<h1>Hello World from {language}</h1>")

@app.get("/language")
async def get_language():
    return JSONResponse({
        "language": language
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
