"""Compare the households declaring they lacked electricity with others.

In terms of quantiles of the electricity use distribution, Vietnam households.
Use VHLSS 2014 as the question about needs met was not asked in 2016 and 2018.

(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

from VHLSS_importer import survey
from scipy.stats import percentileofscore


def results(year):
    all_households = survey.kwh_last_month[survey.year == year]
    lacking_households = all_households.loc[survey.lacking]
    lt30_households = all_households.loc[survey.low_use]
    hicost_households = all_households.loc[survey.high_cost]
    print("============================================")
    print("Results for year", year, "\n")
    print("       Households \tAll      \tNot sufficient electricity")
    print(
        "                  \tn = {:d}\tn = {:d}".format(
            all_households.count(), lacking_households.count()
            )
        )
    print("Electricity use last month")
    print(
        "Median            \t{:.0f} kWh   \t{:.0f} kWh".format(
            all_households.median(), lacking_households.median()
            )
        )
    print(
        "50% interquartile \t{:.0f}-{:.0f} kWh   \t{:.0f}-{:.0f} kWh".format(
            all_households.quantile(0.25),
            all_households.quantile(0.75),
            lacking_households.quantile(0.25),
            lacking_households.quantile(0.75),
            )
        )
    print(
        "90% interquartile \t{:.0f}-{:.0f} kWh   \t{:.0f}-{:.0f} kWh".format(
            all_households.quantile(0.05),
            all_households.quantile(0.95),
            lacking_households.quantile(0.05),
            lacking_households.quantile(0.95),
            )
        )
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


results(2010)
results(2014)
results(2018)
