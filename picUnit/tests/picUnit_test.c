#include <stdio.h>
#include <stdlib.h>
#include <picUnit.h>
#include <platform.h> //platform specific includes

uint8_t foo = 7;
uint8_t bar = 4;

static uint8_t test_foo() {
    picUnit_assert(foo == 7);
    return 0;
}

static uint8_t test_bar() {
    picUnit_assert(bar == 4);
    return 0;
}

static uint8_t test_foobar() {
    picUnit_assert(foo > bar);
    return 0;
}

static uint8_t all_tests(uint8_t * tests_run_p, uint8_t test_results[]) {
    picUnit_run_test(test_foo, tests_run_p, test_results);
    picUnit_run_test(test_bar, tests_run_p, test_results);
    picUnit_run_test(test_foobar, tests_run_p, test_results);
    return 0;
}

int main(int argc, char **argv) {
    uint8_t tests_run = 0;
    uint8_t test_results[(MAX_NUM_OF_TESTS / 8)] = {0, 0, 0, 0, 0, 0, 0, 0};

    all_tests(&tests_run, test_results);
    //the next line probable does not work because the pointers are not valid in the eeprom driver
    picUnit_writeTestResultsToNonVolatileMemory(&tests_run, test_results);

    /*for(;;)
    {
        ;
    }*/

    return 0;
}
