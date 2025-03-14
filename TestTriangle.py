# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','201,201,201 is an InvalidInput')
        
    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','-1,-1,-1 is an InvalidInput')
        
    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle('-1',-1,-1),'InvalidInput','\'-1\',-1,-1 is an InvalidInput')
        
    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,1,5),'NotATriangle','1,1,5 is not a Triangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIsoscelesTriangle(self): 
        self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,3,5 is an Isosceles triangle')
        
    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 is an Scalene triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

