# class Animal():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def speak(self):
#         return f"{self.name} billi"

#     def get_age(self):
#         return f"age is {self.age}"

# # class Dog(Animal):       # This is how you inherit a class, here Dog is child ,and Animal is parent
# #     def speak(self):
# #         return f"{self.name} bhai"   
    
# class Jungle():
#     def __init__(self,pos):
#         self.pos=pos
#     def position(self):
#         return self.pos
    
# class Sher(Animal,Jungle):
#     def it_speak(self,pos):
#         # super().__init__(self.name, self.age)
#         super().__init__(self.pos)
#         return f"{self.name} bhau who is {self.age} years old and position is {self.pos}"

# s1=Sher("simbha",4)
# # s1.__init__("simbha", 6)
# print(s1.it_speak("sher"))

# d1=Dog("Dogesh",9)
# print(d1.speak(),d1.get_age())          # Here I'm calling a method which is not present in the child class
# print()

# c1=Animal("billu",5) 
# print(c1.speak(),c1.get_age())      
import math
print(math.comb(12,9))         
"""It selects the number of possiblities 
of k things from n items 
first param -> n
second param -> k
n,k range [0,+infinity]"""