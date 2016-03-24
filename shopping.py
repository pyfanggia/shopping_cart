class ShoppingCart(object):
	"""Create shopping cart object for website users"""

	items_in_cart = {'mango': 0,
	                 'apple': 0,
	                 'pear': 0,
	                 'banana':0
	                 }
	items_price = {'mango': 3,
	               'apple': 2,
	               'pear': 2,
	               'banana': 1
	               }

	def __init__(self, user):
		self.user = user

	def add_item(self, item, num):
		self.items_in_cart[item] += num
		print "you've added %d %s." % (num, item)
		return self.items_in_cart

	def remove_item(self, item, num):
		if self.items_in_cart[item] - num >= 0:
			self.items_in_cart[item] -= num
			print "you've removed %d %s." % (num, item)
		else:
			self.items_in_cart[item] = 0
			print "there is now no %s in the shopping cart." % item
		return self.items_in_cart

	def bill(self):
		total = 0
		for item in self.items_in_cart:
			total += self.items_in_cart[item] * self.items_price[item]
		print "total: %d" % total
