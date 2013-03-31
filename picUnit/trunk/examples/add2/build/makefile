#Myunit folders
PICUNIT=../../..
PICUNIT_SRC=$(PICUNIT)/src
PICUNIT_HEADER=$(PICUNIT_SRC)
PICUNIT_TESTS=$(PICUNIT)/tests

#Myunit source code files
PICUNIT_FILES=$(PICUNIT_SRC)/picUnit.c
PICUNIT_SELFTEST=$(PICUNIT_TESTS)/picUnit_test.c

#PIC Platform
##PIC tools
PICUNIT_PIC_COMPILER=/opt/microchip/xc8/v1.11/bin/xc8
PICUNIT_PIC_PK2CMD=../../../tools/pk2cmd
PICUNIT_PIC_PK2CMD=/home/jacob/svntrac/cidemo/tools/pk2cmd
PICUNIT_PIC_TARGET=add2TestPic
##PIC folders
PICUNIT_PIC_SRC=$(PICUNIT_SRC)/platform/pic
PICUNIT_PIC_INC_DIRS=$(PICUNIT_PIC_SRC)
PICUNIT_PIC_OUT=$(PICUNIT)/out/xc8
##PIC Platform specific souce code
PICUNIT_PIC_FILES=$(PICUNIT_PIC_SRC)/eepromDriver.c $(PICUNIT_PIC_SRC)/picUnit_pic.c

#GCC Platform
##GCC Tools
PICUNIT_GCC_COMPILER=gcc
PICUNIT_GCC_TARGET=add2TestGcc
##GCC folders
PICUNIT_GCC_SRC=$(PICUNIT_SRC)/platform/gcc
PICUNIT_GCC_INC_DIRS=$(PICUNIT_GCC_SRC)
PICUNIT_GCC_OUT=$(PICUNIT)/out/gcc
##GCC Platform specific source code
PICUNIT_GCC_FILES=$(PICUNIT_GCC_SRC)/picUnit_gcc.c

#add2
ADD2_TESTS=../tests
ADD2_SELFTEST=$(ADD2_TESTS)/add2_test.c
ADD2=../src
ADD2_FILES=$(ADD2)/add2.c
ADD2_HEADER=$(ADD2)
ADD2_OUT_PIC=../out/pic
ADD2_OUT_GCC=../out/gcc

default: clean buildpic buildgcc runpic rungcc printpic printgcc

clean:
	@echo Cleaning files
	rm -f $(ADD2_OUT_PIC)/*
	rm -f funclist
	rm -f $(ADD2_OUT_GCC)/*

buildpic: clean
	@echo PIC: Compiling add2 test with xc8 for Pic
	$(PICUNIT_PIC_COMPILER) --CHIP=16F690 $(PICUNIT_PIC_FILES) $(PICUNIT_FILES) $(ADD2_FILES) $(ADD2_SELFTEST) -I$(PICUNIT_SRC) -I$(PICUNIT_PIC_INC_DIRS) -I$(ADD2_SELFTEST_HEADER) -I$(ADD2_HEADER) --OUTDIR=$(ADD2_OUT_PIC) --OUTPUT=intel -O$(ADD2_OUT_PIC)/$(PICUNIT_PIC_TARGET)
	rm -f funclist

runpic: buildpic
	@echo PIC: Load program on to PIC
	$(PICUNIT_PIC_PK2CMD)/pk2cmd -PPIC16F690 -B$(PICUNIT_PIC_PK2CMD) -F$(ADD2_OUT_PIC)/$(PICUNIT_PIC_TARGET).hex -M
	@echo      Power on PIC
	$(PICUNIT_PIC_PK2CMD)/pk2cmd -PPIC16F690 -B$(PICUNIT_PIC_PK2CMD) -T -R
	@echo      Wait 2 seconds
	sleep 2
	@echo      Power down PIC
	$(PICUNIT_PIC_PK2CMD)/pk2cmd -PPIC16F690 -B$(PICUNIT_PIC_PK2CMD) -W
	@echo      Read EEPROM memory
	$(PICUNIT_PIC_PK2CMD)/pk2cmd -PPIC16F690 -B$(PICUNIT_PIC_PK2CMD) -GE0-ff | tee $(ADD2_OUT_PIC)/eeprom.txt
	@echo      Parse test names
	cat $(ADD2_SELFTEST) | grep picUnit_run_test | sed 's/^.*(//g' | sed 's/,.*$$//g' | tee $(ADD2_OUT_PIC)/testNames.txt
	@echo      Generate test report in xml format
	python $(PICUNIT_SRC)/generateJunitReportFromEeprom.py -p pic -r $(ADD2_OUT_PIC)/eeprom.txt -x $(ADD2_OUT_PIC)/add2_testresults.xml -t $(ADD2_OUT_PIC)/testNames.txt

printpic: runpic
	@echo
	@echo PIC: Test results in Jenkins XML-format
	cat $(ADD2_OUT_PIC)/add2_testresults.xml

buildgcc: clean
	@echo GCC: Compiling add2 test with gcc
	$(PICUNIT_GCC_COMPILER) -ggdb $(PICUNIT_GCC_FILES) $(PICUNIT_FILES) $(ADD2_FILES) $(ADD2_SELFTEST) -I$(PICUNIT_SRC) -I$(PICUNIT_GCC_INC_DIRS) -I$(ADD2_HEADER) -o$(ADD2_OUT_GCC)/$(PICUNIT_GCC_TARGET).o


rungcc: buildgcc
	@echo
	@echo GCC: Running $(PICUNIT_GCC_TARGET)
	$(ADD2_OUT_GCC)/$(PICUNIT_GCC_TARGET).o | tee $(ADD2_OUT_GCC)/testResults.txt
	@echo Parse test case names in $(ADD2_SELFTEST)
	cat $(ADD2_SELFTEST) | grep picUnit_run_test | sed 's/^.*(//g' | sed 's/,.*$$//g' | tee $(ADD2_OUT_GCC)/testNames.txt
	@echo Generate test report $(ADD2_OUT_GCC)/add2_testresults.xml in Jenkins XML format
	python $(PICUNIT_SRC)/generateJunitReportFromEeprom.py -p gcc -r $(ADD2_OUT_GCC)/testResults.txt -x $(ADD2_OUT_GCC)/add2_testresults.xml -t $(ADD2_OUT_GCC)/testNames.txt

printgcc: rungcc
	@echo
	@echo GCC: Test results $(ADD2_OUT_GCC)/add2_testresults.xml in Jenkins XML-format
	@cat $(ADD2_OUT_GCC)/add2_testresults.xml
