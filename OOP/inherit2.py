from budget import Vegetable
"""
class Vegtable(object):
	def __init__(self,name,price):
		self.name = name
		self.price = price

	def display(self):
		print(f'{self.name}  {self.price}')
"""

class Onion(Vegetable):
	def __init__(self,name, price, amount):
		Vegetable.__init__(self,name,price)
		self.amount = amount

	def cost(self):
		return self.amount*self.price


o = Onion("onion", 30, 2)
o.display()
print(o.cost())
