# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# sudo pip3 install matplotlib-venn

from VHLSS_importer import survey, pd, plt
from matplotlib_venn import venn3, venn2
from matplotlib import gridspec

#%%


d = pd.DataFrame(
    {'grid': survey[survey.year == 2014].main_light.dropna() == 'Main_Grid',
     'lacking': survey[survey.year == 2014].elec_poor.dropna() == 'Lacking',
     'low_kwh': survey[survey.year == 2014].kwh_last_month.dropna() <= 30,
     'big_effort': survey[survey.year == 2014].elec_year.dropna() / survey.inc.dropna() > 0.06,
     'subsidized': survey[survey.year == 2014].en_subsidy.dropna() > 0}
     )

print('Year 2014')
print('=========')
print('Respondents not using the main grid for lighting')
off_grid = d[d.grid == False].astype(str)
print('N =', len(off_grid))
print(off_grid.groupby(['low_kwh']).size())
print(off_grid.groupby(['low_kwh', 'lacking']).size())

print()
print('Respondents using the main grid for lighting')

on_grid = d[d.grid == True].astype(str)
print('N=', len(on_grid))
print(on_grid.groupby(['low_kwh']).size())
print(on_grid.groupby(['low_kwh', 'lacking']).size())
print(on_grid.groupby(['low_kwh', 'lacking', 'big_effort']).size())
print(on_grid.groupby(['low_kwh', 'lacking', 'big_effort', 'subsidized']).size())

print()
print('Respondents using the main grid for lighting, dropping NaN')

on_grid = d[d.grid == True]
print('N=', len(on_grid))
print(on_grid.groupby(['low_kwh']).size())
print(on_grid.groupby(['low_kwh', 'lacking']).size())
print(on_grid.groupby(['low_kwh', 'lacking', 'big_effort']).size())
print(on_grid.groupby(['low_kwh', 'lacking', 'big_effort', 'subsidized']).size())


english = {'low_kwh': 'Used <30kWh',
           'lacking': 'Needs not met',
           'big_effort': 'Bill > 6% income',
           'subsidized': 'Subsidized'}

def cover2(col1, col2, axe):
    gb = d[d.grid == True].groupby([col1, col2]).size()
    venn2(subsets = (gb[1,0], gb[0,1], gb[1,1]), set_labels=([english[col1], english[col2]]), ax=axe)

def cover3(col1, col2, col3, axe):
    gb = d[d.grid == True].groupby([col1, col2, col3]).size()
    print(gb)
    venn3(subsets = (gb[1,0,0], gb[0,1,0], gb[1,1,0], gb[0,0,1], gb[1,0,1], gb[0,1,1], gb[1,1,1]),
          set_labels=([english[col1], english[col2], english[col3]]), ax=axe)
    axe.text(-0.6, -0.5, 'All other: '+str(gb[0,0,0])+' replies')
    return sum(gb)


fig = plt.figure(figsize=(10, 10))
gs = gridspec.GridSpec(4,3)


cover2('subsidized', 'lacking', fig.add_subplot(gs[3,0]))
cover2('subsidized', 'big_effort', fig.add_subplot(gs[3,1]))
cover2('subsidized', 'low_kwh', fig.add_subplot(gs[3,2]))

n = cover3('low_kwh', 'lacking', 'big_effort', fig.add_subplot(gs[0:3,:]))

fig.suptitle('The energy poverty criteria are not correlated\nVietnam 2014 survey, N='+str(n)+" households", fontsize=18)

fig.savefig('KPIDiagram.png')