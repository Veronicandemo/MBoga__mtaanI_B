class Vendor:
    def __init__(self,store_name,store_location,store_description,vendor_id,vendor_name):
        self.store_name = store_name
        self.store_location = store_location
        self.store_description = store_description
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        
    def create_user(self):
        user_dict={
            "name":self.vendor_name,
            "id":self.vendor_id,
            "store":self.store_name,
            "location":self.store_location,
            "description":self.store_description
             
        }
        return user_dict

store_name = input("Enter name of the store :")
store_location = input("Enter the store's location :")
store_description = input("Enter a short decription of the store:")
vendor_id = input("Input the vendor's unique Id:")
vendor_name = input("Input the vendor's name:")
    
new_vendor = Vendor(store_name,store_location,store_description,vendor_id,vendor_name)
new_user = Vendor(store_name,store_location,store_description,vendor_id,vendor_name)
print(new_vendor.create_user())
