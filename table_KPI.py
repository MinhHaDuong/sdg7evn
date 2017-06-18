# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

from VHLSS_importer import survey, pd, np

survey['elec_use'] = pd.cut(survey.kwh_last_month, [-100, 30, 3000])
survey['income_share'] = pd.cut(survey.elec_year / survey.inc, [0, 0.06, 1])


def row(column, complement=False, df=survey):
    xtable = pd.crosstab(df[column], df.year, normalize='columns')
    kpi = 100 * xtable.ix[0]
    if complement:
        kpi = 100 - kpi
    if kpi[2008] == 0:
        kpi[2008] = np.NaN
    fmt_string = '\t{:.1f}%\t{:.1f}%\t{:.1f}%\t{:.1f}%'
    return fmt_string.format(kpi[2008], kpi[2010], kpi[2012], kpi[2014])


print('                       Year\t2008\t2010\t2010\t2014')
print('Share of households')
print('No grid lighting, Rural', row('main_light', True, survey[survey.urb_rur == 'Rural']))
print('No grid lighting, Urban', row('main_light', True, survey[survey.urb_rur == 'Urban']))
print('Use does not meet needs', row('elec_poor'))
print('Use < 30 kWh / month   ', row('elec_use'))
print('Bill > 6% income       ', row('income_share', True))
