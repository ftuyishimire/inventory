from category import Category
from product import Product

#list to store the products and categories
products = []
categories = []

#function for managing the products in the stock
def add_product(product):
    products.append(product)

def list_products():
    return products

#function that will manage the category of the product in the stock
def add_category(category):
    categories.append(category)

def list_category():
    return categories

