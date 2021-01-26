# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
import pandas as pd

from scipy.stats import chi2_contingency

from VHLSS_importer import survey

print("""Answers to VHLSS 2010/2012/2014 surveys
Cross tabulation of
Q12. Has consumption of electricity [....]
been sufficient to meet needs over the last 30 days?
""")

categoricalColumns = survey.select_dtypes(include=['category'])

survey["grid_presence"].cat.remove_categories('Missing', inplace=True)


def crosstable(column, yr):
    print('---------------------------------------------------------')
    print(column, yr)
    try:
        print('\nContingency table:')
        table = pd.crosstab(survey.Q12[survey.year == yr], survey.loc[survey.year == yr, column],
                            margins=True)
        print(table)
        print('\nProportions (%)')
        print(100 * table / table.ix["All"])
        print('\nIndependance ?')
        chi2, p, dof, ex = chi2_contingency(table.drop('All').drop('All', 1))
        print('Chi2 =', chi2)
        print('p-value =', p)
        print('degrees of freedom =', dof)
#    print('Expected proportions =\n', ex)
#    print('\n')
    except ValueError:
        print('ValueError: No data I presume.')
    finally:
        print()
#%%


for column in categoricalColumns.drop(['elec_poor', 'Q12', 'en_subsidy', 'block'], axis=1):
    crosstable(column, 2008)
    crosstable(column, 2010)
    crosstable(column, 2012)
    crosstable(column, 2014)
    print('\n')

print('''
**********************
***   Non users    ***
**********************

=========================================================
Column True is respondents who declared using 0 kWh last month
Column False is NA or respondents who declared using >0 kWh last month
''')
for column in categoricalColumns.drop(['elec_poor', 'en_subsidy'], axis=1):
    print('')
    print(pd.crosstab(survey.loc[:, column], [survey.kwh_last_month == 0],
                      margins=True))


print('''
=========================================================
Column True is respondents who declared paying 0 VND last month
Column False is NA or respondents who declared using >0 kWh last month
''')
for column in categoricalColumns.drop(['elec_poor', 'en_subsidy'], axis=1):
    print('')
    print(pd.crosstab(survey.loc[:, column], [survey.elec_last_month == 0],
                      margins=True))

print("""
Consistency check:
Rows: True if declared using zero kWh of electricity, false if non-zero, including NA
Cols: True if declared paying zero VND for electricity, false if non-zero, including NA

Bottom left cell used no electricity but still paid something
Top right cell used electricity without paying.
Comment: IRL there is a subsidy program. And there are free riders on the neighbor's connection
""")
print(pd.crosstab([survey.kwh_last_month == 0], [survey.elec_last_month == 0],
                  margins=False))
