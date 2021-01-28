# Statistics on energy poverty in Vietnam
#
# (c) 2016-2017 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
"""Quantiles of the electricity use distribution Vientam households

Comparing the general sample with the households declaring their electricity needs not met
"""

from VHLSS_importer import survey
from scipy.stats import percentileofscore

all_households = survey.loc[survey.year2014, 'kwh_last_month']
lacking_households = all_households.loc[survey.lacking]
lt30_households = all_households.loc[survey.low_use]
hicost_households = all_households.loc[survey.high_cost]

print("       Households \tAll      \tNot sufficient electricity")
print("                  \tn = {:d}\tn = {:d}".format(
      all_households.count(), lacking_households.count()
      ))

print("Electricity use last month")

print("Median            \t{:.0f} kWh   \t{:.0f} kWh".format(
      all_households.median(), lacking_households.median()
      ))

print("50% interquartile \t{:.0f}-{:.0f} kWh   \t{:.0f}-{:.0f} kWh".format(
      all_households.quantile(0.25), all_households.quantile(0.75),
      lacking_households.quantile(0.25), lacking_households.quantile(0.75)
      ))

print("90% interquartile \t{:.0f}-{:.0f} kWh   \t{:.0f}-{:.0f} kWh".format(
      all_households.quantile(0.05), all_households.quantile(0.95),
      lacking_households.quantile(0.05), lacking_households.quantile(0.95)
      ))

print()
medPoor = lacking_households.median()
numPoor = lacking_households.count() // 2
print('\nHalf of the self-declared electricity poors households used less than',
      medPoor, 'kWh in the month')
print('That is', numPoor, 'respondents\n')

p = percentileofscore(all_households, medPoor)
numSober = round(p * all_households.count() / 100)
print('Among all households, {:.1f} percent of respondents used less than that'.format(p))
print('That is {:.0f} respondents\n'.format(numSober))

odd = (numSober - numPoor) / numPoor

print('Among the households using less than', medPoor, 'kWh last month,')
print('For one who declares lacking electricity, {:.1f} declare having enough'.format(odd))
