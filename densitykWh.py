# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, plt

print("""Answers to VHLSS 2010/2012/2014 survey
Electricity used last month
""")


def subfig(yr):
    s1 = survey.loc[(survey.year == yr) & survey.lacking, 'kwh_last_month']
    s2 = survey.loc[(survey.year == yr) & ~survey.lacking, 'kwh_last_month']
    s1.plot.kde()
    s2.plot.kde()


fig = plt.figure(figsize=(5, 12))

ax = fig.add_subplot(311)
subfig(2010)
ax.set_title('2010')
ax.set_xlim([-10, 1000])
ax.legend(["Lacking", "Not lacking"], loc="upper right")

bx = fig.add_subplot(312)
subfig(2012)
bx.set_title('2012')
bx.set_xlim([-10, 1000])

cx = fig.add_subplot(313)
subfig(2014)
cx.set_title('2014')
cx.set_xlabel('kWh')
cx.set_xlim([-10, 1000])

plt.savefig('densitykWh.png')
