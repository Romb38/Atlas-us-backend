from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login(username : str, password : str):
    pass

@router.post("/logout")
async def logout():
    pass