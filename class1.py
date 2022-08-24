class Item:  # We created a class name Item.
    def calculate_price(self,x,y): # Defined  a method for item class.
        return x*y

item1 = Item() # Created an object  named itme1 of Item class.
item1.name = 'phone' # These are the attributes of item1 object 
item1.price = 100
item1.quantity = 5
print(item1.calculate_price(item1.price,item1.quantity)) # Called the method of Item class using the object item1.


item2 = Item() # Created another object named item2 for Item class.
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
print(item2.calculate_price(item2.price,item2.quantity))