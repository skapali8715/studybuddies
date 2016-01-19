# Can you fix this code? Give it a try. It's one of the tests to join CodeWars
# Good luck all!

class Person:
  def __init__(self, name):
    self.name = name
  
  def greet(self, other_name):
    return "Hi {0}, my name is {1}".format(other_name, name)
