from fastapi import APIRouter


router = APIRouter(tags=["Index"])


@router.get("/")
async def get_index() -> str:
    return "Welcome to Open Ru API"
