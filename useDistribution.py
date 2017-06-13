# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
##
# Created on Tue Oct 11 07:14:08 2016
#


from VHLSS_importer import survey, gini, pd

pd.set_option('precision', 0)


def cdf(yr):
    d = survey[survey.year == yr].kwh_last_month.dropna()
    sorted = d.sort_values()
    print('\nIn year', yr, 'the fraction of households who declared ')
    print('having used less than 50 kWh on electricity in the previous month was ', end='')
    print(round(100 * (len(d[d <= 50]) + len(d[d < 50])) / 2 / len(d), 1), '%')
    print('having used less than 100 kWh on electricity in the previous month was ', end='')
    print(round(100 * (len(d[d <= 100]) + len(d[d < 100])) / 2 / len(d), 1), '%')
    print('The Gini index: was ', end='')
    print(round(100 * gini(sorted), 2), '\n')
    print(d.describe())
#    print(100 * relative_mean_absolute_difference(sorted))

cdf(2010)
cdf(2012)
cdf(2014)
