from category import Category
from product import Product
import inventory_manager

#create entry point for categories and products in the inventory system
#creating also object instances for class product and category

electronic_category = Category(1, 'Electronics')
clothing_category = Category(2, 'clothing')

laptop = Product(1001, 'laptop', 400.45, electronic_category)
shirt = Product(201, 'shirt', 23.99, clothing_category)

#adding these products and categories in the inventory

inventory_manager.add_category(electronic_category)
inventory_manager.add_category(clothing_category)

inventory_manager.add_product(laptop)
inventory_manager.add_product(shirt)

#listing products and these added categories through methods that return elements in these variables of products and categories

print("Categories")
for category in inventory_manager.list_category():
    print(f"{category.category_id} : {category.category_name}")

print("\n Products:")
for product in inventory_manager.list_products():
    print(f"{product.product_id} : {product.product_name} ${product.product_price} in {product.category.category_name}")


