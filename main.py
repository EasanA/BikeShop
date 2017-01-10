from bicycles import Bike, BikeShop, Customer


if __name__ == '__main__':
    bike1 = Bike('bike1', 30, 100)
    bike2 = Bike('bike2', 20, 300)
    bike3 = Bike('bike3', 22, 500)
    bike4 = Bike('bike4', 19, 700)
    bike5 = Bike('bike5', 15, 900)
    bike6 = Bike('bike6', 25, 400)
    bike_models = {bike1: 4, bike2 : 2, bike3 : 5, bike4 : 0, bike5 : 2, bike6: 4}
    bike_shop = BikeShop(bike_models, 0, 1.2)
    customer1 = Customer('Bob', 200)
    customer2 = Customer('Carol',500)
    customer3 = Customer('John', 1000)
    customers = [customer1, customer2, customer3]
    print(bike_shop.bikes)
    print(customers)
    print('{} can afford {}'.format(customer1.name, bike_shop.afford(customer1)))
    customer1.buy(bike_shop,bike1)
    print('{} can afford {}'.format(customer2.name, bike_shop.afford(customer2)))
    customer2.buy(bike_shop,bike2)
    print('{} can afford {}'.format(customer3.name, bike_shop.afford(customer3)))
    customer3.buy(bike_shop,bike4)
    print('Inventory:{}'.format(bike_models))