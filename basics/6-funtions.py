# def print_my_list_of_products(products):
#     for product, details in products.items():
#         print(f"Product: {product}, Price: ${details['price']}, Quantity: {details['qty']}, Category: {details['category']}")   
# def calculate_total_price(products):
#     if products['category'] == 'electronics':
#         total_price = products['price'] * products['qty'] * 1.1  # Add 10% tax
#         return total_price
#     elif products['category'] == 'furniture':
#         total_price = products['price'] * products['qty'] * 1.05  # Add 5% tax
#         return total_price
#     elif products['category'] == 'stationery':
#         total_price = products['price'] * products['qty'] * 1.02  # Add 2% tax
#         return total_price
# # products = [
# #     "laptop": {"price": 999.99, "qty": 5, "category": "electronics"},
# #     "mouse": {"price": 29.99, "qty": 50, "category": "electronics"},
# #     "desk": {"price": 299.99, "qty": 12, "category": "furniture"},
# #     "chair": {"price": 199.99, "qty": 8, "category": "furniture"},
# #     "monitor": {"price": 349.99, "qty": 15, "category": "electronics"},
# #     "keyboard": {"price": 79.99, "qty": 30, "category": "electronics"},
# #     "headphones": {"price": 149.99, "qty": 20, "category": "electronics"},
# #     "lamp": {"price": 59.99, "qty": 25, "category": "furniture"},
# #     "notebook": {"price": 9.99, "qty": 100, "category": "stationery"},
# #     "pen": {"price": 1.99, "qty": 200, "category": "stationery"}
# # ]
# products = {
#     "laptop": {"price": 999.99, "qty": 5, "category": "electronics"},
#     "mouse": {"price": 29.99, "qty": 50, "category": "electronics"},
#     "desk": {"price": 299.99, "qty": 12, "category": "furniture"},
#     "chair": {"price": 199.99, "qty": 8, "category": "furniture"},
#     "monitor": {"price": 349.99, "qty": 15, "category": "electronics"},
#     "keyboard": {"price": 79.99, "qty": 30, "category": "electronics"},
#     "headphones": {"price": 149.99, "qty": 20, "category": "electronics"},
#     "lamp": {"price": 59.99, "qty": 25, "category": "furniture"},
#     "notebook": {"price": 9.99, "qty": 100, "category": "stationery"},
#     "pen": {"price": 1.99, "qty": 200, "category": "stationery"}
# }
# print_my_list_of_products(products) # This will print the list of products with their details
# print(calculate_total_price(products['laptop']))  # This will print the total price of the laptop with tax

# print(calculate_total_price(products[0]))  # This will print the total price of the laptop with tax



# from util import print_my_list_of_products, calculate_total_price, calculate_price_with_gst  
import util.reuse as util
        

##Create a list of dictionary with products and their prices with name, price, quantity, and category.
products = [
    {"name": "Apple", "price": 0.5, "quantity": 10, "category": "Fruit"},
    {"name": "Banana", "price": 0.3, "quantity": 20, "category": "Fruit"},
    {"name": "Carrot", "price": 0.2, "quantity": 15, "category": "Vegetable"},
    {"name": "Broccoli", "price": 0.4, "quantity": 5, "category": "Vegetable"},
    {"name": "Milk", "price": 1.0, "quantity": 10, "category": "Dairy"},
    {"name": "Cheese", "price": 2.5, "quantity": 5, "category": "Dairy"}
]
    

util.print_my_list_of_products(products)
print(util.calculate_total_price(products[0]))  # Output: 4.5 (0.5 * 10 * 0.9)
util.print_my_list_of_products(products)
print(util.calculate_price_with_gst(products[2]))  # Output: 5.04 (4.5 * 1.12 for Fruit)

##if you get the JSON data we can use the json module to convert it to a python object
import json
# Example JSON data
json_data =    '''
[
    {"name": "Apple", "price": 0.5, "quantity": 10, "category": "Fruit"},
    {"name": "Banana", "price": 0.3, "quantity": 20, "category": "Fruit"},
    {"name": "Carrot", "price": 0.2, "quantity": 15, "category": "Vegetable"},
    {"name": "Broccoli", "price": 0.4, "quantity": 5, "category": "Vegetable"},
    {"name": "Milk", "price": 1.0, "quantity": 10, "category": "Dairy"},
    {"name": "Cheese", "price": 2.5, "quantity":    5, "category": "Dairy"}
]'''
# Convert JSON data to Python object
products_from_json = json.loads(json_data)
util.print_my_list_of_products(products_from_json)
print(util.calculate_total_price(products_from_json[0]))  # Output: 4.5
