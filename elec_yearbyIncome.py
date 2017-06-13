# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# The data summary is shown in "incomeShare.py"
#

from VHLSS_importer import survey, np, plt


print("""Answers to VHLSS 2008/2010/2012/2014 surveys
Multidimentional plot on what is energy poverty:
Electricity spending last year
Income last year
""")


def subfig(yr, n):
    ax = fig.add_subplot(4, 1, n)
    df = survey[['year', 'elec_year', 'inc']].dropna()
    df = df[df.year == yr]
    plt.hexbin(df.inc/1000, df.elec_year/1000,
               bins='log', cmap='Greys',
               gridsize=500
               )
    ax.set_title(str(yr), y=0.8, x=0.85)
    ax.set_ylabel('Annual expense, M VND')
    ax.set_ylim([0, 5])
    ax.set_xlim([0, 400])
#    print('----------------------')
#    print(yr)
    x = np.arange(200)
#    slope, intercept = np.polyfit(df.inc[df.inc < 200000], df.elec_year[df.inc < 200000], 1)
#    ax.plot(x, intercept + slope * x, color='red')
    ax.plot(x, x * 0.1, color='red')
    return ax


fig = plt.figure(figsize=(6, 12))
fig.suptitle("Electricity bill below the 10% income red line\nfor most households in Vietnam", fontsize=14)

subfig(2008, 1)

subfig(2010, 2)

subfig(2012, 3)

subfig(2014, 4).set_xlabel('Annual income, M VND (nominal)')

plt.savefig('elec_yearbyIncome.png')
