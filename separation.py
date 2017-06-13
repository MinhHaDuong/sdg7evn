# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, plt

print("""Answers to VHLSS 2010/2012/2014 surveys
Multidimentional plot on what is energy poverty:
Electricity bill last month / income last month
Household size
""")


def subfig(yr):
    df = survey[['year', 'elec_last_month', 'inc', 'size', 'elec_poor']]
    df = df[df.year == yr]
    x = df.elec_last_month[df.elec_poor != 'Lacking'] / df.inc[df.elec_poor != 'Lacking']
    y = df.loc[df.elec_poor != 'Lacking', 'size']
    plt.scatter(x, y)
    x = df.elec_last_month[df.elec_poor == 'Lacking'] / df.inc[df.elec_poor == 'Lacking']
    y = df.loc[df.elec_poor == 'Lacking', 'size']
    plt.scatter(x, y, color='red', alpha=0.3)


fig = plt.figure(figsize=(6, 12))

ax = fig.add_subplot(311)
subfig(2010)
ax.set_title('2010')
ax.set_xlim([0, 0.10])
ax.set_ylim([1, 16])

ax = fig.add_subplot(312)
subfig(2012)
ax.set_title('2012')
ax.set_xlim([0, 0.10])
ax.set_ylim([1, 16])

ax = fig.add_subplot(313)
subfig(2014)
ax.set_title('2014')
ax.set_ylabel('Household size')
ax.set_xlabel('Electricity expense / income ratio')
ax.set_xlim([0, 0.10])
ax.set_ylim([1, 16])

plt.savefig('separation.png')
plt.close(fig)

#%%
from pandas.tools.plotting import radviz
fig = plt.figure(figsize=(10, 10))

df = survey[[ 'elec_last_month', 'inc', 'size', 'elec_poor', 'sq_m']]
df.elec_poor = df.elec_poor.cat.remove_categories(['Missing', 'Idk', 'Plenty'])
df = df[survey.year == 2014].dropna()
radviz(df, 'elec_poor')
plt.show(fig)
plt.close(fig)
