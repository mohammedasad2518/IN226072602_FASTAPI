from fastapi import FastAPI

app = FastAPI()

# Product list
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI store"}


# Task 1 - Get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


# Task 2 - Filter products by category
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):

    filtered_products = [
        p for p in products
        if p["category"].lower() == category_name.lower()
    ]

    if not filtered_products:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": filtered_products,
        "total": len(filtered_products)
    }


# Task 3 - Show only in-stock products
@app.get("/products/in-stock")
def get_in_stock_products():

    in_stock_products = [
        p for p in products if p["in_stock"] == True
    ]

    return {
        "in_stock_products": in_stock_products,
        "total": len(in_stock_products)
    }


# Task 4 - Filter products by price range
@app.get("/products/price-range")
def get_products_by_price(min_price: int, max_price: int):

    filtered_products = [
        p for p in products
        if min_price <= p["price"] <= max_price
    ]

    return {
        "min_price": min_price,
        "max_price": max_price,
        "products": filtered_products,
        "total": len(filtered_products)
    }


# Task 5 - Search products by name
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }


# Task 6 - Store summary
@app.get("/store/summary")
def store_summary():

    in_stock_count = len([p for p in products if p["in_stock"]])
    out_of_stock_count = len(products) - in_stock_count

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }