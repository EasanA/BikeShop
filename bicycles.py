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
            
            
    def afford(self, customer):
    #need to make a afford function that filters through the bike_models list and prints bikes within customer's budget
        affordable =[]
        for bike in self.bikes:
            if bike.selling_price <= customer.budget:
                affordable.append(bike) 
        return affordable
        
    def update_inv(self, bike):   
        self.bikes[bike] -= 1
        self.profit(bike)
    
    def profit(self, bike):
        shop_profit = 0
        profit_per_bike = bike.selling_price - bike.cost_price
        shop_profit += profit_per_bike 
        print(shop_profit)
        return(shop_profit)

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def __repr__(self):
        return ('name:{}: budget:{}').format(self.name, self.budget)
    
    def buy(self, bike_shop, bike):
         print(bike)
         self.budget -= bike.selling_price
         print(self.budget)
         bike_shop.update_inv(bike)