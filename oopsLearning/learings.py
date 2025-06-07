# to map the real world scenerio, we started using objects in code
# This is called object oriented programming


# class and objects are used to increase readability and decrease redundancy. 
# It's not mandatory to use oops concepts but whenever we feel we can use it


# Difference between classes and object:
# class : Class is the blue print for creating objects

# creating Class:                => Class name must be start with capital letter
#       name = "Karan Kumar"


#creating object (Instance)      => Object are create using class as blueprint 
#       s1 = Student()
#       print(s1.name)


# class Car:
#     company = "BMW"

# car1 = Car()
# print(car1.company)




# __init__ Function
# Constructor: 
# All clases have a fucntion Called __init__(), which is always 
# executed when the class is being initiated.


#creating Class:
# class Student():
    #   def __init__(self, fullname):
    #   self.name = fullname


#creating Object:
#s1 = Student("rohan")
#print(s1.name)

# class Student():

#     def __init__(self,naMe):
#         self.name = naMe
#         print('"',naMe,'"', "is adding to the data base...")

    

# s1 = Student("Dewang")
# print(s1.name)



# the self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class


# class Car():

#     def __init__(self,brand,speciallity):
#         self.brand = brand
#         self.speciallity = speciallity
#         print(self.speciallity)
#         print("Showing the results")


# vehicle1 = Car("BMW",3000)
# print("Brand name is:",vehicle1.brand, "and the Speacillity is:",vehicle1.speciallity , end= "\n")


# vehicle2 = Car("Audi","Speed + Comfort")
# print("Brand name is:",vehicle2.brand, "and the Speacillity is:",vehicle2.speciallity)


########################################################################################################
# There are two type of Constructor

#First is default Constructor

# def __init__(self)  => This is deafult constructor 

# and second constructor is called the parametrized constructor
# def __init__(self ,name ,age)  => constructor run is depend on the match of the parameter.



# Now there are two types of attributes:
# class.attr
# obj.attr


# obj.attr > class.attr

#class.attr => it is used

# class Car():

    # collegeName = "ABCD"     => this is called class oject

#     def __init__(self,brand,speciallity):
#         self.brand = brand                 => this is called ibject attribute    
#         self.speciallity = speciallity
#         print(self.speciallity)
#         print("Showing the results")


# vehicle1 = Car("BMW",3000)
# print("Brand name is:",vehicle1.brand, "and the Speacillity is:",vehicle1.speciallity , end= "\n")


