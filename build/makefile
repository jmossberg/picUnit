#picUnit folders
PICUNIT=..
PICUNIT_SRC=$(PICUNIT)/src
PICUNIT_HEADER=$(PICUNIT_SRC)
PICUNIT_TESTS=$(PICUNIT)/tests

#picUnit source code files
PICUNIT_FILES=$(PICUNIT_SRC)/picUnit.c
PICUNIT_SELFTEST=$(PICUNIT_TESTS)/picUnit_test.c

#PIC Platform
##PIC tools
PIC_COMPILER=/opt/microchip/xc8/v1.11/bin/xc8
PIC_PK2CMD=../../../tools/pk2cmd
PIC_TARGET=picUnittestpic
##PIC folders
PIC_SRC=$(PICUNIT_SRC)/platform/pic
PIC_INC_DIRS=$(PIC_SRC)
PIC_OUT=$(PICUNIT)/out/xc8
##PIC Platform specific souce code
PIC_FILES=$(PIC_SRC)/eepromDriver.c $(PIC_SRC)/picUnit_pic.c

#GCC Platform
##GCC Tools
GCC_COMPILER=gcc
GCC_TARGET=picUnittestgcc
##GCC folders
GCC_SRC=$(PICUNIT_SRC)/platform/gcc
GCC_INC_DIRS=$(GCC_SRC)
GCC_OUT=$(PICUNIT)/out/gcc
##GCC Platform specific source code
GCC_FILES=$(GCC_SRC)/picUnit_gcc.c

all: runonpic 

clean:
	rm -f $(PIC_OUT)/*
	rm -f funclist
	rm -f $(GCC_OUT)/*

buildforpic: clean
	@echo Creating folder $(PIC_OUT) if does not exist
	mkdir -p $(PIC_OUT)
	@echo Compiling picUnit test with xc8 for Pic
	$(PIC_COMPILER) --CHIP=16F690 $(PIC_FILES) $(PICUNIT_FILES) $(PICUNIT_SELFTEST) -I$(PICUNIT_SRC) -I$(PIC_INC_DIRS) --OUTDIR=$(PIC_OUT) --OUTPUT=intel -O$(PIC_OUT)/$(PIC_TARGET)
	@echo Removing funclist file
	rm -f funclist

buildforgcc: clean
	@echo Creating folder $(GCC_OUT) if does not exist
	mkdir -p $(GCC_OUT)
	@echo Compiling picUnit test with gcc
	$(GCC_COMPILER) $(GCC_FILES) $(PICUNIT_FILES) $(PICUNIT_SELFTEST) -I$(PICUNIT_SRC) -I$(GCC_INC_DIRS) -o$(GCC_OUT)/$(GCC_TARGET).o

runonpic: buildforpic
	@echo Load program on to PIC
	$(PIC_PK2CMD)/pk2cmd -PPIC16F690 -B$(PIC_PK2CMD) -F$(PIC_OUT)/$(PIC_TARGET).hex -M
	@echo Power on PIC
	$(PIC_PK2CMD)/pk2cmd -PPIC16F690 -B$(PIC_PK2CMD) -T -R
	@echo Wait 2 seconds
	@sleep 2
	@echo Power down PIC
	$(PIC_PK2CMD)/pk2cmd -PPIC16F690 -B$(PIC_PK2CMD) -W
	@echo Read EEPROM memory
	$(PIC_PK2CMD)/pk2cmd -PPIC16F690 -B$(PIC_PK2CMD) -GE0-ff | tee $(PIC_OUT)/eeprom.txt
	@echo Parse test names
	cat $(PICUNIT_SELFTEST) | grep picUnit_run_test | sed 's/^.*(//g' | sed 's/,.*$$//g' | tee $(PIC_OUT)/testNames.txt
	@echo Generate test report in xml format
	python $(PICUNIT_SRC)/generateJunitReportFromEeprom.py -p pic -r $(PIC_OUT)/eeprom.txt -x $(PIC_OUT)/picUnit_testresults.xml -t $(PIC_OUT)/testNames.txt

runongcc: buildforgcc
	@echo Running $(GCC_TARGET)
	$(GCC_OUT)/$(GCC_TARGET).o | tee $(GCC_OUT)/testResults.txt
	@echo Parse test names
	cat $(PICUNIT_SELFTEST) | grep picUnit_run_test | sed 's/^.*(//g' | sed 's/,.*$$//g' | tee $(GCC_OUT)/testNames.txt
	@echo Generate test report in xml format
	python $(PICUNIT_SRC)/generateJunitReportFromEeprom.py -p gcc -r $(GCC_OUT)/testResults.txt -x $(GCC_OUT)/picUnit_testresults.xml -t $(GCC_OUT)/testNames.txt
