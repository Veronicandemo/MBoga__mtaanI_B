class CheckOrders:
    def __init__(self,customerName):
        self.orders = []
        self.customerName=customerName
    def add_order(self, order):
        self.orders.append(order)
    def remove_order(self, order):
        self.orders.remove(order)
    def get_orders(self):
        return self.orders
    def get_order_by_id(self, Name):
        for order in self.orders:
            if Name == Name:
                return order
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
my_orders = CheckOrders("John Doe")
new_order = Orders("123", "Product A", 10.99,"JNFJ","LDJNF")
print(my_orders.add_order(new_order))
all_orders = my_orders.get_orders()
Name = "123"
order = my_orders.get_order_by_id(Name)
