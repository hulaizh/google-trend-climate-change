# google-trend-climate-change

This code is to download Google trends of "Climate Change" by country.

Before running the code, install the `pytrends` package: `pip install pytrends`.

The code returns scaled Google search volume index `SVI` for all countries every month. The scaled `SVI` equals to the `unscaled SVI` divided by monthly adjustment factors. Each month, some country will get the highest `SVI` 100 and some country will get the lowest `SVI` 0.