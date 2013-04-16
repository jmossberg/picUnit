import sys
import getopt
import subprocess


def readEeprom(eeprom_file):
	f1 = open(eeprom_file, mode="r")
	f1.readline()
        eeprom = f1.readline()
        eeprom = f1.readline()
        eeprom = f1.readline()
	nrOfRuns = int(eeprom[5:7], 16)
	testResultsBitLevel = []
	testResultsBitLevel.append(int(eeprom[9:11], 16))
	testResultsBitLevel.append(int(eeprom[13:15], 16))
	testResultsBitLevel.append(int(eeprom[17:19], 16))
	testResultsBitLevel.append(int(eeprom[21:23], 16))
	testResultsBitLevel.append(int(eeprom[25:27], 16))
	testResultsBitLevel.append(int(eeprom[29:31], 16))
	testResultsBitLevel.append(int(eeprom[33:35], 16))
        eeprom2 = f1.readline()
	testResultsBitLevel.append(int(eeprom2[5:7], 16))
	f1.close()
	return nrOfRuns, testResultsBitLevel

def readGccTestResults(result_file):
	f1 = open(result_file, mode="r")
        results = f1.readline()
	nrOfRuns = int(results[0:2], 16)
	testResultsBitLevel = []

	testResultsBitLevel.append(int(results[3:5], 16))
	testResultsBitLevel.append(int(results[6:8], 16))
	testResultsBitLevel.append(int(results[9:11], 16))
	testResultsBitLevel.append(int(results[12:14], 16))
	testResultsBitLevel.append(int(results[15:17], 16))
	testResultsBitLevel.append(int(results[18:20], 16))
	testResultsBitLevel.append(int(results[21:23], 16))
	testResultsBitLevel.append(int(results[24:26], 16))

	f1.close()
	return nrOfRuns, testResultsBitLevel

def getTestResults(testResultsBitLevel):
	testResults = []

	for testResultByte in testResultsBitLevel:
		for i in range(0, 8):
			testResults.append((testResultByte >> i) & 1)
	
	return testResults

def getTestCaseNames(testCaseNames_file):
	testCaseNames = []
	noOfTests = 0
	f1 = open(testCaseNames_file, mode="r")
	for line in f1:
		noOfTests = noOfTests + 1
		testCaseNames.append(line)
	f1.close()
	return noOfTests, testCaseNames
	
def writeResultsToXML(nrOfRuns, nrOfTests, testResults, testCaseNames, xml_file):
	f2 = open(xml_file, mode="w")
	f2.write('<?xml version="1.0" encoding="UTF-8"?>\n')
	f2.write('<testsuites tests="' + str(nrOfTests) + '" failures="0" disabled="0" errors="0" time="0" name="AllTests">\n')
	f2.write('  <testsuite name="lcdDriver" tests="' + str(nrOfTests) + '" failures="0" disabled="0" errors="0" time="0">\n')

	for index, testCaseName in enumerate(testCaseNames):
		f2.write('    <testcase name="' + testCaseName.rstrip('\n') + '" status="run" time="0" classname="lcdDriver">')
		if (testResults[index] == 1):
			f2.write('\n        <failure message="failure" type="failed">test1</failure>\n')
		f2.write('    </testcase>\n')

	f2.write('  </testsuite>\n')
	f2.write('</testsuites>\n')
	f2.close()

def main(argv):
	result_file = ''
	xml_file = ''
	testCaseNames_file = ''
	platform = ''
	try:
		opts, args = getopt.getopt(argv,"p:r:x:t:")
	except getopt.GetoptError:
		print 'generateJunitReportFromEeprom.py -p <platform> -r <result_file> -x <xml_file> -t <testCaseNames_file>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-p':
			platform = arg
		elif opt == '-r':
			result_file = arg
		elif opt in ("-x"):
			xml_file = arg
		elif opt in ("-t"):
			testCaseNames_file = arg

	if platform == 'pic':
		nrOfRuns, testResultsBitLevel = readEeprom(result_file)
	else:
		nrOfRuns, testResultsBitLevel = readGccTestResults(result_file)
		
	testResults = getTestResults(testResultsBitLevel)
	nrOfTests, testCaseNames = getTestCaseNames(testCaseNames_file)
	writeResultsToXML(nrOfRuns, nrOfTests, testResults, testCaseNames, xml_file)

if __name__ == "__main__":
	main(sys.argv[1:])
