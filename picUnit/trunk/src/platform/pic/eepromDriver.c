#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <xc.h>

int eepromDriver_write(uint8_t* adr_p, uint8_t* dat_p) {

    di(); //disable interrupts

    EEADR = *adr_p; //Data Memory Address to write
    EEDAT = *dat_p; //Data Memory Value to write
    EECON1bits.EEPGD = 0; //Point to DATA memory
    EECON1bits.WREN  = 1; //Enable writes

    //EEPROM write sequence
    EECON2 = 0x55; //Write 55h
    EECON2 = 0xaa; //Write AAh
    EECON1bits.WR = 1; //Set WR bit to begin write

    ei(); //enable interrupts

    while(PIR2bits.EEIF != 1){;} //Wait until EEPROM write finished

    PIR2bits.EEIF = 0;
    EECON1bits.WREN = 0; //Disable writes

    (*adr_p)++;

    return (EXIT_SUCCESS);
}



