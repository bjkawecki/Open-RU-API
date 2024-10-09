from fastapi import FastAPI
from src.routers import index_router, translations_router

from src.routers.words_router import words_create
from src.routers.words_router import words_delete
from src.routers.words_router import words_read

from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:3000", "http://localhost:8000"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(index_router.router)

app.include_router(words_create.router)
app.include_router(words_delete.router)
app.include_router(words_read.router)

app.include_router(translations_router.router)
