Title: How to write an R Data Frame to an SQL Table
Date: 2015-07-08 20:45
Authors: Michael Toth
Modified: 2015-07-08 20:45 
Category: R
Tags: R, SQL
Slug: how-to-write-an-r-data-frame-to-an-sql-table
author_gplusid: 103836786232018210272
Summary: A brief tutorial on how you can create SQL tables directly from R to make querying based on a list of IDs a simpler process 

Frequently I find I need to perform an analysis that requires querying some values in a database table based on a series of IDs that might vary depending on some input. As an example, assume we have the following:

* A table that contains historical stock prices for 2000 stocks for the last 30 years
* Some input that contain's a user's portfolio of stock tickers  

Often, we'll want to pull the price history over a certain date range for all stocks in the user's portfolio. We could of course query all values in the stock prices table and then subset, but this is incredibly inefficient and also means we can't make use of any SQL aggregation functions in our query. Something I've done before when working in an SQL IDE is to create a temp table where I insert a list of the IDs that I am trying to look up, and then join on that table for my query. This is an ideal solution when we're talking about looking up more than a few securities. It took me a while to find an easy way to do this directly in R, but it turns out to be quite simple. I'm hoping my solution helps anybody else who might have this same issue.  
<br>

#### Assumptions:
* A table called *stock_prices* that contains stock price history
* A data frame called *tickers* that contains a list of stock tickers (column name = ticker)
* Here I am using PostgreSQL, but this should work essentially the same for any SQL variant  
<br>

#### Code

Start by setting up the connection:

```R
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, user='user', password='password', dbname='my_database', host='host')
```
<br>

Next create the temp table and insert values from our data frame. The key here is the dbWriteTable function which allows us to write an R data frame directly to a database table. The data frame's column names will be used as the database table's fields

```R
# Drop table if it already exists
if (dbExistsTable(con, "temp_tickers"))
    dbRemoveTable(con, "temp_tickers")

# Write the data frame to the database
dbWriteTable(con, name = "temp_tickers", value = tickers, row.names = FALSE)
```
<br>

Finally, join the stock prices table to the table we just created and query the subsetted values

```R
sql <- " 
    select sp.ticker, sp.date, sp.price
    from stock_prices sp
    join temp_tickers tt on sp.ticker = tt.ticker
    where date between '2000-01-01' and '2015-07-08'
"

results <- dbGetQuery(con, sql)

# Free up resources
dbDisconnect(con)
dbUnloadDriver(drv)
```
<br>

And that's it. It turned out to not be very complicated, and many may already know this, but it took me a while to figure out how this should be done. I spent a lot of time messing around with INSERT statements before scrapping that idea and coming up with this solution. Let me know if you find this helpful or if you have any ideas on how to do this better!
