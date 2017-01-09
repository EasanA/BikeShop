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
        pass
        #run profit
    
    def profit(self):
        pass

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def __repr__(self):
        return ('name:{}: budget:{}').format(self.name, self.budget)
    
    def buy(self, bike_shop, bike):
         print(bike)
         self.budget = self.budget - bike.selling_price
         print(self.budget)
         bike_shop.update_inv(bike)
        
if __name__ == '__main__':
    bike1 = Bike('bike1', 30, 100)
    bike2 = Bike('bike2', 20, 300)
    bike_models = {bike1: 1, bike2 : 2}
    bike_shop = BikeShop(bike_models)
    print(bike1.selling_price)
    customer1 = Customer('bob', 200)
    customers = [customer1]
    print(bike_models)
    print(bike_shop.bikes)
    print(customers)
    print(bike_shop.afford(customer1))
    customer1.buy(bike_shop,bike1)
    print(customer1)