
# class Car:

#     car_name = "Allion"

#     def move(self):
#         print(self.car_name, "is moving")


# class Truck:

#     truck_name = "ACL"

#     def move(self):
#         print(self.truck_name, "is moving")

    
# class Bike:

#     bike_name = "Honda"

#     def move(self):
#         print(self.bike_name, "is moving")


# vehicles = [Car(), Truck(), Bike()]

# for vehicle in vehicles:
#     vehicle.move()






# print(len("mahbub"))

# print(len([23, 4, 6, 2, 7]))



# def add(x, y, z = 0):
    
#     return x + y + z

# print(add(2, 3))
# print(add(2, 3, 4))





# class BD:

#     def capital(self):
#         print("Dhaka is capital of Bangladesh")
    
#     def language(self):
#         print("Bangla is the primary language of Bangladesh")
    
#     def type(self):
#         print("Bangladesh is developing country")
    

# class USA:
    
#     def capital(self):
#         print("Wahington, D.C is capital of USA")
    
#     def language(self):
#         print("English is the primary language of USA")
    
#     def type(self):
#         print("USA is a developed country")
    

# bangladesh = BD()
# america = USA()

# for country in (bangladesh, america):
#     country.capital()
#     country.language()
#     country.type()
    






class Bird:

    def intro(self):
        print("There are many types of birds")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")
    

class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
    

class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")
    

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


























