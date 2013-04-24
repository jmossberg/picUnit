###############################################
#Edit the following variables to suite your environment
###############################################

# Location of pcUnit test framework
PICUNIT=../../..

# C compilers ###########
GCC=gcc
XC8=xc8 #C compiler for PIC microcontrollers

# Software under test
ADD2=..
ADD2_SRC=$(ADD2)/src
ADD2_FILES=$(ADD2_SRC)/add2.c
ADD2_SELFTEST=$(ADD2)/tests/add2_test.c
###############################################

###############################################
#The following variables can be left as thery are
###############################################

#Out folders
OUT=../out
XC8_OUT=$(OUT)/xc8
GCC_OUT=$(OUT)/gcc

#Out target names
XC8_TARGET=add2TestXc8
GCC_TARGET=add2TestGcc

#picUnit folders and files
PICUNIT_SRC=$(PICUNIT)/src
PICUNIT_FILES=$(PICUNIT_SRC)/picUnit.c
PICUNIT_PIC_SRC=$(PICUNIT_SRC)/platform/pic
PICUNIT_PIC_FILES=$(PICUNIT_PIC_SRC)/eepromDriver.c $(PICUNIT_PIC_SRC)/picUnit_pic.c
PICUNIT_GCC_SRC=$(PICUNIT_SRC)/platform/gcc
PICUNIT_GCC_FILES=$(PICUNIT_GCC_SRC)/picUnit_gcc.c
###############################################

default: xc8 gcc

clean:
	@rm -rf $(OUT)

clean_xc8:
	@echo XC8: Removing out folder
	@rm -f funclist
	@rm -rf $(XC8_OUT)

xc8: clean_xc8
	@echo XC8: Compiling add2 tests with xc8 for Pic
	@echo
	@mkdir -p $(XC8_OUT)
	$(XC8) --CHIP=16F690 $(PICUNIT_PIC_FILES) $(PICUNIT_FILES) $(ADD2_FILES) $(ADD2_SELFTEST) -I$(PICUNIT_PIC_SRC) -I$(PICUNIT_SRC) -I$(ADD2_SRC) --OUTDIR=$(XC8_OUT) --OUTPUT=intel -O$(XC8_OUT)/$(XC8_TARGET)
	@rm -f funclist

clean_gcc:
	@echo GCC: Removing out folder
	@rm -rf $(GCC_OUT)

gcc: clean_gcc
	@echo GCC: Compiling add2 tests with gcc
	@echo
	@mkdir -p $(GCC_OUT)
	$(GCC) -ggdb $(PICUNIT_GCC_FILES) $(PICUNIT_FILES) $(ADD2_FILES) $(ADD2_SELFTEST) -I$(PICUNIT_GCC_SRC) -I$(PICUNIT_SRC) -I$(ADD2_SRC) -o$(GCC_OUT)/$(GCC_TARGET).o
