# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

""" Mosaic plots of 'Electricity sufficiency' vs. categorical variables in VHLSS

Answers to VHLSS 2010/2012/2014 surveys
Cross tabulation of
Q12. Has consumption of electricity [....] been sufficient to meet needs over the last 30 days?
on categorical variables.
"""

from VHLSS_importer import survey, plt

# sudo pip3 install statsmodels
from statsmodels.graphics.mosaicplot import mosaic


categoricalColumns = survey.select_dtypes(include=['category'])
cols = categoricalColumns.drop(['elec_poor', 'en_subsidy'], axis=1)  # en_subsidy is binned integer
num_cols = len(cols.columns)

# NO GRID PRESENCE QUESTION IN 2014 ??

survey["Q12"] = survey.elec_poor.cat.remove_categories(['Missing', 'Idk'])

survey.loc[:, 'grid_presence'] = survey.grid_presence.cat.remove_categories('Missing')


def label(key):
    return ""


def prop(key):
    color = 'black'   # Should never happen
    if ('Lacking' in key):
        color = 'red'
    if ('Enough' in key):
        color = 'green'
    if ('Plenty' in key):
        color = 'blue'
    return {'color': color}


def sub_mosaic(position, year, column):
    ax = fig.add_subplot(num_cols, 3, position)
    if not all(survey.loc[survey.year == year, column].isnull()):
       mosaic(survey[survey.year == year], [column, 'Q12'],
               ax, gap=0.02, labelizer=label, properties=prop,
               title=column + " " + str(year))


fig = plt.figure(figsize=(15, 50))

for i in range(num_cols):
    column = cols.columns[i]
    sub_mosaic(3 * i + 1, 2010, column)
    sub_mosaic(3 * i + 2, 2012, column)
    sub_mosaic(3 * i + 3, 2014, column)

plt.savefig('mosaics.png')
