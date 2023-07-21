# import fastapi
from pydantic import BaseModel
from typing import Annotated
from store_features import database as db 
from store_features.authentication import auth_scheme 
from fastapi import Depends, APIRouter

router = APIRouter()

class Product(BaseModel):
    name: str
    category: str
    price: float

@router.post("/admin/add")
def add_products(token: Annotated[str, Depends(auth_scheme)], product: Product):
    product_details = {'name':product.name, 'price': product.price, 'category':product.category}
    generated_id = db.product_ids[-1] + 1
    db.product_ids.append(generated_id)
    db.products[generated_id] = product_details
    print(db.products)
    return (f"{product.name} has been added to the products database!")
    
    
