# -*- coding: utf-8 -*-
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import calendar
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
    for month in range(1, 13,3):
        lastday = calendar.monthrange(year,month+2)[1]
        beg = datetime(year,month,1).strftime("%Y-%m-%d")
        end = datetime(year,month+2,lastday).strftime("%Y-%m-%d")
        timeframelist.append("{0} {1}".format(beg,end))

# download google trends by country, over quarter
# SVI scaled each quarter
dflist = []
for timeframe in tqdm(timeframelist):
    pytrend.build_payload(kw_list=[kw_lists[0]],timeframe=timeframe,geo="",gprop="")
    tmpdf = pytrend.interest_by_region()
    tmpdf.columns = [timeframe[:4]+timeframe[5:7]]
    dflist.append(tmpdf)
df = pd.concat(dflist,axis=1)

# output
df.reset_index().to_csv("./ClimateChange_q.csv",index=False,encoding='utf8')

