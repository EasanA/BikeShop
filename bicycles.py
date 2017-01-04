class Bike(object):
    def __init__(self, name, weight, prod_cost):
        self.name = name
        self.weight = weight
        self.cost_price = prod_cost
        self.selling_price = 0

    def __repr__(self):
        return ('model:{}: price:{}').format(self.name, self.selling_price)
        
class BikeShop(object):
    def __init__(self, bikes):
        self.margin = 1.2
        self.bikes = bikes
        for bike in bikes:
            bike.selling_price = self.margin * bike.cost_price
    
class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def __repr__(self):
        return ('name:{}: budget:{}').format(self.name, self.budget)

if __name__ == '__main__':
    bike1 = Bike('bike1', 30, 100)
    bike2 = Bike('bike2', 20, 300)
    bike_models = [bike1, bike2]
    bike_shop = BikeShop(bike_models)
    print(bike1.selling_price)
    customer1 = Customer('bob', 200)
    customers = [customer1]
    print(bike_models)
    print(customers)