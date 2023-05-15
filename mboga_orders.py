class Orders:
    def __init__(self,Name,order,payment,deliveryAdress,status) :
        self.order=order
        self.Name=Name
        self.payment=payment
        self.deliveryAddress=deliveryAdress
        self.status=status
    def add_order(self):
        orders_dict={
           "name":self.Name,
           "order":self.order,
           "payment":self.payment,
           "deliveryAdress":self.deliveryAddress,
           "status":self.status
           
       }
        return orders_dict
    
Name=input("input your name")
order=input("Input the type of order")
payment=input("Input the type of payment")
deliveryAddress=input("Input your delivery address")
status=input("Add status of your order")
    
new_Customer=Orders(Name,order,payment,deliveryAddress,status)
user=new_Customer
print(new_Customer.add_order())
