import unittest
from MyDict import MyDict
class TestMyDict(unittest.TestCase):
    def test_init(self):

        d = MyDict(a=1,b='test')
        # self.assertEqual(d.a,1)
        # self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))