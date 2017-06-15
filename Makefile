# Makefile for the VHLSS survey analysis about energy poverty
#
# minh.haduong@gmail.com, 2016-2017

PYTHON=python3

# Hires figures
hiresFiguresNames = ECDspending ECDuse TariffCompared
hiresFiguresFiles = $(addsuffix .pdf,$(hiresFiguresNames)) $(addsuffix -300dpi.png,$(hiresFiguresNames))

# Also used in the paper
figuresNames = blockTariff elec_yearbyIncome kWhbyIncome powerGridMaps prices unsatisfactionMaps KPIDiagram
figuresFiles = $(addsuffix .png,$(figuresNames) $(hiresFiguresNames))

tablesNames = incomeShare KPI table_satisfaction table_TariffWinners table_TariffLIHC
tablesFiles = $(addsuffix .txt,$(tablesNames))


# Exploratory data visualization
moreFiguresNames= boxGrid electricityBills scatterMatrix densitykWh incomeShare separation powerLowUseMaps mosaics
moreFiguresFiles=$(addsuffix .png,$(moreFiguresNames))

moreTablesNames= crossTables summaryTables quantileskWh
moreTablesFiles=$(addsuffix .txt,$(moreTablesNames))

figures=$(figuresFiles) $(moreFiguresFiles)
tables=$(tablesFiles) $(moreTablesFiles)


defaut:
	make -j5 all

all: $(figures) $(tables) $(imageSets)

%.png: %.py
	$(PYTHON) $^

%.txt: %.py
	$(PYTHON) $^ > $@

.PHONY: clean cleaner

clean:
	-rm  $(hiresFiguresFiles) $(figures) $(tables) $(imageSets)  2> /dev/null

cleaner: clean
	-rm -rf __pycache__/  2> /dev/null

