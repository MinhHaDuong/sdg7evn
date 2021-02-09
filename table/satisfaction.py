"""Tabulate of answers to the question about electricity sufficiency.

Use VHLSS 2010-2012-2014.
The question was not asked in 2016 and 2018.

(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""
import pandas as pd

from VHLSS_importer import survey

counts = pd.crosstab(survey["Q12"], survey.year, margins=True)


def freq(reply, year):
    total = counts.loc["All", year]
    amount = counts.loc[reply, year]
    percentage = 100 * amount / total
    return "{:4,.1f}%".format(percentage)


def printrow(label, reply):
    print(
        label, freq(reply, 2010.0), freq(reply, 2012.0), freq(reply, 2014.0), sep="\t"
    )


print("Survey year          \t2010\t    2012\t    2014")
print(
    "Responses            \tN={}\tN={}\tN={}".format(
        counts.loc["All", 2010.0], counts.loc["All", 2012.0], counts.loc["All", 2014.0]
    )
)
printrow("Not sufficient      ", "Lacking")
printrow("Sufficient          ", "Enough")
printrow("More than sufficient", "Plenty")
