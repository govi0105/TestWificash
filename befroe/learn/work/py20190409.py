# import unittest
#
# class Test_StartEnd(unittest.TestCase):
#     def setUp(self):
#         print("--Test Start--")
#
#     def tearDown(self):
#         print("--Test End--")
#
# class Test2(Test_StartEnd):
#     def test_c(self):
#         print("C")
#
#     def test_b(self):
#         print("B")
#
# class Test1(Test_StartEnd):
#     def test_a(self):
#         print("A")
#
# class Test3(Test_StartEnd):
#     def test_d(self):
#         print("D")
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(Test3("test_d"))
#     suite.addTest(Test2("test_c"))
#     suite.addTest(Test1("test_a"))
#     suite.addTest(Test2("test_b"))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
     print(k, v)