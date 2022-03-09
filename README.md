# google-trend-climate-change

This code is to download Google trends of "Climate Change" by country.

Before running the code, install the `pytrends` package: `pip install pytrends`.

The code returns scaled Google search volume index $\hat{G}_{c,t}$ for all countries every month. Let $G_{c,t}$ be the unscaled search volume, $\hat{G}_{c,t}$ equals to $G_{c,t}/\eta_{t}$, where $\eta_{t}$ is the month specific adjustment factor. $\hat{G}_{c,t}$ is scaled from 0 to 100.