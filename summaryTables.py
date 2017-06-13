# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, np, pd


def printout(df, column):
    counts = pd.crosstab(df[column], df.year, margins=True)
    print(counts, '\n')
    # normalize='column' only available in Pandas 18.1
    frequencies = 100 * counts / counts.ix["All"]
    print(np.round(frequencies, 1))


print("""
--------------------------- Power meets needs ---------------
Answers to VHLSS 2010/2012/2014 surveys
Q12. Has consumption of electricity [....]
been sufficient to meet needs over the last 30 days?
(translation from form Muc08_1Bnew in the 2010 wave)
""")

df = survey[['year', 'elec_poor']]
df.elec_poor = df.elec_poor.cat.remove_categories(['Missing', 'Idk'])
df = df.dropna()
printout(df, 'elec_poor')

print("""
-------------------- Lightning power source ---------------
There may be some ambiguity in what "Local" means
The answers categories may have changed across surveys
""")
df = survey[['year', 'main_light']].dropna()
printout(df, 'main_light')

print("""
-------------------- Low power use ---------------
""")
df = survey[['year', 'kwh_last_month']].dropna()
bins = [-1000, -0.001, 0, 0.001, 25, 50, 100, 150, 3000, 30000]
df['elec_use'] = pd.cut(df.kwh_last_month, bins)

printout(df, 'elec_use')