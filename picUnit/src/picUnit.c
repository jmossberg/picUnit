#include <picUnit.h>

uint8_t picUnit_run_test(uint8_t (*test_function)(), uint8_t * noOfTestsRun_p, uint8_t testResults[])
{
  if(PICUNIT_TEST_FAILED == test_function())
  {
    picUnit_report_test_failed(noOfTestsRun_p, testResults);
  }
  else
  {
    picUnit_report_test_passed(noOfTestsRun_p, testResults);
  }
  return 0;
}

static uint8_t picUnit_report_test_failed(uint8_t * noOfTestsRun_p, uint8_t testResults[])
{
  uint8_t byteInArray = *noOfTestsRun_p / 8;
  uint8_t bitInByte = *noOfTestsRun_p % 8;
  (*noOfTestsRun_p)++;
  setbit(testResults[byteInArray], bitInByte);
  return 0;
}

static uint8_t picUnit_report_test_passed(uint8_t * noOfTestsRun_p, uint8_t testResults[])
{
  uint8_t byteInArray = *noOfTestsRun_p / 8;
  uint8_t bitInByte = *noOfTestsRun_p % 8;
  (*noOfTestsRun_p)++;
  clrbit(testResults[byteInArray], bitInByte);
  return 0;
}

