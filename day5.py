#Oops
#qn1
'''class Vehicle:
    def __init__(self,vehicle_id,vehicle_type,vehicle_cost):
        self.__vehicle_id=vehicle_id
        self.__vehicle_type=vehicle_type
        self.__vehicle_cost=vehicle_cost
        self.__premium_amount=None
    def calculate_premium(self):
        if self.__vehicle_type.lower()=="two wheeler":
            self.__premimum_amount=0.02*self.__vehicle_cost
        elif self.__vehicle_type.lower()=="four wheeler":
            self.__premimum_amount=0.06*self.__vehicle_cost
        else:
            raise ValueError("Invalid vehicle type")

    def get_vehicle_id(self):
        return self.__vehicle_id
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type

    def get_vehicle_cost(self):
        return self.__vehicle_cost   
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost

    def get_premium_amount(self):
        return self.__premimum_amount



vehicle1 = Vehicle("V001", "Two Wheeler", 50000)
vehicle2 = Vehicle("V002", "Four Wheeler", 100000)

# Set instance variables using setter methods
vehicle1.set_vehicle_id("V003")
vehicle1.set_vehicle_type("Four Wheeler")
vehicle1.set_vehicle_cost(75000)

# Calculate premium for all vehicles
vehicle1.calculate_premium()
vehicle2.calculate_premium()

# Display vehicle details
print("Vehicle ID:", vehicle1.get_vehicle_id())
print("Vehicle Type:", vehicle1.get_vehicle_type())
print("Vehicle Cost:", vehicle1.get_vehicle_cost())
print("Premium Amount:", vehicle1.get_premium_amount())
print()
print("Vehicle ID:", vehicle2.get_vehicle_id())
print("Vehicle Type:", vehicle2.get_vehicle_type())
print("Vehicle Cost:", vehicle2.get_vehicle_cost())
print("Premium Amount:", vehicle2.get_premium_amount())'''

#qn2
'''class student:
    def _init_(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    def set_details(self,sid,sm,sa):
        self.__student_id=sid
        self.__marks=sm
        self.__age=sa
    def validate_marks(self):
        if 100>=self.__marks>=0:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
        else:
            return True
    def choose_course(self):
        if self.check_qualification():
            self.fees=None
            self.course=int(input("\nyou are eligible for admission,\ninput 1001 to choose course 1001 (default fees 25575.0)\ninput 1002 to choose course 1002 (default fees 15500.0)\nyour choice: "))
            if self.course==1001 and self.__marks>85:
                self.fees =25575.0- 0.25*25575.0
            elif self.course==1001 and self.__marks<=85:
                self.fees =25575.0
            elif self.course==1002 and self.__marks>85:
                self.fees =15500.0- 0.25*15500.0
            elif self.course==1002 and self.__marks<=85:
                self.fees =15500.0
            print(f"\nyou have joined course {self.course} and your fees is {self.fees}")
            

s1=student()
s1.set_details(int(input("enter id: ")),int(input("enter marks: ")),int(input("enter age: ")))
s1.choose_course()'''


#qn3

class Customer:
    def validate_quantity(self, quantity):
        if quantity >= 1 and quantity <= 5:
            return True
        else:
            return False

class PizzaService:
    counter = 100
    
    def __init__(self, pizza_type, quantity, additional_topping):
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.additional_topping = additional_topping
        self.pizza_cost = -1
        
    def validate_pizza_type(self):
        if self.pizza_type.lower() == "small" or self.pizza_type.lower() == "medium":
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer().validate_quantity(self.quantity):
            pizza_cost_table = {"small": 150, "medium": 200}
            additional_topping_cost_table = {"small": 35, "medium": 50}
            
            pizza_cost = pizza_cost_table[self.pizza_type.lower()] * self.quantity
            if self.additional_topping:
                pizza_cost += additional_topping_cost_table[self.pizza_type.lower()] * self.quantity
                
            self.pizza_cost = pizza_cost
            self.service_id = self.pizza_type[0].upper() + str(PizzaService.counter + 1)
            PizzaService.counter += 1
            
        else:
            self.pizza_cost = -1
    
class DoorDelivery(PizzaService):
    def __init__(self, pizza_type, quantity, additional_topping, distance_in_kms):
        super().__init__(pizza_type, quantity, additional_topping)
        self.distance_in_kms = distance_in_kms
        
    def validate_distance_in_kms(self):
        if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
            return True
        else:
            return False
        
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms() and super().calculate_pizza_cost() != -1:
            delivery_charge_table = {1: 5, 6: 7}
            
            if self.distance_in_kms <= 5:
                self.pizza_cost += delivery_charge_table[1] * self.quantity
            else:
                self.pizza_cost += delivery_charge_table[1] * self.quantity
                self.pizza_cost += delivery_charge_table[6] * (self.distance_in_kms - 5) * self.quantity
                
        else:
            self.pizza_cost = -1

# Testing
pizza_service = PizzaService("Small", 3, True)
pizza_service.calculate_pizza_cost()
print("Service ID:", pizza_service.service_id)
print("Pizza cost:", pizza_service.pizza_cost)

door_delivery = DoorDelivery("Medium", 2, False, 8)
door_delivery.calculate_pizza_cost()
print("Service ID:", door_delivery.service_id)
print("Pizza cost:", door_delivery.pizza_cost)




















