# import fastapi
from pydantic import BaseModel
from typing import Annotated
import store_features.database as db #remember to remove this
# import authentication #remember to remove this also 
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
    



class Product(BaseModel):
    name: str
    category: str
    price: float

# router = fastapi.APIRouter() # Remember to change this to APIrouter later after testing

@router.post("/admin/add")
def add_products(token: Annotated[str, Depends(auth_scheme)], product: Product):
    product_details = {'name':product.name, 'price': product.price, 'category':product.category}
    generated_id = db.product_ids[-1] + 1
    db.product_ids.append(generated_id)
    db.products[generated_id] = product_details
    print(db.products)
    return (f"{product.name} has been added to the products database!")
    
    
