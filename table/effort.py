"""Tabulate electricity bill as a fraction of income in the VHLSS.

Statistics on energy poverty in Vietnam
(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE.
We censor 2008 pending verification that the numbers are comparable.
"""

import pandas as pd

from VHLSS_importer import survey, YEARS


def fmt(percent):
    """Format the percentage float as a string."""
    return "{:4.1f}%".format(100 * percent)


def summary_stat(year):
    """Summary statistics of the distribution of effort, for a given year.

    Effort is the fraction of income spend on the electricity bill.
    """
    effort = survey.effort[survey.year == year].dropna()

    sample_size = len(effort)
    pay_nothing = fmt(len(effort[effort <= 0.001]) / sample_size)
    pay_much = fmt(len(effort[effort > 0.06]) / sample_size)
    median = fmt(effort.quantile(0.5))
    top_vintile = fmt(effort.quantile(0.95))
    return pay_nothing, pay_much, median, top_vintile


labels = [
    "Households not paying anything  ",
    "Hh paying >6% of income on electricity",
    "Half of households pay less than",
    "95% of households pay less than "
]
contents = [summary_stat(year) for year in YEARS]
table = pd.DataFrame(contents, index=YEARS, columns=labels).transpose()

pd.set_option('display.max_columns', len(YEARS))
pd.set_option('display.width', 150)
print(table)
