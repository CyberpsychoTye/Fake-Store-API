from typing import Annotated
from fastapi import Depends, APIRouter, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

auth_scheme = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()

@router.post("/login")
def login (form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    valid_user = db.users.get(form_data.username)
    if not valid_user:
        return Response("Incorrect username or password",404,media_type="application/json")
    supplied_password = form_data.password
    if valid_user["password"] != supplied_password:
        return Response("Incorrect username or password",400,media_type="application/json")
    
    return {"access_token":form_data.username, "token_type":"bearer"}
    
