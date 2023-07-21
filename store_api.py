import fastapi
import store_features.viewing as viewing
import store_features.checkout as checkout_basket
import store_features.database_add as database_add


store_api = fastapi.FastAPI()

def configure_routing():
    store_api.include_router(viewing.router)
    store_api.include_router(checkout_basket.router)
    store_api.include_router(database_add.router)
    

configure_routing()