class Vehicle:
    v_count = 0

    '''
    type
    brand
    engine_capacity
    power
    torque
    fuel
    fuel_tank_capacity
    other_details
    mileageData
    '''

    '''
    The following table shows the different behaviour:
    Name:Notation:Behaviour
    name:Public:Can be accessed from inside and outside
    _name:Protected:Like a public member, but they shouldn't be directly accessed from outside.
    __name:Private:Can't be seen and accessed from outside
    '''

    def __init__(self,type_in,brand_in,engine_capacity_in,power_in,torque_in,fuel_in,fuel_tank_capacity_in,other_details_in):
                        self.type =  type_in
                        self.brand= brand_in
                        self.engine_capacity = engine_capacity_in
                        self.power = power_in
                        self.torque = torque_in
                        self.fuel = fuel_in
                        self.fuel_tank_capacity = fuel_tank_capacity_in
                        self.other_details = other_details_in
                        Vehicle.v_count += 1

    #Destroying Objects (Garbage Collection)
    #This __del__() destructor prints the class name of an instance that is about to be destroyed −
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, ": destructor called")

    def showType(self):
        print("Type of Vehicle: ", self.type)

    def showBrand(self):
        print("Brand: ", self.brand)

    def showEngineCapacity(self):
        print("EngineCapacity: ", self.engine_capacity,"CC")

    def showPower(self):
        print("Power: ", self.power,"bhp")

    def showTorque(self):
        print("Torque: ", self.torque,"NM")

    def showFuel(self):
        print("Fuel: ", self.fuel)

    def showFuelTankCapacity(self):
        print("Fuel Tank Capacity: ", self.fuel_tank_capacity,"Ltr")

    def showOtherDetails(self):
        print("Other Details: ", self.other_details)

    def showNoVehicle(self):
        print("Vehicle No: %d" % Vehicle.v_count)


#Creating First Instance Objects
my_first_vehicle = Vehicle("bike","bajaj","200","23","20","Petrol","10","Pulsar")
my_first_vehicle.showType()
my_first_vehicle.showBrand()
my_first_vehicle.showEngineCapacity()
my_first_vehicle.showPower()
my_first_vehicle.showTorque()
my_first_vehicle.showFuel()
my_first_vehicle.showFuelTankCapacity()
my_first_vehicle.showOtherDetails()
my_first_vehicle.showNoVehicle()

#Accessing Attributes
print("Brand of My First Vehicle: %s" % my_first_vehicle.brand)

#Accessing Attributes
print("Vehicle Count:  %d \n" % Vehicle.v_count)

#Creating Other Instance Objects
my_other_vehicle = Vehicle("bike","Yamaha","135","14","13","Petrol","10","RX 5-Speed")

print("\nMy Other Bike")

my_other_vehicle.showType()
my_other_vehicle.showBrand()
my_other_vehicle.showEngineCapacity()
my_other_vehicle.showPower()
my_other_vehicle.showTorque()
my_other_vehicle.showFuel()
my_other_vehicle.showFuelTankCapacity()
my_other_vehicle.showOtherDetails()
my_other_vehicle.showNoVehicle()

#Accessing Attributes
print("Vehicle Count:  %d" % Vehicle.v_count)

# use of other Functions
# to access the attribute of object.
print("Other Vehicle Brand: ", getattr(my_other_vehicle,'brand'))
# to check if an attribute exists or not.
print("is Other Vehicle Other Details Present: ", hasattr(my_other_vehicle,'other_details'))

#to set an attribute. If attribute does not exist, then it would be created.
setattr(my_other_vehicle,'brand','Yamaha-Escort')
print("Other Vehicle Brand: ", getattr(my_other_vehicle,'brand'))

#to delete an attribute.
delattr(my_other_vehicle,'other_details')
# to check if an attribute exists or not.
print("is Other Vehicle Other Details Present: ", hasattr(my_other_vehicle,'other_details'))

#python Built-In Class Attributes

#__doc__ − Class documentation string or none, if undefined.
print ("Vehicle.__doc__:", Vehicle.__doc__)

#__name__ − Class name.
print ("Vehicle.__name__:", Vehicle.__name__)

#__module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print ("Vehicle.__module__:", Vehicle.__module__)

#__bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
print ("Vehicle.__bases__:", Vehicle.__bases__)

#__dict__ − Dictionary containing the class's namespace.
print ("Vehicle.__dict__:", Vehicle.__dict__)

