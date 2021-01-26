# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
import matplotlib.pyplot as plt

from VHLSS_importer import survey

print("""Answers to VHLSS 2010/2012/2014 surveys
Cross plot of
Q12. Has consumption of electricity [....]
been sufficient to meet needs over the last 30 days?
""")

# Plots discussion
# http://www.exegetic.biz/blog/2013/05/introducing-r-plottin-categorical-variables/
# http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/DataPresentation/DataPresentation7.html


numericalColumns = ('elec_last_month', 'kwh_last_month', 'elec_year',
                    'inc', 'inc_ave', 'size', 'edu_max', 'assets', 'sq_m', 'en_coal',
                    'en_briquette', 'en_petro', 'en_kerosene', 'en_mazut', 'en_diesel',
                    'en_lpg', 'en_natural_gas', 'en_fire_wood', 'en_agr_waste', 'en_other')

assert set(numericalColumns) <= set(survey.select_dtypes(include=['float32', 'float64']).columns)

categories = ['Lacking', 'Enough', 'Plenty']  # We drop 'Idk' and 'Missing'

fig = plt.figure(figsize=(15, 50))

for i, column in enumerate(numericalColumns):
    for j, yr in enumerate((2010, 2012, 2014)):
        ax = fig.add_subplot(len(numericalColumns), 3, i * 3 + j + 1)
        ax.set_title(column + " " + str(yr), x=0.2, y=0.8, fontsize=8)
        data = [survey.loc[(survey.elec_poor == c) & (survey.year == yr), column].dropna()
                for c in categories]
        plt.boxplot(data, labels=categories, showfliers=False, whis=[5, 95], showmeans=True)

plt.savefig('boxGrid.png')
