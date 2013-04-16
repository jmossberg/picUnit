#include <stdint.h>

// helper macros
#define testbit(var, bit) ((var) & (1 <<(bit)))
#define setbit(var, bit) ((var) |= (1 << (bit)))
#define clrbit(var, bit) ((var) &= ~(1 << (bit))) 

// asserts
#define picUnit_assert(test) do { if (!(test)) return 1; } while (0)

#define MAX_NUM_OF_TESTS 64

static const uint8_t PICUNIT_TEST_FAILED = 1;
static const uint8_t PICUNIT_TEST_PASSED = 0;

static uint8_t testResults[(MAX_NUM_OF_TESTS / 8)];

uint8_t picUnit_run_test(uint8_t (*test_function)(), uint8_t * noOfTestsRun_p, uint8_t testResults[]); 
uint8_t picUnit_writeTestResultsToNonVolatileMemory(uint8_t * noOfTestsRun_p, uint8_t testResults[]);

static uint8_t picUnit_report_test_failed(uint8_t * noOfTestsRun_p, uint8_t * testResults_p);
static uint8_t picUnit_report_test_passed(uint8_t * noOfTestsRun_p, uint8_t * testResults_p);
