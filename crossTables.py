# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, pd
from scipy.stats import chi2_contingency

print("""Answers to VHLSS 2010/2012/2014 surveys
Cross tabulation of
Q12. Has consumption of electricity [....]
been sufficient to meet needs over the last 30 days?
""")

categoricalColumns = survey.select_dtypes(include=['category'])

# en_subsidy is a binned integer


def crosstable(column, yr):
    print('---------------------------------------------------------')
    print(column, yr)
    df = survey.loc[survey.year == yr, ['elec_poor', column]]
    df.elec_poor = df.elec_poor.cat.remove_categories(['Missing', 'Idk'])
    if (column == 'grid_presence'):
        df.loc[:, column] = df.loc[:, column].cat.remove_categories('Missing')
    df = df.dropna()
    if all(df.loc[:, column].isnull()):
        print('No data')
        return
    print('\nContingency table:')
    table = pd.crosstab(df.elec_poor, df.loc[:, column], margins=True)
    print(table)
    print('\nProportions')
    print(table / table.ix["All"])
    print('\nIndependance ?')
    chi2, p, dof, ex = chi2_contingency(table.drop('All').drop('All', 1))
    print('Chi2 =', chi2)
    print('p-value =', p)
    print('degrees of freedom =', dof)
#    print('Expected proportions =\n', ex)
#    print('\n')
#   tableNoMargin.transpose().plot(kind='bar', figsize=(8, 8), stacked=True)


for column in categoricalColumns.drop(['elec_poor', 'en_subsidy'], axis=1):
    crosstable(column, 2008)
    crosstable(column, 2010)
    crosstable(column, 2012)
    crosstable(column, 2014)
    print('\n')

print('Column True is respondents who declared using 0 kWh last month')
print('Column False is NA or respondents who declared using >0 kWh last month')
for column in categoricalColumns.drop(['elec_poor', 'en_subsidy'], axis=1):
    print('\n')
    print(pd.crosstab(survey.loc[:, column], [survey.kwh_last_month == 0],
                      margins=True))


print('\n\n')
print('Column True is respondents who declared paying 0 VND last month')
print('Column False is NA or respondents who declared using >0 kWh last month')
for column in categoricalColumns.drop(['elec_poor', 'en_subsidy'], axis=1):
    print('\n')
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
