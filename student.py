class Student:
  school="Akirachix"
  def __init__(self,firstname,lastname,age,country):
   self.firstname=firstname
   self.lastname=lastname
   self.age=age
   self.country=country
  #def greet(self):
      #return f"Hello {self.name} welcome to {self.school}, how is {self.country}" 
  def full_name(self):
      return f"Hello your name is {self.firstname} {self.lastname}"
  def years_of_birth(self) :
      year_of_birth=2022-self.age   
      return f"Hello you age is {year_of_birth}"
  def your_initials(self):
      return f"Hello your initials are {self.firstname[0]} {self.lastname[0]}"    
