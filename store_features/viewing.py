import fastapi 

products = {
    1: {    'name': 't-shirt',   'price': 19.99,    'category': 'clothes'},
    2: {    'name': 'stickers',  'price': 1.99,     'category': 'accessories'},
    3: {    'name': 'mug',       'price': 9.99,     'category': 'kitchenware'},
    4: {    'name': 'hoodie',    'price': 29.99,    'category': 'clothes'},
    5: {    'name': 'cap',       'price': 14.99,    'category': 'accessories'}
}
router = fastapi.APIRouter()

@router.get("/products")
def get_all_products():
    return products

@router.get("/products/{product_id}")
def get_product(product_id:int):
    return products[product_id]

@router.get("/products/by_category/{category}")
def get_products_by_category(category:str):
    result = {}
    for key,value in products.items():
        if category in value.values():
          result [key] = value
        else:
          continue
    return result

@router.get("/products/filter_by_price/{price}")
def filter_products_by_price(price:float):
    result = {}
    for key,value in products.items():
        if price >= value['price']:
          result [key] = value
        else:
          continue
    return result

