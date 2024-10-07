from fastapi import FastAPI
from src.routers import words
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:3000", "http://localhost:8000", "http://172.20.0.3:3000/"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(words.router)
