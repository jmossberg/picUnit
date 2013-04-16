#include <stdint.h>
#include <stdio.h>

uint8_t picUnit_writeTestResultsToNonVolatileMemory(uint8_t * noOfTestsRun_p, uint8_t * testResults_p)
{
  uint8_t i = 0;

  printf("%02x", *noOfTestsRun_p);

  for(i = 0; i < 8; i++)
  {
    printf(" %02x", *(testResults_p + i));
  }

  printf("\n");
 
  return 0;
}

