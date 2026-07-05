from fastapi import APIRouter

router = APIRouter(
    prefix="/facturas",
    tags=["Facturas"]
)

@router.get("/")
def obtener_facturas():
    return []