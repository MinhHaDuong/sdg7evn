# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# The data distribution is shown on "elec_yearbyIncome.py"
"""Electricity bill as a fraction of income in the VHLSS.
"""

from VHLSS_importer import survey


def summary_stat(year):
    """Summary statistics of the distribution of effort, for a given year

    Effort is the fraction of income spend on the electricity bill"""
    effort = survey.loc[survey.year == year, 'effort'].dropna()

    sample_size = len(effort)
    pay_nothing = len(effort[effort == 0]) / sample_size * 100
    pay_much = len(effort[effort >= 0.06]) / sample_size * 100
    median = effort.quantile(0.5) * 100
    top_vintile = effort.quantile(0.95) * 100
    return pay_nothing, pay_much, median, top_vintile


def row(heading, unit, index):
    "Table summarizing the evolution of the electricity bill effort in Vietnam households"
    row_string = heading + "\t{:,.2f}%\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\t" + unit
    row_data = (summary_stat(year)[index] for year in [2008, 2010, 2012, 2014])
    return row_string.format(*row_data)


print("Survey year                          \t2008\t2010\t2012\t2014")
print(row("Households not paying anything  ", "of households", 0))
print(row("Hh paying >6% of income on electricity", "of households", 1))
print(row("Half of households pay less than", "of income on electricity", 2))
print(row("95% of households pay less than ", "of income on electricity", 3))
