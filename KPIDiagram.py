# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# sudo pip3 install matplotlib-venn

from VHLSS_importer import survey, pd, plt
from matplotlib_venn import venn3, venn2
from matplotlib import gridspec

#%%

# Subsampling to Q12 respondents does not change much the
# percentages for off_grid, low_use, high_cost

data = survey[(survey.year == 2014) & survey.elec_poor.notnull()]


def num_poors(column, definition):
    answers = data.loc[:, column].count()
    poors = data.loc[definition, column].count()
    return "\t{:.1f}%\t{:d}\t{:d}".format(100 * poors / answers, poors, answers)


print("Energy poverty criteria in 2014, Vietnam Households having answered Q12")
print()
print("Criteria                               \tShare\tMatches\tAnswers")

print("Did not use main grid for lighting     " + num_poors("main_light", survey.off_grid))
print("Used less than 30 kWh last month       " + num_poors("kwh_last_month", survey.low_use))
print("Electricity expenses > 6% income       " + num_poors("effort", survey.high_cost))
print("Low income High cost                   " + num_poors("effort", survey.LIHC))
print("Electricity did not meet needs         " + num_poors("elec_poor", survey.lacking))
print("Received electricity subsidy           " + num_poors("en_subsidy", survey.subsidized))

#%%

english = {'low_use': 'Used <30kWh',
           'lacking': 'Needs not met',
           'high_cost': 'Bill > 6% income',
           'LIHC': 'Low income high cost',
           'subsidized': 'Subsidized'}


def cover_two(col1, col2, axe):
    gb = data.groupby([col1, col2]).size()
    venn2(subsets=(gb[1, 0], gb[0, 1], gb[1, 1]),
          set_labels=([english[col1], english[col2]]), ax=axe)


def cover3(col1, col2, col3, axe):
    gb = data.groupby([col1, col2, col3]).size()
#    print(gb)
    venn3(subsets=(gb[1, 0, 0], gb[0, 1, 0], gb[1, 1, 0], gb[0, 0, 1],
                   gb[1, 0, 1], gb[0, 1, 1], gb[1, 1, 1]),
          set_labels=([english[col1], english[col2], english[col3]]), ax=axe)
    axe.text(-0.6, -0.5, 'All other: ' + str(gb[0, 0, 0]) + ' replies')
    return sum(gb)


fig = plt.figure(figsize=(10, 10))
gs = gridspec.GridSpec(6, 2)

cover_two('subsidized', 'low_use', fig.add_subplot(gs[4, 1]))
cover_two('subsidized', 'lacking', fig.add_subplot(gs[4, 0]))
cover_two('subsidized', 'high_cost', fig.add_subplot(gs[5, 0]))
cover_two('subsidized', 'LIHC', fig.add_subplot(gs[5, 1]))

n = cover3('low_use', 'lacking', 'LIHC', fig.add_subplot(gs[0:4, :]))

fig.suptitle('Energy poverty in Vietnam Households 2014 survey\n(n=' + str(n) + ")", fontsize=18)

fig.savefig('KPIDiagram.png')
