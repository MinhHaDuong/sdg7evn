# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
##
# Created on Tue Oct 11 07:14:08 2016
#


from VHLSS_importer import survey, YEARS, gini
from scipy.stats import percentileofscore


def cdf(yr):
    d = survey.loc[survey.year == yr, "kwh_last_month"].dropna()
    print("\nIn year {:d} the Gini index was {:.1f}".format(yr, 100 * gini(d)))
    print("The fraction of households who declared they used")
    print(
        "... less than 50 kWh on electricity in the previous month was {:.1f}%".format(
            percentileofscore(d, 50)
        )
    )
    print(
        "... less than 100 kWh on electricity in the previous month was {:.1f}%".format(
            percentileofscore(d, 100)
        )
    )
    print("Distribution of declared electricity use (kWh in previous month)")
    print(d.describe())


for year in YEARS[1:]:
    cdf(year)
