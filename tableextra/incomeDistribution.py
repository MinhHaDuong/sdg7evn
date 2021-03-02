# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, gini, CPI, YEARS


def cdf(yr):
    print("\n---------------------")
    print("Income of vietnamese households declared for year", yr)
    d = survey.loc[survey.year == yr, "inc"].dropna() / 1000
    print("The Gini index was {:.2f}".format(100 * gini(d)))
    print("\nNominal amounts (M VND per year)")
    print(d.describe())
    print("\nDeflated to 2014 (M VND per year)")
    deflator = float(CPI["2014"]) / float(CPI[str(yr)])
    dd = d * deflator
    print(dd.describe())


[cdf(y) for y in YEARS]