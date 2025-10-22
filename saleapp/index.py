from flask import Flask, render_template,request
import dao

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get('q')
    category_id = request.args.get('category_id')
    products = dao.load_products(keyword=q, category_id=category_id)
    return render_template("index.html",  products=products, query=q)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = dao.get_product_by_id(product_id)
    if product is None:
        return "Sản phẩm không tồn tại", 404
    return render_template("product_detail.html", product=product)

@app.context_processor
def common_attribute():
    return {
        "cates" : dao.load_categories()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)