# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, np, pd


def printout(column):
    counts = pd.crosstab(survey[column], survey.year, margins=True)
    print(counts, '\n')
    # normalize='column' only available in Pandas 18.1
    frequencies = 100 * counts / counts.ix["All"]
    print(np.round(frequencies, 1))


#%%

print("""
--------------------------- Power meets needs ---------------
Answers to VHLSS 2010/2012/2014 surveys
Q12. Has consumption of electricity [....] been sufficient to meet needs over the last 30 days?
(translation from form Muc08_1Bnew in the 2010 wave)
""")

survey["Q12"] = survey.elec_poor.cat.remove_categories(['Missing', 'Idk']).dropna()
printout('Q12')

#%%

print("""
-------------------- Lightning power source ---------------
There may be some ambiguity in what "Local" means
The answers categories may have changed across surveys
""")

printout('main_light')


#%%

print("""
-------------------- Power use last month by tariff block ---------------
""")
blocks = [-1000, -0.001, 0, 0.001, 30, 50, 100, 150, 200, 300, 400, 3000, 30000]
survey["elec_use"] = pd.cut(survey.kwh_last_month, blocks)
printout('elec_use')
