import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for letter in sentence:
		if letter == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		highest_stock = 0
		hs_item = self.items[0]
		for item in self.items:
			if item.stock > highest_stock:
				highest_stock = item.stock
				hs_item = item

		return hs_item
			

	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		highest_price = 0
		hp_item = self.items[0]
		for item in self.items:
			if item.price > highest_price:
				highest_price = item.price
				hp_item = item
		return hp_item

			



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a('apple'), 1) 


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		w = Warehouse()
		w.add_item(self.item1)
		it = w.items[0].price
		self.assertEqual(it, 6)
		w.add_item(self.item2)
		it = w.items[1].price
		self.assertEqual(it, 5)


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		w = Warehouse()
		w.add_item(self.item1)
		w.add_item(self.item2)
		w.add_item(self.item3)
		max_item = w.get_max_stock()
		self.assertEqual(max_item.stock, 100)
		w.add_item(self.item4)
		w.add_item(self.item5)
		max_item = w.get_max_stock()
		self.assertEqual(max_item.stock, 100)
		




	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		w = Warehouse()
		w.add_item(self.item1)
		w.add_item(self.item2)
		w.add_item(self.item3)
		max_item = w.get_max_price()
		self.assertEqual(max_item.price, 6)
		w.add_item(self.item4)
		w.add_item(self.item5)
		max_item = w.get_max_price()
		self.assertEqual(max_item.price, 6)
		

def main():
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()