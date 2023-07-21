import fastapi

products = {
    1: {    'name': 't-shirt',   'price': 19.99,    'category': 'clothes'},
    2: {    'name': 'stickers',  'price': 1.99,     'category': 'accessories'},
    3: {    'name': 'mug',       'price': 9.99,     'category': 'kitchenware'},
    4: {    'name': 'hoodie',    'price': 29.99,    'category': 'clothes'},
    5: {    'name': 'cap',       'price': 14.99,    'category': 'accessories'}
}
router = fastapi.APIRouter()
basket = []

@router.post("/products/add")
def add_to_basket(product_id:int):
    if product_id not in products.keys():
        return fastapi.Response("You have selected an item that we do not have!",404,media_type="application/json")
    else:
        basket.append(products[product_id])
        return "Item has been added to your checkout basket!"
    
@router.get("/checkout")
def get_basket():
    total_price = 0
    for item in basket:
        total_price += item['price']
    return basket, f"Total price: {total_price}"