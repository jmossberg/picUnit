#include <picUnit.h> //test framework
#include <add2.h> //module to test

uint8_t a = 1;
uint8_t b = 2;

static uint8_t test_1plus2() {
    picUnit_assert(3 == add2(a,b));  
    return 0;
}

static uint8_t test_1plus3() {
    picUnit_assert(4 == add2(1,3));
    return 0;
}

static uint8_t all_tests(uint8_t * tests_run_p, uint8_t test_results[]) {
    picUnit_run_test(test_1plus2, tests_run_p, test_results);
    picUnit_run_test(test_1plus3, tests_run_p, test_results);
    return 0;
}

int main(int argc, char **argv) {
    uint8_t tests_run = 0;
    uint8_t test_results[(MAX_NUM_OF_TESTS / 8)] = {0, 0, 0, 0, 0, 0, 0, 0};

    all_tests(&tests_run, test_results);
    //the next line probable does not work because the pointers are not valid in the eeprom driver
    picUnit_writeTestResultsToNonVolatileMemory(&tests_run, test_results);

    return 0;
}
