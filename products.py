class Products:                  #define the class product

    def __init__(self, name, description, price, quantity, image):   #initialize attributes
        self.product_name = name
        self.product_description = description
        self.product_price = price
        self.product_quantity = quantity
        self.product_image = image
    
    
    def add_product(self):
        product_dict = {            #structure to enable us to access specific attributes and their values
            "name": self.product_name,
            "description": self.product_description,
            "price": self.product_price,
            "quantity": self.product_quantity,
            "image": self.product_image
        }
        
        return product_dict

products_list = []       #empty list to store all the products that are added


added_products = int(input("How many products do you want to add? "))     #prompt to ask user how many products are to be added


for i in range(added_products):          #iterating over the number of products to be added
    name = input(f"Enter product name {i+1}: ")
    description = input(f"Enter product description {i+1}: ")
    price = float(input(f"Enter product price {i+1}: "))
    quantity = int(input(f"Enter product quantity{i+1}: "))
    image_link = input(f"Enter img link {i+1}: ")
    
    product = Products(name, description, price, quantity, image_link)     #object instantiton
    products_list.append(product)                #adding new products to product list
    
    product_dict = product.add_product()         
    print(product_dict)
    

def edit_products(products_list):          #method to edit details of already existing rpoductd

    edit_product = input("Which product do you want to edit?:")

    for product in products_list:              #iteration through the list of products
        if product.product_name == edit_product:     #checking if the input product matches with any product in the productlist
            new_name = input("Enter new name: ")
            new_description = input("Enter new description: ")
            new_price = float(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))
            new_image_link = input("Enter the new img link: ")
            
            #modifying attributes to new entered values for edited product
            product.product_name = new_name
            product.product_description = new_description
            product.product_price = new_price
            product.product_quantity = new_quantity
            product.product_image = new_image_link
            
            print("Product edited successfully.")

        else:
            print("Product not found.")


edit_products(products_list)

def delete_product(products_list):       #method to remove a product from the list
    delete_product = input("Which product do you want to delete? ")      #prompt to enter name o fproduct to delete

    for product in products_list:      #iteration through our product list
        if product.product_name == delete_product:     #checking if input product is in the list
            products_list.remove(product)
            print("Product deleted successfully.")
        else:
            print("Product not found.")
delete_product(products_list)