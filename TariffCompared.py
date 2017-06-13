# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# Created on Thu Sep 22 13:50:53 2016
#

from VHLSS_importer import np, plt, survey
from VHLSS_importer import block_limits, block_prices_2013, block_prices_alt

block_sizes = np.diff(block_limits)

#%%


#df = survey[['year', 'kwh_last_month']]
household_use = survey[survey.year == 2014].kwh_last_month.dropna()


def plot_block_tariff(ax, col, block_prices):
    ax.step(block_limits, block_prices, color=col)
    ax.set_ylim([0, 3550])
    ax.set_xlabel('kWh / month')
    ax.set_ylabel('VND')
    ax.set_title('Block tariff (= marginal price)')


def plot_total_bill(ax, col, block_prices):
    block_costs = block_sizes * block_prices[1:]
    total_bills = np.cumsum(np.insert(block_costs, 0, 0))
    ax.plot(block_limits, total_bills / 1000, color=col)
    ax.set_ylim([0, 1600])
    ax.set_xlabel('kWh / month')
    ax.set_ylabel('kVND')
    ax.set_title('Monthly bill (= total price)')


#%%

fig = plt.figure(figsize=(5, 8))

top_panel = fig.add_subplot(3, 1, 1)
plot_block_tariff(top_panel, 'red', block_prices_2013)
plot_block_tariff(top_panel, 'blue', block_prices_alt)
top_panel.legend(['EVN 2013', 'More progessive'], loc=4)

bottom_panel = fig.add_subplot(3, 1, 2, sharex=top_panel)
plot_total_bill(bottom_panel, 'red', block_prices_2013)
plot_total_bill(bottom_panel, 'blue', block_prices_alt)
bottom_panel.legend(['EVN 2013', 'More progessive'], loc=4)

add_panel = fig.add_subplot(3, 1, 3, sharex=top_panel)
survey[survey.year == 2014].hist(column='kwh_last_month',
                                 ax=add_panel,
                                 bins=block_limits,
                                 color='grey')
add_panel.set_title('Number of households per block (N='+
                    str(len(household_use))+
                    ')')

top_panel.set_xticks(block_limits)
top_panel.set_xlim([0, 550])

plt.tight_layout()
fig.suptitle("Vietnam households electricity costs", fontsize=16)
plt.subplots_adjust(top=0.92)

fig.savefig('TariffCompared.png')
fig.savefig('TariffCompared.pdf')
fig.savefig('TariffCompared-300dpi.png', dpi=300)
