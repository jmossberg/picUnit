import sys
import getopt
import subprocess
#from mockfileobject import open


def getResultStringFromFile(fileObject):
    resultString = fileObject.readline()
    fileObject.close()
    return resultString

def getNumberOfTests(resultString):
    numberOfTests = int(resultString[0:2], 16)
    return numberOfTests

" First test is denoted with testNo = 0  "
def getTestResult(resultString, testNo):
    "Get word, One word is 2 bytes, First byte is wordIndex = 0"
    wordIndex = testNo / 16 
    startPosition = 3 + (3 * wordIndex) 
    endPosition = startPosition + 2
    word = int(resultString[startPosition:endPosition], 16) 

    "Get bit"
    noOfBitsToShift = testNo % 16
    bit = (word >> noOfBitsToShift) & 1
    return bit
