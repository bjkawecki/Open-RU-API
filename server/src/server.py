from fastapi import FastAPI
from src.routers import index_router, translations_router, words_router
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
app.include_router(words_router.router)
app.include_router(translations_router.router)
