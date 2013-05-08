"""Unittest for generatetestreport.py"""

import generatetestreport
import unittest

class GenerateTestReportTests(unittest.TestCase):
    def testOpenInputFile(self):
        result = generatetestreport.openInputFile()
        self.assertEqual(1, result)

    def testGetNumberOfTests(self):
        resultString = "02 00 00 00 00 00 00 00 00"
        result = generatetestreport.getNumberOfTests(resultString) 
        self.assertEqual(2, result)

        resultString = "0A 00 00 00 00 00 00 00 00"
        result = generatetestreport.getNumberOfTests(resultString) 
        self.assertEqual(10, result)
        
        resultString = "40 00 00 00 00 00 00 00 00"
        result = generatetestreport.getNumberOfTests(resultString) 
        self.assertEqual(64, result)

    def testGetTestResultFirstTestPassed(self):
        resultString = "02 00 00 00 00 00 00 00 00"

        testNo = 0
        result = generatetestreport.getTestResult(resultString, testNo)
        self.assertEqual(0, result)

    def testGetTestResultFirstTestFailed(self):
        resultString = "02 01 00 00 00 00 00 00 00"

        testNo = 0
        result = generatetestreport.getTestResult(resultString, testNo)
        self.assertEqual(1, result)

    def testGetTestResultSecondTestFailed(self):
        resultString = "02 02 00 00 00 00 00 00 00"

        testNo = 1
        result = generatetestreport.getTestResult(resultString, testNo)
        self.assertEqual(1, result)

    def testGetTestResultTestSeventeenFailed(self):
        resultString = "02 00 01 00 00 00 00 00 00"

        testNo = 16
        result = generatetestreport.getTestResult(resultString, testNo)
        self.assertEqual(1, result)

        
if __name__ == "__main__":
    unittest.main() 
