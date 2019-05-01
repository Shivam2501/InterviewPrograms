import unittest
from KPCBMap import KPCBMap

class TestKPCBMap(unittest.TestCase):

	# Test to ensure that a fixed sized hash map can be created.
	def testCreateFixedSizeMap(self):
		kpcbMap = KPCBMap(2)
		kpcbMap.set("key1", "value1")
		self.assertTrue(kpcbMap.set("key2", "value2"))
		self.assertFalse(kpcbMap.set("key3", "value3"))

	# Test that set, get and delete works
	def testKeyValue(self):
		kpcbMap = KPCBMap(5)
		kpcbMap.set("key1", "value1")
		kpcbMap.set("key2", 45)
		kpcbMap.set("key3", KPCBMap(5))
		kpcbMap.set("key2", 23)

		self.assertEqual(kpcbMap.get("key1"), "value1")
		self.assertEqual(kpcbMap.get("key2"), 23)

		kpcbMap.delete("key2")
		self.assertEqual(kpcbMap.get("key2"), None)
		self.assertEqual(kpcbMap.delete("key2"), None)

	# Test to verify the load function
	def testCheckLoad(self):
		kpcbMap = KPCBMap(5)
		kpcbMap.set("key1", "value1")
		kpcbMap.set("key2", 45)
		kpcbMap.set("key3", KPCBMap(5))
		kpcbMap.set("key2", 23)

		self.assertEqual(kpcbMap.load(), 0.6)
		kpcbMap.set("key4", "value4")
		kpcbMap.set("key5", "value5")
		
		kpcbMap.set("key6", "value6")
		self.assertEqual(kpcbMap.load(), 1.0)

if __name__ == '__main__':
	unittest.main()