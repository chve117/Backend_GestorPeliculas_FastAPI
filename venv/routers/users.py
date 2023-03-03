from fastapi import APIRouter
from fastapi import Depends,Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movies import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middleware.jwt_bearer import JWTBearer
from jwt_manager import create_token

user_router = APIRouter()

class User(BaseModel):
     email: str
     password: str

@user_router.post('/login',tags=['auth'])
def login(user:User):
     if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
 