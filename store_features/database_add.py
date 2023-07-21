import fastapi
from pydantic import BaseModel
import database as db


class Product(BaseModel):
    name: str
    category: str
    price: float

router = fastapi.APIRouter()

@router.post("/add")
def add_products(product: Product):
    product_details = {'name':product.name, 'price': product.price, 'category':product.category}
    generated_id = db.product_ids[-1] + 1
    db.product_ids.append(generated_id)
    db.products[generated_id] = product_details
    print(db.products)
    return (f"{product.name} has been added to the products database!")
    
    
