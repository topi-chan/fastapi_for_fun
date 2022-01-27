from fastapi import APIRouter

router = APIRouter(
    prefix="/bond_prices",
    tags=["bond_prices"],
    responses={404: {"description": "Page not found :("},
               200: {"description": "All right!"}},
)


@router.get("/")
def main_bond_price():
    return "test"
