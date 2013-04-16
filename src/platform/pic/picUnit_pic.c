#include <eepromDriver.h>
#include <stdint.h>

static uint8_t picUnit_writeTestResultsToEeprom(uint8_t * noOfTestsRun_p, uint8_t * testResults_p)
{
  uint8_t adr = 0x00;
  eepromDriver_write(&adr, noOfTestsRun_p);

  for(uint8_t i = 0; i < 8; i++)
  {
    eepromDriver_write(&adr, (testResults_p + i));
  }
 
  return 0;
}

uint8_t picUnit_writeTestResultsToNonVolatileMemory(uint8_t * noOfTestsRun_p, uint8_t * testResults_p)
{
  picUnit_writeTestResultsToEeprom(noOfTestsRun_p, testResults_p);
  return 0;
}

