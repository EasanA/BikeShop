from bicycles import Bike, BikeShop, Customer, Wheel, Frame, BikeManufacturer


if __name__ == '__main__':
    wheel1 = Wheel('wheel1', 5, 20)
    wheel2 = Wheel('wheel2', 4, 100)
    wheel3 = Wheel('wheel3', 3, 250)
    frame1 = Frame('frame1', 10, 75)
    frame2 = Frame('frame2', 8, 250)
    frame3 = Frame('frame3', 4, 400)
    manufacturer1 = BikeManufacturer('Manu1', 1.1)
    manufacturer2 = BikeManufacturer('Manu2', 1.2)
    bike1 = Bike('bike1', wheel1, frame1, manufacturer1)
    bike2 = Bike('bike2', wheel1, frame2, manufacturer1)
    bike3 = Bike('bike3', wheel2, frame2, manufacturer2)
    bike4 = Bike('bike4', wheel3, frame2, manufacturer2)
    bike5 = Bike('bike5', wheel2, frame3, manufacturer2)
    bike6 = Bike('bike6', wheel3, frame3, manufacturer1)
    bike_models = {bike1: 4, bike2 : 2, bike3 : 5, bike4 : 0, bike5 : 0, bike6: 4}
    bike_shop = BikeShop(bike_models, 0, 1.2)
    customer1 = Customer('Bob', 200)
    customer2 = Customer('Carol',500)
    customer3 = Customer('John', 1000)
    customers = [customer1, customer2, customer3]
    print(bike_shop.bikes)
    print(customers)
    print('{} can afford {}'.format(customer1.name, bike_shop.afford(customer1)))
    print(customer1.buy(bike_shop,bike1))
    print('{} can afford {}'.format(customer2.name, bike_shop.afford(customer2)))
    print(customer2.buy(bike_shop,bike4))
    print('{} can afford {}'.format(customer3.name, bike_shop.afford(customer3)))
    print(customer3.buy(bike_shop,bike5))
    print('Inventory:{}'.format(bike_models))