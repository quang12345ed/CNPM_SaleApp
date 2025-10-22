import json


def load_categories():
    with open("data/category.json",encoding="utf-8") as f:
        return json.load(f)
def load_products(keyword = None,category_id = None):
    with open("data/product.json", encoding="utf-8") as f:
        products =  json.load(f)
        if keyword:
            keyword = keyword.lower()
            products = [p for p in products if keyword in p['name'].lower() or keyword in p['description'].lower()]
        if category_id is not None:
            try:
                cid = int(category_id)
                products = [p for p in products if p['category_id'] == cid]
            except ValueError:
                pass
    return products

def get_product_by_id(product_id):
    with open("data/product.json", encoding="utf-8") as f:
        products = json.load(f)
        for p in products:
            if p['id'] == product_id:
                return p
    return None

if __name__=="__main__":
    print(load_categories())