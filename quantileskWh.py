# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, pd
from scipy.stats import percentileofscore

df = survey[['year','elec_poor','kwh_last_month']]
df.elec_poor = df.elec_poor.cat.remove_categories(['Missing', 'Idk'])
df = df.dropna()
e = df.kwh_last_month[survey.year == 2014]

def desc(serie):
    return serie.describe(percentiles = [0.05, 0.25, 0.5, 0.75, 0.95])

table = pd.DataFrame(
[desc(e),
 desc(e[survey.elec_poor == 'Lacking']),
 desc(e[survey.elec_poor != 'Lacking'])
 ])

print(table)

medPoor = e[survey.elec_poor == 'Lacking'].median()
numPoor = round(len(e[survey.elec_poor == 'Lacking'])/2)
print('\nHalf of the self-declared electricity poors households used less than', medPoor, 'kWh in the month')
print('That is', numPoor, 'respondents')

p = percentileofscore(e, medPoor)
numSober = round(p * len(e)/100)
print('\n', p, 'percent of respondents used less than that')
print('That is', numSober, 'respondents')

odd = (numSober - numPoor) / numPoor

print('Among the households using less than',medPoor,'kWh last month,')
print('For one who declares lacking electricity,', odd, 'declare having enough')