---
title: Federal Reserve Recession Predictions are Worse than Using the Long-Run Average
author: Michael Toth
date: 2017-06-09
category: R
tags: R, Politics, Donald Trump
summary: A visualization of historical Presidential approval ratings from Harry Truman through Donald Trump
output: html_document
status: draft
---







I was reading an article recently that referred to the Federal Reserve's Recession Probability Indicator, which I'd never heard of before. I was intrigued enough to look into it, and it turns out it's a monthly statistic [published on the New York Fed's website](https://www.newyorkfed.org/research/capital_markets/ycfaq.html) that aims to predict the probability that the economy will be in a recession 12 months in the future. 

The first thing I noticed was that as of April 30, 2017, they were predicting the probability of recession in 12 months to be 6.3%. To me, this number seemed low, so I decided to look at their raw data and make some calculations. First, I looked at the long-run average, and I found that since 1960, the U.S. has been in a recession 13.5% of the time. This was enough to convince me a deeper analysis of these predictions was warranted. First though, let's take a look at what I'm talking about. Graphically, the prediction statistic looks like this:

![center](/figures/fed_recession_probability/forecast_graph-1.png)

The x-axis represents the date, covering monthly periods from 1960 through April 2017. The y-axis shows the predicted probability of recession. I've also added vertical bars that show the time periods classified as recessions by the [National Bureau of Economic Research](http://www.nber.org/), which was the measure this statistic was built to predict. 

A quick visual inspection identifies several issues with the predictions. In the highlighted period, there are a total of 8 identified recessions. Of these, 4 of them occurred when the stated probability of recession was quite low:

* The 1960-1961 recession was preceded by probabilities of approximately 10%
* The 1974 recession was preceded by probabilities of approximately 2% - 5%
* The 1981 recession was preceded by probabilities of approximately 5%. This is one of the stranger ones--In March 1981, the probability of recession was forecasted at 94%, but by June this number had fallen to just under 2%. The recession then did hit 2 months later, in July, and lasted over a year. 
* The 2001 recession was preceded by probabilities of 10% - 15%

In all of these cases, the prediction statistic does increase once the recession has begun, but that's of no use as a forecasting tool. It's certainly troubling that this method was seemingly unable to identify four of the eight recessions in this period, but it's important to note that that's not technically what they're testing for here. What's really important is that their probabilities match reality. That is, if they predict a recession will occur with 10% probability, they're not necessarily incorrect when a recession does occur. In fact, with a good prediction model we should expect such a result 10% of the time. 

So now let's get into this. When the Federal Reserve predicts there is an n% chance of a recession, how often does a recession actually occur 12 months later? Under a perfect model, we'd expect recessions to occur exactly n% of the time.

![center](/figures/fed_recession_probability/core-analysis-1.png)

For this graph I've grouped the Fed Predictions into 8 separate bands by quantile, each containing approximately the same number of predictions (78 at the lowest, 86 at the greatest). For each of these bands, I've calculated the average prediction by the Fed and the actual historical probability associated with those predictions, and I've added it to the plot.


```
## [1] 0.1117896
```

```
## [1] 0.1098789
```

To their credit, I don't believe the Fed is deliberately trying to mislead here. In fact, they have a detailed Q&A section on this page that details this methodology, its shortcomings, and further findings. But that's not sufficient. The real problem here is the insidious side effects that come from this type of forecast. Academics with no skin in the game make forecasts about the macroeconomy. The forecasts are published by the Federal Reserve, and they bring with them the authority of that organization. Then retail (and in many cases institutional) investors make real-money investments based on these forecasts, and they are the ones who suffer the consequences of the poor forecasting. The academics who make the forecasts are never held accountable for their poor forecasting ability, and the forecasts are treated as if they are the 

People who do not have skin in the game should not make forecasts. It is well established that forecasts in the economic sphere are of essentially 0 utility.
