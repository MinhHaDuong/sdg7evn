# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, np, plt

print("""Answers to VHLSS 2010/2012/2014 surveys
Electricity used last month vs. Income
""")


def subfig(yr, n):
    ax = fig.add_subplot(3, 1, n)
    df = survey[['year', 'kwh_last_month', 'inc']].dropna()
    df = df[df.year == yr]
    plt.hexbin(df.inc/1000, df.kwh_last_month,
               bins='log', cmap='Greys',
               gridsize=500
               )
    ax.set_title(str(yr), x=0.85, y=0.8)
    ax.set_ylabel('kWh')
    ax.set_ylim([0, 400])
    ax.set_xlim([0, 400])
    x = np.arange(200)
    slope, intercept = np.polyfit(df.inc[df.inc < 200000], df.kwh_last_month[df.inc < 200000], 1)
    ax.plot(x, intercept + slope * x*1000, color='red')
    regressionText = "kWh = " + str(round(intercept)) + ' + ' + str(round(slope*1000, 2)) + ' * income'
    ax.text(205, intercept + slope * 200000, regressionText, color='red')
    print('----------------------')
    print(yr)
    print('Electricity use in kWh per month = ', round(intercept, 2), '+ ', round(slope*1000, 2), '* annual income in M VND')
    return ax


fig = plt.figure(figsize=(6, 12))
fig.suptitle("Monthly electricity use as a function of annual income\nfor households in Vietnam", fontsize=14)

subfig(2010, 1)

subfig(2012, 2)

subfig(2014, 3).set_xlabel('Annual income, M VND')


plt.savefig('kWhbyIncome.png')
