from datetime import datetime
"""import unittest


class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(True, False)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()"""

now = datetime.now()

print(now.strftime("%A %d. %b %Y"))
print(now.strftime('%c'))
print(now.strftime("%I:%M%p %a %d. %b %Y"))
print(now.strftime('%d/%m/%Y'))

def double(x):
    return x*x

def doubled(func, *args):
    return [func(x) for x in args]

print(doubled(double,1,2,3))

















