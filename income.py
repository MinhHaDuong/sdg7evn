# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, gini, CPI, pd

pd.set_option('precision', 0)


def cdf(yr):
    print('\n---------------------')
    print('Income of vietnamese households declared for year', yr)
    d = survey[survey.year == yr].inc.dropna() / 1000
    sorted = d.sort_values()
# Would need to look at the official poverty lines
#    print('having used less than 50 kWh on electricity in the previous month was ', end='')
#    print(round(100 * (len(d[d <= 50]) + len(d[d < 50])) / 2 / len(d), 1), '%')
#    print('having used less than 100 kWh on electricity in the previous month was ', end='')
#    print(round(100 * (len(d[d <= 100]) + len(d[d < 100])) / 2 / len(d), 1), '%')
    print('The Gini index: was ', end='')
    print(round(100 * gini(sorted), 2), '\n')
    print('Nominal amounts (M VND per year)')
    print(d.describe())
    print('\nDeflated to 2014 (M VND per year)')
    deflator = float(CPI.Consumer_Price_Index["2014"]) / float(CPI.Consumer_Price_Index[str(yr)])
    dd = d * deflator
    print(dd.describe())

cdf(2008)
cdf(2010)
cdf(2012)
cdf(2014)

print('\n-------------------------')
print('Real increase of mean', 106 - 95, 'M VND2014')
print('Real increase of median', 81 - 69, 'M VND2014')