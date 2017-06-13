#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:21:58 2017

@author: haduong
"""


from VHLSS_importer import survey, pd

df = survey[['year', 'elec_poor']]
df.elec_poor = df.elec_poor.cat.remove_categories(['Missing', 'Idk'])
df = df.dropna()
counts = pd.crosstab(df['elec_poor'], df.year, margins=True)

def freq(reply, year):
    total = counts.loc['All', year]
    amount = counts.loc[reply, year]
    percentage = 100 * amount / total
    return "{:,.1f}%".format(percentage)

def printrow(label, reply):
    print(label,
          freq(reply, 2010.0),
          freq(reply, 2012.0),
          freq(reply, 2014.0),
          sep="\t")

print("Survey year          \t2010\t2012\t2014")
print("Responses            \tN={}\tN={}\tN={}".format(counts.loc['All', 2010.0],
                                  counts.loc['All', 2012.0],
                                  counts.loc['All', 2014.0]))
printrow("Not sufficient      ", "Lacking")
printrow("Sufficient          ", "Enough")
printrow("More than sufficient", "Plenty")
