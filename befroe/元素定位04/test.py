#python 3.6
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  TestCases.test2 import data
import unittest
import ddt
@ddt.ddt
class MyTestCase2(unittest.TestCase):
    @ddt.data((1, 2), (2, 3))
    @ddt.unpack
    def test_1_tuple(self, value1, value2):
        print(value1, value2)

    @ddt.data([1, 2], [2, 3])
    @ddt.unpack
    def test_0_list(self, value1, value2):
        print(value1, value2)

    @ddt.data(*data)
    def test_2_dict(self, data):
        print(data["user"],data["pwd"])

if __name__ == '__main__':
    unittest.main()