# sdg7evn
Is electricity affordable and reliable for all in Vietnam - analysis of household surveys

This python code analyzes VHLSS results regarding to energy poverty.

Requirements:
  Python3 with SciPy stack (pandas >= 18.1, numpy, matplotlib, statsmodels)
  Python3 libraries pyshp, matplotlib_venn
  make
  Preprocessed VHLSS data located in   ../data/Processed_data
  Shapefiles for Vientam provinces located in  ../data/VNM_adm_shp


Use:
  make -j5


Source code organization:

 VHLSS_importer.py   reads the data tables, cleans them and exports the "survey" dataframe to all other scripts.
                     Since it is the common header file, it also defines auxilliary functions

 mapTinh.py          a module for Choropleth plots:  mapping a numerical function by province in Vietnam

 
 other files are scripts, independent from each other so they can be run in parallel using the -j5 option in the make command
 some scripts produce one table
 some scripts produce one figure
 some scripts are only used for exploratory data analysis, they are not run by the Makefile
