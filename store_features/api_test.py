import requests
import json
data = {'product_id':6, 'category':'clothes', 'price':500.00, 'name':'gucci_tee'}


# response = requests.get("http://127.0.0.1:8000/products/all/")
# response_2 = requests.get("http://127.0.0.1:8000/products/5")
# response_3 = requests.get("http://127.0.0.1:8000/products/by_category/clothes")
# response_4 = requests.post("http://127.0.0.1:8000/products/add?product_id=1")
# response_5 = requests.post("http://127.0.0.1:8000/products/add?product_id=3")
# response_5 = requests.post("http://127.0.0.1:8000/products/add?product_id=4")
# response_5 = requests.post("http://127.0.0.1:8000/products/add?product_id=3")
# response_6 = requests.get("http://127.0.0.1:8000/checkout")
response_7 = requests.post("http://127.0.0.1:8000/add", data=json.dumps(data))
print(response_7.json())