from bicycles import Bike, BikeShop, Customer


if __name__ == '__main__':
    bike1 = Bike('bike1', 30, 100)
    bike2 = Bike('bike2', 20, 300)
    bike3 = Bike('bike3', 22, 500)
    bike4 = Bike('bike4', 19, 700)
    bike5 = Bike('bike5', 15, 900)
    bike6 = Bike('bike6', 25, 400)
    bike_models = {bike1: 4, bike2 : 2, bike3 : 5, bike4 : 1, bike5 : 2, bike6: 4}
    bike_shop = BikeShop(bike_models)
    customer1 = Customer('Bob', 200)
    customer2 = Customer('Carol',500)
    customer3 = Customer('Bob', 1000)
    customers = [customer1, customer2, customer3]
    print(bike_shop.bikes)
    print(customers)
    print(bike_shop.afford(customer1))
    print(bike_shop.afford(customer2))
    print(bike_shop.afford(customer3))
    customer1.buy(bike_shop,bike1)
    customer2.buy(bike_shop,bike2)
    customer3.buy(bike_shop,bike4)
    print(customer1)
    print(customer2)
    print(customer3)
    print(bike_models)