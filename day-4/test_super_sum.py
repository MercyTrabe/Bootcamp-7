
import unittest
from super_sum import super_sum
class SuperSumTestCase(unittest.TestCase):
	def test_empty_input(self):
		self.assertEqual(super_sum(), 0)

	def test_sum_of_integers(self):

		self.assertEqual(super_sum(1,2,3), 6)
		self.assertEqual(super_sum(-1,1), 0)


	def test_sum_of_items_in_one_list(self):

		self.assertEqual(super_sum([1,2,3]), 6)

	def test_sum_of_string(self):
		self.assertEqual(super_sum('string',1,4),0)
