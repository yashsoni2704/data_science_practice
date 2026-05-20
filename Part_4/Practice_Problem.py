class Store:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    @staticmethod
    def calc_discount(price,discount):
        result = price - (discount * price/100)
        return result
    
p1 = Store("iphone 14 pro max",140000)
p2 = Store("iphone 14",80000)
print(p1.calc_discount(140000,10))