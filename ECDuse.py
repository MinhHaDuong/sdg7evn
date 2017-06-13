# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# Created on Thu Sep 22 13:50:53 2016
#

from VHLSS_importer import survey, np, plt, curve_style


def cdf(yr):
    d = survey[survey.year == yr].kwh_last_month.dropna()
    sorted = d.sort_values()
    yvals = np.arange(1, len(sorted) + 1) / float(len(sorted))
    plt.step(sorted, yvals, color=curve_style[yr][0], linestyle=curve_style[yr][1])


plt.axis([0, 350, 0, 1])
plt.xlabel('kWh')
plt.ylabel('% respondents used less than X kWh last month')
plt.title('Monthly electricity usage by households in Vietnam')

cdf(2014)
cdf(2012)
cdf(2010)

plt.grid(True)
plt.legend(['2014', '2012', '2010'], loc=4)

plt.savefig('ECDuse.png')
plt.savefig('ECDuse-300dpi.png', dpi=300)
plt.savefig('ECDuse.pdf')
