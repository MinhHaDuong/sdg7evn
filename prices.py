# Reading the VHLSS 2010/2012/2014 survey data into a Python Pandas dataframe
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
from VHLSS_importer import electricity_tariffs, CPI, plt


fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(111)

electricity_tariffs.plot(ax=ax)
ax.set_ylabel('VND per kWh')
ax.set_ylim([0, 3000])
ax.set_title('CPI & Price of electricity blocks for households in Vietnam')

(5*CPI).plot(ax=ax, linewidth=3.0)

plt.savefig('prices.png')

# https://www.vietcombank.com.vn/exchangerates/
# Accessed 2016-09-28
# VNDperUSD = 22265
#
# ax2 = ax.twinx()
# ax2.set_ylim([0, 3000/VNDperUSD])
# ax2.set_ylabel('US cents  per kWh')
