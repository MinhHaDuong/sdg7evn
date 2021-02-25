# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#

from VHLSS_importer import survey

# %%

# Subsampling to Q12 respondents does not change much the
# percentages for off_grid, low_use, high_cost

data = survey[(survey.year == 2014) & survey.elec_poor.notnull()]


def num_poors(column, definition):
    answers = data.loc[:, column].count()
    poors = data.loc[definition, column].count()
    return "\t{:4.1f}% \t{:4d} \t{:d}".format(100 * poors / answers, poors, answers)


print("Energy poverty criteria in 2014, Vietnam Households having answered Q12")
print()
print("Criteria                               \tShare\tMatches\tAnswers")

print(
    "Did not use main grid for lighting     " + num_poors("main_light", survey.off_grid)
)
print(
    "Used less than 30 kWh last month       "
    + num_poors("kwh_last_month", survey.low_use)
)
print("Electricity expenses > 6% income       " + num_poors("effort", survey.high_cost))
print("Low income High cost                   " + num_poors("effort", survey.LIHC))
print(
    "Electricity did not meet needs         " + num_poors("elec_poor", survey.lacking)
)
print(
    "Received electricity subsidy           "
    + num_poors("en_subsidy", survey.subsidized)
)
