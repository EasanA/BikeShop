from bicycles import Bike, BikeShop, Customer


if __name__ == '__main__':
    bike1 = Bike('bike1', 30, 100)
    bike2 = Bike('bike2', 20, 300)
    bike_models = {bike1: 4, bike2 : 2}
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
    print(bike_models)