from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("570748db-664d-43fc-af12-f04f3b255171"),
        first_name="Win",
        middle_name=None,
        last_name="Ngo",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("25f08e37-dd40-4a48-9cc7-6e82f9fd1b22"),
        first_name="Sol",
        middle_name=None,
        last_name="Ngo",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]

# Get: retrieve common info
@app.get("/")
def root():
    return {"Hello" : "WN"}

# Get: retrive objects
@app.get("/api/v1/users")
async def fetch_users():
    return db

# Post: create an object
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

# Delete: delete an object by id
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists."
    )

# Put: update an object 