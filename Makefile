# Makefile for the VHLSS survey analysis about energy poverty
#
# minh.haduong@gmail.com, 2016-2021

PYTHON=python3

# Figures and tables used in the paper
pythonFiguresNames = ECDspending ECDuse effort KPIDiagram subsidies highexpense mapGrid prices inequalities mapSatisfaction 
odgFiguresNames = block_tariff_example

figuresFiles = $(addsuffix .png,$(pythonFiguresNames) $(odgFiguresNames))
hiresFiguresFiles = $(addsuffix -300dpi.png,$(pythonFiguresNames)) $(addsuffix .svg,$(odgFiguresNames))

tablesNames = effort kpi satisfaction unmetNeedSubsample useDistribution summaryTables
tablesFiles = $(addsuffix .txt,$(tablesNames))

# Extra figures and tables, used for exploratory data visualization
moreFiguresNames= boxGrid electricityBills kWhbyIncome scatterMatrix densitykWh incomeShare separation blockTariff mapLowUse TariffImpacts TariffCompared
moreFiguresFiles=$(addsuffix .png,$(moreFiguresNames))

moreTablesNames= TariffWinners TariffLIHC crossTables incomeDistribution poorNumbersByCriteria
moreTablesFiles=$(addsuffix .txt,$(moreTablesNames))

figures=$(figuresFiles) $(hiresFiguresFiles) $(moreFiguresFiles)
tables=$(tablesFiles) $(moreTablesFiles)

default:
	make -j5 results

results: $(figuresFiles) $(hiresFiguresFiles) $(tablesFiles)

extra: $(moreFiguresFiles) $(moreTablesFiles)

all: results extra

%.png %-300dpi.png: figure/%.py
	$(PYTHON) -m figure.$*

%.png: figure/%.odg
	libreoffice --convert-to png $^

%.svg: figure/%.odg
	libreoffice --convert-to svg $^

%.png: figureextra/%.py
	$(PYTHON) -m figureextra.$*

%.txt: table/%.py
	$(PYTHON) -m table.$* > $@

%.txt: tableextra/%.py
	$(PYTHON) -m tableextra.$* > $@

.PHONY: default results extra all clean cleaner

clean:
	-@rm $(figures) $(tables) 2> /dev/null || true

cleaner: clean
	-rm -rf __pycache__/  2> /dev/null
