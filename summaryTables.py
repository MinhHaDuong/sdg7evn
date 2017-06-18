# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, np, pd


def printout(column):
    counts = pd.crosstab(survey[column], survey.year, margins=True)
    print(counts, '\n')
    print("%")
    counts = pd.crosstab(survey[column], survey.year, margins=True, normalize='columns')
    print(np.round(100 * counts, 2), '\n')


#%%

print("""
--------------------------- Power meets needs ---------------
Answers to VHLSS 2010/2012/2014 surveys
Q12. Has consumption of electricity [....] been sufficient to meet needs over the last 30 days?
(translation from form Muc08_1Bnew in the 2010 wave)
""")

printout('elec_poor')

#%%

print("""
-------------------- Lightning power source ---------------
There may be some ambiguity in what "Local" means
The answers categories may have changed across surveys
""")

printout('main_light')


#%%

print("""
-------------------- Power use last month by block ---------------
""")
printout('block')
