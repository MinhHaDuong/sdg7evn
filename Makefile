# Makefile for the VHLSS survey analysis about energy poverty
#
# minh.haduong@gmail.com, 2016-2017

PYTHON=python3

# Hires figures
hiresFiguresNames = ECDspending ECDuse TariffCompared kWhbyIncome figure_effort KPIDiagram blockTariff figure_highexpense mapGrid prices mapUnsatisfaction 
hiresFiguresFiles = $(addsuffix .pdf,$(hiresFiguresNames)) $(addsuffix -300dpi.png,$(hiresFiguresNames))

# Also used in the paper
figuresNames = 
figuresFiles = $(addsuffix .png,$(figuresNames) $(hiresFiguresNames))

tablesNames = effort KPI satisfaction TariffWinners TariffLIHC kwh_quantiles
tablesFiles = $(addsuffix .txt,$(tablesNames))


# Exploratory data visualization
moreFiguresNames= boxGrid electricityBills scatterMatrix densitykWh incomeShare separation
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

%.txt: table/%.py
	$(PYTHON) -m table.$* > $@

.PHONY: clean cleaner

clean:
	-@rm  $(hiresFiguresFiles) $(figures) $(tables) 2> /dev/null || true

cleaner: clean
	-rm -rf __pycache__/  2> /dev/null
