class Vegetable(object):
	def __init__(self,name,price):
		self.name = name
		self.price = price

	def display(self):
		print(f'{self.name}  {self.price}')


