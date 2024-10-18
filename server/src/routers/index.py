from src.routers import index_router as router


@router.get("/")
async def get_index() -> str:
    return "Welcome to Open Ru API"
