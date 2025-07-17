from fastapi import APIRouter, Depends, HTTPException,Form
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import status
from database import get_db
import models, schemas,utils
import utils.user


router = APIRouter(prefix="/post", tags=["post"])

@router.post("/create-post")
def create_user(
    username: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    user = schemas.UserCreate.model_validate({"username": username, "email": email})
    created_user = utils.user.create_user(db=db, user=user)
    return JSONResponse(
    content={
        "status_code": status.HTTP_201_CREATED,
        "message": "user created successfully",
        "data": schemas.User.model_validate(created_user).model_dump()
    },
    status_code=status.HTTP_201_CREATED
)

@router.get("/get-post") 
def read_users(db: Session = Depends(get_db)):
    users = utils.user.get_users(db)
    user_list = [schemas.User.from_orm(u).model_dump() for u in users]

    return JSONResponse(
        content={
            "status_code": status.HTTP_200_OK,
            "message": "user data fetched successfully",
            "data": user_list
        },
        status_code=status.HTTP_200_OK
    )
