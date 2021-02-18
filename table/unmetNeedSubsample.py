"""Compare the households declaring they lacked electricity with others.

In terms of quantiles of the electricity use distribution, Vietnam households.
Use VHLSS 2014 as the question about needs met was not asked in 2016 and 2018.

(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import pandas as pd

from VHLSS_importer import survey
from scipy.stats import percentileofscore


def describe(sample, fs, label):
    q1 = fs.format(sample.quantile(0.25))
    q2 = fs.format(sample.quantile(0.50))
    q3 = fs.format(sample.quantile(0.75))
    v1 = fs.format(sample.quantile(0.05))
    v19 = fs.format(sample.quantile(0.95))

    description = {
        "n =": sample.count(),
        "Median":  q2,
        "Interquartile range": '-'.join([q1, q3]),
        " 5-95 centile range": '-'.join([v1, v19])}
    return pd.Series(description, name=label)


def compare(year, column, fs, subsample, heading):
    """Print a table comparing the distribution of a variable for a subsample.

    The variable is a column name, can be "kwh_last_month" or "effort"
    The subsample can be survey.lacking, survey.low_use or survey.high_cost.
    """
    whole = survey.loc[survey.year == year, column]
    subsample = whole.loc[subsample]
    col1 = describe(whole, fs, "All")
    col2 = describe(subsample, fs, heading)
    table = col1.to_frame()
    table[heading] = col2
    print(table)
    return whole, subsample


compare(2014, "kwh_last_month", "{:.0f} kWh",
        survey.lacking, "Not sufficient electricity")


# %%


def results(year):
    print()
    print("============================================")
    print("Results for year", year, "\n")
    print()
    print("Electricity use last month")
    all_households, lacking_households = compare(
        year,
        "kwh_last_month",
        "{:.0f} kWh",
        survey.lacking,
        "Not sufficient electricity")
    print()
    print("Effort")
    compare(year, "effort", "{:.3f}",
            survey.lacking, "Not sufficient electricity")

    print()
    medPoor = lacking_households.median()
    numPoor = lacking_households.count() // 2
    print(
        "\nHalf of the self-declared electricity poors households used less than",
        medPoor,
        "kWh in the month",
        )
    print("That is", numPoor, "respondents\n")
    p = percentileofscore(all_households.dropna(), medPoor)
    numSober = round(p * all_households.count() / 100)
    print(
        "Among all households, {:.1f} percent of respondents used less than that".format(p)
        )
    print("That is {:.0f} respondents\n".format(numSober))
    odd = (numSober - numPoor) / numPoor
    print("Among the households using less than", medPoor, "kWh last month,")
    print(
        "For one who declares lacking electricity, {:.1f} declare having enough".format(odd)
         )


# results(2010)
results(2014)
