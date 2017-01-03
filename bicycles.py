class Bike(object):
    def __init__(self, name, weight, prod_cost):
        self.name = name
        self.weight = weight
        self.cost_price = prod_cost
        self.selling_price = 0

class BikeShop(object):
    def __init__(self, bikes):
        self.margin = 1.2
        self.bikes = bikes
        for bike in bikes:
            bike.selling_price = self.margin * bike.cost_price
    
class Customer(object):
    pass

if __name__ == '__main__':
    bike1 = Bike('bike1', 30, 100)
    bike_models = [bike1]
    bike_shop = BikeShop(bike_models)
    print(bike1.selling_price)