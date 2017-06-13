# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, plt, pd

# sudo pip3 install statsmodels
from statsmodels.graphics.mosaicplot import mosaic

print("""Answers to VHLSS 2010/2012/2014 surveys
Cross tabulation of
Q12. Has consumption of electricity [....]
been sufficient to meet needs over the last 30 days?
""")

categoricalColumns = survey.select_dtypes(include=['category'])


fig = plt.figure(figsize=(15, 50))

# en_subsidy is a binned integer
cols = categoricalColumns.drop(['elec_poor', 'en_subsidy'], axis=1)

# NO GRID PRESENCE QUESTION IN 2014 ??

def label(key):
    return ""

def prop(key):
    if ('Lacking' in key):
        color = 'red'
    if ('Enough' in key):
        color = 'green'
    if ('Plenty' in key):
        color = 'blue'
    return {'color': color}

for i in range(len(cols.columns)):
    column = cols.columns[i]
    print(column)
    df = survey.loc[:, ['elec_poor', column]]
    df.elec_poor = df.elec_poor.cat.remove_categories(['Missing', 'Idk'])
    if (column == 'grid_presence'):
        df.loc[:, column] = df.loc[:, column].cat.remove_categories('Missing')
    df = df.dropna()
    f = plt.figure(figsize=(15, 5))
    if not all(df.loc[survey.year == 2010, column].isnull()):
        ax = f.add_subplot(131)
        mosaic(df[survey.year == 2010], [column, 'elec_poor'], ax, gap=0.02, labelizer=label, properties=prop, title=column+" 2010")
    ax = f.add_subplot(132)
    mosaic(df[survey.year == 2012], [column, 'elec_poor'], ax, gap=0.02, labelizer=label, properties=prop, title=column+" 2012")
    ax = f.add_subplot(133)
    if not all(df.loc[survey.year == 2014, column].isnull()):
        mosaic(df[survey.year == 2014], [column, 'elec_poor'], ax, gap=0.02, labelizer=label, properties=prop, title=column+" 2014")
    plt.savefig('mosaics_' + str(i) + '_' + column + '.png')
    plt.close(f)
