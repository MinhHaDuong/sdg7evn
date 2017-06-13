# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#

from VHLSS_importer import survey
import matplotlib.pyplot as plt


def subfig(yr, n):
    ax = fig.add_subplot(3, 1, n)
    df = survey[['year', 'elec_last_month', 'kwh_last_month', 'elec_poor']]
    df = df[df.year == yr]
    plt.hexbin(df.kwh_last_month[df.elec_poor != 'Lacking'],
               df.elec_last_month[df.elec_poor != 'Lacking'],
               bins='log', cmap='Blues',
               gridsize=200)
    plt.hexbin(df.kwh_last_month[df.elec_poor == 'Lacking'],
               df.elec_last_month[df.elec_poor == 'Lacking'],
               bins='log', cmap='Reds', alpha=0.5,
               gridsize=200)
    ax.set_title(str(yr), x=0.85, y=0.8)
    ax.set_ylabel('Elec. expense last month (kVND)')
    ax.set_xlim([0, 400])
    ax.set_ylim([0, 600])
    return ax


fig = plt.figure(figsize=(6, 12))
fig.suptitle("Electricity usage, expense and satisfaction of needs\nRed: Vietnam households with unsatisfied needs\nBlue: satisfied or NA", fontsize=12)

subfig(2010, 1)

subfig(2012, 2)

subfig(2014, 3).set_xlabel('Electricity usage last month (kWh)')

plt.savefig('electricityBills.png')