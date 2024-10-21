from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.index import router as index_router
from src.routers.translations import router as translations_router
from src.routers.words import router as words_router

origins = ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8000"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(index_router)
app.include_router(words_router)
app.include_router(translations_router)
