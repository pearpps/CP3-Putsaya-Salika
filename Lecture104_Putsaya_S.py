class Customer:
    name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added product to",self.name,self.lastName,"'s Cart")

customer1 = Customer()
customer1.name = "Elon"
customer1.lastName = "M"
customer1.addCart()

customer2 = Customer()
customer2.name = "Jerome"
customer2.lastName = "P"
customer2.addCart()

customer3 = Customer()
customer3.name = "Joe"
customer3.lastName = "B"
customer3.addCart()

customer4 = Customer()
customer4.name = "Mark"
customer4.lastName = "S"
customer4.addCart()

customer5 = Customer()
customer5.name = "Bill"
customer5.lastName = "G"
customer5.addCart()
