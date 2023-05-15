class Products:

    def __init__(self, name, description, price, quantity, image):
        self.product_name = name
        self.product_description = description
        self.product_price = price
        self.product_quantity = quantity
        self.product_image = image
    
    def add_product(self):
        product_dict = {
            "name": self.product_name,
            "description": self.product_description,
            "price": self.product_price,
            "quantity": self.product_quantity,
            "image": self.product_image
        }
        
        return product_dict

# create an empty list to store the products
products_list = []

num_products = int(input("How many products do you want to add? "))

for i in range(num_products):
    name = input(f"Enter the name of product {i+1}: ")
    description = input(f"Enter the description of product {i+1}: ")
    price = float(input(f"Enter the price of product {i+1}: "))
    quantity = int(input(f"Enter the quantity of product {i+1}: "))
    image_url = input(f"Enter the URL of product {i+1} image: ")
    
    product = Products(name, description, price, quantity, image_url)
    products_list.append(product)
    
    product_dict = product.add_product()
    print(product_dict)
    
print("All Products:")
for i, product in enumerate(products_list):
    print(f"Product {i+1} Details:")
    print(f"Name: {product.product_name}")
    print(f"Description: {product.product_description}")
    print(f"Price: {product.product_price}")
    print(f"Quantity: {product.product_quantity}")
    print(f"Image URL: {product.product_image}")
    print()


def edit_products(products_list):
    edit_product = input("Which product do you want to edit?:")

    for product in products_list:
        if product.product_name == edit_product:
            new_name = input("Enter the new name: ")
            new_description = input("Enter the new description: ")
            new_price = float(input("Enter the new price: "))
            new_quantity = int(input("Enter the new quantity: "))
            new_image_url = input("Enter the new image URL: ")
            
            product.product_name = new_name
            product.product_description = new_description
            product.product_price = new_price
            product.product_quantity = new_quantity
            product.product_image = new_image_url
            
            print("Product edited successfully.")
            return

    print("Product not found.")


edit_products(products_list)

def delete_product(products_list):
    delete_product = input("Which product do you want to delete? ")

    for product in products_list:
        if product.product_name == delete_product:
            products_list.remove(product)
            print("Product deleted successfully.")
            return

        print("Product not found.")