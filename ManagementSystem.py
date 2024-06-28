class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner 
    
              
        def update_owner(self, new_owner):
            self.owner = new_owner


vehicle1 = Vehicle("123ABC", "Car", "John")
vehicle2 = Vehicle("456DEF", "Motorcycle", "Alice")


print("Initial Owners:")
print("Vehicle 1 - Owner:", vehicle1.owner)
print("Vehicle 2 - Owner:", vehicle2.owner)


vehicle1.update_owner("Mike")
vehicle2.update_owner("Emma")


print("\nUpdated Owners:")
print("Vehicle 1 - Owner:", vehicle1.owner)
print("Vehicle 2 - Owner:", vehicle2.owner)
            



# class Event:
#         def __init__(self, name, date):
#             self.name = name
#             self.date = date