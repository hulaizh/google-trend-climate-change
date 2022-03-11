# -*- coding: utf-8 -*-
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import calendar
from time import sleep
from tqdm import tqdm

# get the topic code for climate change
pytrend = TrendReq(hl='en-US', tz=360)
keywords = pytrend.suggestions(keyword='Climate Change')
df = pd.DataFrame(keywords)
df

# topic for climate change
kw_lists = [r"/m/0d063v"]

# months
end_year = 2021
timeframelist = []
for year in range(2004,end_year+1):
    for month in range(1,13):
        lastday = calendar.monthrange(year,month)[1]
        beg = datetime(year,month,1).strftime("%Y-%m-%d")
        end = datetime(year,month,lastday).strftime("%Y-%m-%d")
        timeframelist.append("{0} {1}".format(beg,end))

# download google trends by country, by month
dflist = []
for timeframe in tqdm(timeframelist):
    pytrend.build_payload(kw_list=[kw_lists[0]],timeframe=timeframe,geo="",gprop="")
    tmpdf = pytrend.interest_by_region()
    tmpdf.columns = [timeframe[:4]+timeframe[5:7]]
    dflist.append(tmpdf)
    sleep(3)
df = pd.concat(dflist,axis=1)

# download google trends by month, over 27 countries
# SVI scaled each country
geo = ['AT','AU','BE','CA','CL','CN','DE','DK','EG','ES','FI','FR','GB','GR','HK','IL','IN','IT','JP','KR','NL','NZ','PL','SE','SG','US','ZA']
dflist = []
for country in geo:
    pytrend.build_payload(kw_list=[kw_lists[0]],timeframe='2004-01-01 2021-12-31',geo=country,gprop="")
    tmpdf = pytrend.interest_over_time()
    tmpdf.drop(columns=['isPartial'], inplace=True)
    tmpdf.rename(columns={'/m/0d063v':country}, inplace=True)
    dflist.append(tmpdf)
    sleep(3)
df_country = pd.concat(dflist,axis=1)

# output
df.reset_index().to_csv("./ClimateChange_m.csv",index=False,encoding='utf8')

df_country.reset_index().to_csv("./ClimateChangeCountry_m.csv",index=False,encoding='utf8')
