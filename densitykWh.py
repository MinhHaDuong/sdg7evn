# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, plt

print("""Answers to VHLSS 2010/2012/2014 surveys
Electricity used last month
""")


def subfig(yr):
    df = survey[['year', 'elec_last_month', 'kwh_last_month', 'elec_poor']]
    df = df[df.year == yr]
    s1 = df.kwh_last_month[survey.elec_poor == 'Lacking']
    s2 = df.kwh_last_month[survey.elec_poor != 'Lacking']
    s1.plot.kde()
    s2.plot.kde()

fig = plt.figure(figsize=(5, 12))

ax = fig.add_subplot(311)
subfig(2010)
ax.set_title('2010')
ax.set_xlim([-10, 1000])

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
