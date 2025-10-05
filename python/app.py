import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse, HTMLResponse


router = APIRouter()
app = FastAPI()

app.include_router(router)

language = 'Python'

@router.get("/")
async def index():
    return HTMLResponse(content=f"<h1>Hello World from {language}</h1>")

@router.get("/language")
async def language():
    return JSONResponse({
        "language": language
    })

if name == "main":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    