# prints the ids of the obejcts
print (id(my_first_vehicle), id(my_other_vehicle))
del my_first_vehicle
del my_other_vehicle

#Inheritance
class Bike(Vehicle):
    def __init__(self,type_in,brand_in,engine_capacity_in,power_in,torque_in,fuel_in,fuel_tank_capacity_in,other_details_in,bike_type_in):
        Vehicle.__init__(self,type_in,brand_in,engine_capacity_in,power_in,torque_in,fuel_in,fuel_tank_capacity_in,other_details_in)
        self._bike_type = bike_type_in # a protected member

    def showBikeType(self):
        #print("Bike Type: %s", self.bike_type) #AttributeError: 'Bike' object has no attribute 'bike_type'
        print("Bike Type: %s" % self._bike_type)

    #Overriding Methods
    def showBrand(self):
        print("Brand: ", self.brand.upper()) #overriding and printing in UpperCase

#Creating Instance Child
my_inherit_bike = Bike("bike","Bajaj","400","43","43","Petrol","13","Dominar","Tourer")

print("\nMy Inherit Bike")

my_inherit_bike.showType() # parent's method called
my_inherit_bike.showBrand() # child overridden method called
my_inherit_bike.showEngineCapacity() # parent's method called
my_inherit_bike.showPower() # parent's method called
my_inherit_bike.showTorque() # parent's method called
my_inherit_bike.showFuel() # parent's method called
my_inherit_bike.showFuelTankCapacity() # parent's method called
my_inherit_bike.showOtherDetails() # parent's method called
my_inherit_bike.showNoVehicle() # parent's method called
my_inherit_bike.showBikeType() # Child method called


#Operators Overloading
class TotalVehiclePowerNTorque:
    def __init__(self,power,torque):
        self.power = power
        self.torque = torque

    def __str__(self):
        return ("\nVehicles - \n Power: %d \n Torque: %d" %(self.power,self.torque))

    #Overloading add(+) Operator
    def __add__(self, other_vehicle):
        return TotalVehiclePowerNTorque(self.power+other_vehicle.power, self.torque+other_vehicle.torque)

v1power_n_torque = TotalVehiclePowerNTorque(14,13)
v2power_n_torque = TotalVehiclePowerNTorque(23,22)

print (v1power_n_torque)
print (v2power_n_torque)

print("\nTotal Power and Torque of Two Vehicle")
print (v1power_n_torque + v2power_n_torque)


#Inheritance
class Car(Vehicle):
    def __init__(self,type_in,brand_in,engine_capacity_in,power_in,torque_in,fuel_in,fuel_tank_capacity_in,other_details_in,car_type_in,mileage_data):
        Vehicle.__init__(self,type_in,brand_in,engine_capacity_in,power_in,torque_in,fuel_in,fuel_tank_capacity_in,other_details_in)
        self._car_type = car_type_in # a protected member
        self.__mileage_data = mileage_data # a private member(Data Hiding)

    def showCarType(self):
        #print("Bike Type: %s", self.bike_type) #AttributeError: 'Bike' object has no attribute 'bike_type'
        print("Car Type: %s" % self._car_type)

    #Overriding Methods
    def showBrand(self):
        print("Brand: ", self.brand.upper()) #overriding and printing in UpperCase

    #Access Private Member
    def showMileageData(self):
        print("Mileage Data: ", self.__mileage_data,"KM/L") #overriding and printing in UpperCase

#Creating Instance Child
#Creating Instance Child
my_inherit_car = Car("Car","Tata","1198","108","170","Petrol","44","Nixon","SUV","17")

print("\nMy Inherit Car")

my_inherit_car.showType() # parent's method called
my_inherit_car.showBrand() # child overridden method called
my_inherit_car.showEngineCapacity() # parent's method called
my_inherit_car.showPower() # parent's method called
my_inherit_car.showTorque() # parent's method called
my_inherit_car.showFuel() # parent's method called
my_inherit_car.showFuelTankCapacity() # parent's method called
my_inherit_car.showOtherDetails() # parent's method called
my_inherit_car.showNoVehicle() # parent's method called
my_inherit_car.showCarType() # Child method called
#print("Mileage: ",my_inherit_car.__mileage_data) # AttributeError: 'Car' object has no attribute '__mileage_data'
my_inherit_car.showMileageData() # Child method called to show private member data
