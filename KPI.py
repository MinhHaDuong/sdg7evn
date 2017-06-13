# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, pd, np


def printout(df, column):
    counts = pd.crosstab(df[column], df.year, margins=True)
    # print(counts, '\n')
    counts = pd.crosstab(df[column], df.year)
    frequencies = 100 * counts / counts.sum()
    print(np.round(frequencies, 1))


df = survey[['year', 'main_light', 'urb_rur']].dropna()
print('-------------------- Lightning power source, Urban ---------------')
printout(df[df.urb_rur == 'Urban'], 'main_light')
print('-------------------- Lightning power source, Rural ---------------')
printout(df[df.urb_rur == 'Rural'], 'main_light')

print()
print('-------------------- Needs not satisfied ---------------')
df = survey[['year', 'elec_poor']].dropna()
printout(df, 'elec_poor')

print()
print('-------------------- Low power use ---------------')
df = survey[['year', 'kwh_last_month']].dropna()
bins = [-100, 30, 3000]
df['elec_use'] = pd.cut(df.kwh_last_month, bins)
printout(df, 'elec_use')

print()
print('-------------------- Income share ---------------')
df = survey[['year', 'inc', 'elec_year']].dropna()
df['income_share'] = df.elec_year / df.inc
bins = [0, 0.06, 1]
df.income_share = pd.cut(df.income_share, bins)
printout(df, 'income_share')
