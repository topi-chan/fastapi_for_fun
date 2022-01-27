from typing import List
from uuid import UUID

from fastapi import FastAPI

import bond_prices
from models import User, Gender, Role

app = FastAPI()

app.include_router(bond_prices.router)

db: List[User] = [
    User(
        id=UUID("51788b65-6751-45ef-84ba-948142849ade"),
        first_name="Tom",
        last_name="Jerry",
        gender=Gender.male,
        roles=Role.user
    ),
    User(
        id=UUID("f0dab894-bf31-4610-9457-055d2ce63079"),
        first_name="James",
        last_name="Mark",
        gender=Gender.male,
        roles=Role.admin
    ),
]


@app.get("/")
def root():
    return {"Hello": "Hi!"}


@app.get("/users")
async def get_db():
    return db


@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return {id: user.id}
