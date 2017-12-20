---
title: Historical Presidential Approval Ratings
author: Michael Toth
date: 2017-06-09
category: R
tags: R, Politics, Donald Trump
summary: A visualization of historical Presidential approval ratings from Harry Truman through Donald Trump
output: html_document
status: draft
---

Data for this post comes from http://www.presidency.ucsb.edu/data/popularity.php?pres=33&sort=time&direct=DESC&Submit=DISPLAY



```r
library(animation)
```

```
## Warning: package 'animation' was built under R version 3.3.2
```

```r
library(dplyr)
library(gganimate)
library(ggplot2)
library(hrbrthemes)
library(lubridate)
```

```
## 
## Attaching package: 'lubridate'
```

```
## The following object is masked from 'package:base':
## 
##     date
```

```r
# Function to convert 2-digit years
get_year <- function(x, cutoff_year=1944){
  x <- mdy(x)
  m <- year(x) %% 100
  year(x) <- ifelse(m > cutoff_year %% 100, 1900+m, 2000+m)
  x
}

approval <- read.csv('~/dev/michaeltoth/content/_resources/presidentialapproval.csv')
approval$Start <- get_year(approval$Start)
approval$End <- get_year(approval$End)
approval$Quarter <- floor_date(approval$End, unit = 'quarter')
approval <- approval %>% group_by(President) %>% mutate(First = min(End))
approval <- approval %>% mutate(Time = as.numeric(End - First) / 365.25)
```



```r
ggplot(approval) +
  geom_line(aes(x = Time, y = Approval, color = President)) +
  scale_y_continuous(name = 'Approval Rating', limits = c(0, 100)) +
  scale_x_continuous(name = 'Years in Office', limits = c(0, 8), breaks = seq(0, 8, 1)) +
  theme_ipsum(grid='XY')
```

![center](/figures/presidential_approval/graph-1.png)

```r
  #labs(y = 'Approval Rating',
  #     title = 'Presidential Approval Ratings',
  #     caption='michaeltoth.me')
```



```r
presidents <- unique(approval$President)

saveGIF(
{
    for (pres in presidents) {
        current <- filter(approval, President == pres)
        cutoff <- head(current$First, n = 1)
        
        current_quarters <- unique(current$Quarter)
        
        for (quarter in current_quarters) {
            g <- ggplot() +
                geom_line(data = filter(approval, End < cutoff), aes(x = Time, y = Approval, group = President), color = 'grey', alpha = 0.5) +
                geom_line(data = filter(approval, President == pres, End <= quarter), aes(x = Time, y = Approval), color = 'navy') +
                scale_y_continuous(name = 'Approval Rating', limits = c(0, 100)) +
                scale_x_continuous(name = 'Years in Office', limits = c(0, 8), breaks = seq(0, 8, 1)) +
                theme_ipsum(grid='XY') +
                labs(title = 'Presidential Approval Ratings',
                     subtitle = pres,
                     caption = 'Source: michaeltoth.me @michael_toth')
            print(g)
            ani.pause()
            print(paste(pres, as.Date(quarter, origin = '1970-01-01')))
        }
        ani.pause(interval = 1)
    }
}, 
interval = 0.2,
loop = 0,
movie.name = 'pres.gif',
ani.width = 600, 
ani.height = 600
)
```

```
## Warning: Unknown column 'PANEL'

## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1945-04-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## geom_path: Each group consists of only one observation. Do you need to
## adjust the group aesthetic?
```

```
## [1] "Harry S. Truman 1945-07-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1945-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1946-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1946-04-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1946-07-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1946-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1947-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1947-04-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1947-07-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1947-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1948-04-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1949-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1949-04-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1949-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1950-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1950-04-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1950-07-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1950-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1951-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1951-04-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1951-07-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1951-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1952-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1952-04-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1952-07-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Harry S. Truman 1952-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Dwight D. Eisenhower 1953-01-01"
```

```
## [1] "Dwight D. Eisenhower 1953-04-01"
```

```
## [1] "Dwight D. Eisenhower 1953-07-01"
```

```
## [1] "Dwight D. Eisenhower 1953-10-01"
```

```
## [1] "Dwight D. Eisenhower 1954-01-01"
```

```
## [1] "Dwight D. Eisenhower 1954-04-01"
```

```
## [1] "Dwight D. Eisenhower 1954-07-01"
```

```
## [1] "Dwight D. Eisenhower 1954-10-01"
```

```
## [1] "Dwight D. Eisenhower 1955-01-01"
```

```
## [1] "Dwight D. Eisenhower 1955-04-01"
```

```
## [1] "Dwight D. Eisenhower 1955-07-01"
```

```
## [1] "Dwight D. Eisenhower 1955-10-01"
```

```
## [1] "Dwight D. Eisenhower 1956-01-01"
```

```
## [1] "Dwight D. Eisenhower 1956-04-01"
```

```
## [1] "Dwight D. Eisenhower 1956-07-01"
```

```
## [1] "Dwight D. Eisenhower 1956-10-01"
```

```
## [1] "Dwight D. Eisenhower 1957-01-01"
```

```
## [1] "Dwight D. Eisenhower 1957-04-01"
```

```
## [1] "Dwight D. Eisenhower 1957-07-01"
```

```
## [1] "Dwight D. Eisenhower 1957-10-01"
```

```
## [1] "Dwight D. Eisenhower 1958-01-01"
```

```
## [1] "Dwight D. Eisenhower 1958-04-01"
```

```
## [1] "Dwight D. Eisenhower 1958-07-01"
```

```
## [1] "Dwight D. Eisenhower 1958-10-01"
```

```
## [1] "Dwight D. Eisenhower 1959-01-01"
```

```
## [1] "Dwight D. Eisenhower 1959-04-01"
```

```
## [1] "Dwight D. Eisenhower 1959-07-01"
```

```
## [1] "Dwight D. Eisenhower 1959-10-01"
```

```
## [1] "Dwight D. Eisenhower 1960-01-01"
```

```
## [1] "Dwight D. Eisenhower 1960-04-01"
```

```
## [1] "Dwight D. Eisenhower 1960-07-01"
```

```
## [1] "Dwight D. Eisenhower 1960-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "John F. Kennedy 1961-01-01"
```

```
## [1] "John F. Kennedy 1961-04-01"
```

```
## [1] "John F. Kennedy 1961-07-01"
```

```
## [1] "John F. Kennedy 1961-10-01"
```

```
## [1] "John F. Kennedy 1962-01-01"
```

```
## [1] "John F. Kennedy 1962-04-01"
```

```
## [1] "John F. Kennedy 1962-07-01"
```

```
## [1] "John F. Kennedy 1962-10-01"
```

```
## [1] "John F. Kennedy 1963-01-01"
```

```
## [1] "John F. Kennedy 1963-04-01"
```

```
## [1] "John F. Kennedy 1963-07-01"
```

```
## [1] "John F. Kennedy 1963-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Lyndon B. Johnson 1963-10-01"
```

```
## [1] "Lyndon B. Johnson 1964-01-01"
```

```
## [1] "Lyndon B. Johnson 1964-04-01"
```

```
## [1] "Lyndon B. Johnson 1964-10-01"
```

```
## [1] "Lyndon B. Johnson 1965-01-01"
```

```
## [1] "Lyndon B. Johnson 1965-04-01"
```

```
## [1] "Lyndon B. Johnson 1965-07-01"
```

```
## [1] "Lyndon B. Johnson 1965-10-01"
```

```
## [1] "Lyndon B. Johnson 1966-01-01"
```

```
## [1] "Lyndon B. Johnson 1966-04-01"
```

```
## [1] "Lyndon B. Johnson 1966-07-01"
```

```
## [1] "Lyndon B. Johnson 1966-10-01"
```

```
## [1] "Lyndon B. Johnson 1967-01-01"
```

```
## [1] "Lyndon B. Johnson 1967-04-01"
```

```
## [1] "Lyndon B. Johnson 1967-07-01"
```

```
## [1] "Lyndon B. Johnson 1967-10-01"
```

```
## [1] "Lyndon B. Johnson 1968-01-01"
```

```
## [1] "Lyndon B. Johnson 1968-04-01"
```

```
## [1] "Lyndon B. Johnson 1968-07-01"
```

```
## [1] "Lyndon B. Johnson 1968-10-01"
```

```
## [1] "Lyndon B. Johnson 1969-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Richard Nixon 1969-01-01"
```

```
## [1] "Richard Nixon 1969-04-01"
```

```
## [1] "Richard Nixon 1969-07-01"
```

```
## [1] "Richard Nixon 1969-10-01"
```

```
## [1] "Richard Nixon 1970-01-01"
```

```
## [1] "Richard Nixon 1970-04-01"
```

```
## [1] "Richard Nixon 1970-07-01"
```

```
## [1] "Richard Nixon 1970-10-01"
```

```
## [1] "Richard Nixon 1971-01-01"
```

```
## [1] "Richard Nixon 1971-04-01"
```

```
## [1] "Richard Nixon 1971-07-01"
```

```
## [1] "Richard Nixon 1971-10-01"
```

```
## [1] "Richard Nixon 1972-01-01"
```

```
## [1] "Richard Nixon 1972-04-01"
```

```
## [1] "Richard Nixon 1972-10-01"
```

```
## [1] "Richard Nixon 1973-01-01"
```

```
## [1] "Richard Nixon 1973-04-01"
```

```
## [1] "Richard Nixon 1973-07-01"
```

```
## [1] "Richard Nixon 1973-10-01"
```

```
## [1] "Richard Nixon 1974-01-01"
```

```
## [1] "Richard Nixon 1974-04-01"
```

```
## [1] "Richard Nixon 1974-07-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Gerald R. Ford 1974-07-01"
```

```
## [1] "Gerald R. Ford 1974-10-01"
```

```
## [1] "Gerald R. Ford 1975-01-01"
```

```
## [1] "Gerald R. Ford 1975-04-01"
```

```
## [1] "Gerald R. Ford 1975-07-01"
```

```
## [1] "Gerald R. Ford 1975-10-01"
```

```
## [1] "Gerald R. Ford 1976-01-01"
```

```
## [1] "Gerald R. Ford 1976-04-01"
```

```
## [1] "Gerald R. Ford 1976-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Jimmy Carter 1977-01-01"
```

```
## [1] "Jimmy Carter 1977-04-01"
```

```
## [1] "Jimmy Carter 1977-07-01"
```

```
## [1] "Jimmy Carter 1977-10-01"
```

```
## [1] "Jimmy Carter 1978-01-01"
```

```
## [1] "Jimmy Carter 1978-04-01"
```

```
## [1] "Jimmy Carter 1978-07-01"
```

```
## [1] "Jimmy Carter 1978-10-01"
```

```
## [1] "Jimmy Carter 1979-01-01"
```

```
## [1] "Jimmy Carter 1979-04-01"
```

```
## [1] "Jimmy Carter 1979-07-01"
```

```
## [1] "Jimmy Carter 1979-10-01"
```

```
## [1] "Jimmy Carter 1980-01-01"
```

```
## [1] "Jimmy Carter 1980-04-01"
```

```
## [1] "Jimmy Carter 1980-07-01"
```

```
## [1] "Jimmy Carter 1980-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Ronald Reagan 1981-01-01"
```

```
## [1] "Ronald Reagan 1981-04-01"
```

```
## [1] "Ronald Reagan 1981-07-01"
```

```
## [1] "Ronald Reagan 1981-10-01"
```

```
## [1] "Ronald Reagan 1982-01-01"
```

```
## [1] "Ronald Reagan 1982-04-01"
```

```
## [1] "Ronald Reagan 1982-07-01"
```

```
## [1] "Ronald Reagan 1982-10-01"
```

```
## [1] "Ronald Reagan 1983-01-01"
```

```
## [1] "Ronald Reagan 1983-04-01"
```

```
## [1] "Ronald Reagan 1983-07-01"
```

```
## [1] "Ronald Reagan 1983-10-01"
```

```
## [1] "Ronald Reagan 1984-01-01"
```

```
## [1] "Ronald Reagan 1984-04-01"
```

```
## [1] "Ronald Reagan 1984-07-01"
```

```
## [1] "Ronald Reagan 1984-10-01"
```

```
## [1] "Ronald Reagan 1985-01-01"
```

```
## [1] "Ronald Reagan 1985-04-01"
```

```
## [1] "Ronald Reagan 1985-07-01"
```

```
## [1] "Ronald Reagan 1985-10-01"
```

```
## [1] "Ronald Reagan 1986-01-01"
```

```
## [1] "Ronald Reagan 1986-04-01"
```

```
## [1] "Ronald Reagan 1986-07-01"
```

```
## [1] "Ronald Reagan 1986-10-01"
```

```
## [1] "Ronald Reagan 1987-01-01"
```

```
## [1] "Ronald Reagan 1987-04-01"
```

```
## [1] "Ronald Reagan 1987-07-01"
```

```
## [1] "Ronald Reagan 1987-10-01"
```

```
## [1] "Ronald Reagan 1988-01-01"
```

```
## [1] "Ronald Reagan 1988-04-01"
```

```
## [1] "Ronald Reagan 1988-07-01"
```

```
## [1] "Ronald Reagan 1988-10-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "George Bush 1989-01-01"
```

```
## [1] "George Bush 1989-04-01"
```

```
## [1] "George Bush 1989-07-01"
```

```
## [1] "George Bush 1989-10-01"
```

```
## [1] "George Bush 1990-01-01"
```

```
## [1] "George Bush 1990-04-01"
```

```
## [1] "George Bush 1990-07-01"
```

```
## [1] "George Bush 1990-10-01"
```

```
## [1] "George Bush 1991-01-01"
```

```
## [1] "George Bush 1991-04-01"
```

```
## [1] "George Bush 1991-07-01"
```

```
## [1] "George Bush 1991-10-01"
```

```
## [1] "George Bush 1992-01-01"
```

```
## [1] "George Bush 1992-04-01"
```

```
## [1] "George Bush 1992-07-01"
```

```
## [1] "George Bush 1992-10-01"
```

```
## [1] "George Bush 1993-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "William J. Clinton 1993-01-01"
```

```
## [1] "William J. Clinton 1993-04-01"
```

```
## [1] "William J. Clinton 1993-07-01"
```

```
## [1] "William J. Clinton 1993-10-01"
```

```
## [1] "William J. Clinton 1994-01-01"
```

```
## [1] "William J. Clinton 1994-04-01"
```

```
## [1] "William J. Clinton 1994-07-01"
```

```
## [1] "William J. Clinton 1994-10-01"
```

```
## [1] "William J. Clinton 1995-01-01"
```

```
## [1] "William J. Clinton 1995-04-01"
```

```
## [1] "William J. Clinton 1995-07-01"
```

```
## [1] "William J. Clinton 1995-10-01"
```

```
## [1] "William J. Clinton 1996-01-01"
```

```
## [1] "William J. Clinton 1996-04-01"
```

```
## [1] "William J. Clinton 1996-07-01"
```

```
## [1] "William J. Clinton 1996-10-01"
```

```
## [1] "William J. Clinton 1997-01-01"
```

```
## [1] "William J. Clinton 1997-04-01"
```

```
## [1] "William J. Clinton 1997-07-01"
```

```
## [1] "William J. Clinton 1997-10-01"
```

```
## [1] "William J. Clinton 1998-01-01"
```

```
## [1] "William J. Clinton 1998-04-01"
```

```
## [1] "William J. Clinton 1998-07-01"
```

```
## [1] "William J. Clinton 1998-10-01"
```

```
## [1] "William J. Clinton 1999-01-01"
```

```
## [1] "William J. Clinton 1999-04-01"
```

```
## [1] "William J. Clinton 1999-07-01"
```

```
## [1] "William J. Clinton 1999-10-01"
```

```
## [1] "William J. Clinton 2000-01-01"
```

```
## [1] "William J. Clinton 2000-04-01"
```

```
## [1] "William J. Clinton 2000-07-01"
```

```
## [1] "William J. Clinton 2000-10-01"
```

```
## [1] "William J. Clinton 2001-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "George W. Bush 2001-01-01"
```

```
## [1] "George W. Bush 2001-04-01"
```

```
## [1] "George W. Bush 2001-07-01"
```

```
## [1] "George W. Bush 2001-10-01"
```

```
## [1] "George W. Bush 2002-01-01"
```

```
## [1] "George W. Bush 2002-04-01"
```

```
## [1] "George W. Bush 2002-07-01"
```

```
## [1] "George W. Bush 2002-10-01"
```

```
## [1] "George W. Bush 2003-01-01"
```

```
## [1] "George W. Bush 2003-04-01"
```

```
## [1] "George W. Bush 2003-07-01"
```

```
## [1] "George W. Bush 2003-10-01"
```

```
## [1] "George W. Bush 2004-01-01"
```

```
## [1] "George W. Bush 2004-04-01"
```

```
## [1] "George W. Bush 2004-07-01"
```

```
## [1] "George W. Bush 2004-10-01"
```

```
## [1] "George W. Bush 2005-01-01"
```

```
## [1] "George W. Bush 2005-04-01"
```

```
## [1] "George W. Bush 2005-07-01"
```

```
## [1] "George W. Bush 2005-10-01"
```

```
## [1] "George W. Bush 2006-01-01"
```

```
## [1] "George W. Bush 2006-04-01"
```

```
## [1] "George W. Bush 2006-07-01"
```

```
## [1] "George W. Bush 2006-10-01"
```

```
## [1] "George W. Bush 2007-01-01"
```

```
## [1] "George W. Bush 2007-04-01"
```

```
## [1] "George W. Bush 2007-07-01"
```

```
## [1] "George W. Bush 2007-10-01"
```

```
## [1] "George W. Bush 2008-01-01"
```

```
## [1] "George W. Bush 2008-04-01"
```

```
## [1] "George W. Bush 2008-07-01"
```

```
## [1] "George W. Bush 2008-10-01"
```

```
## [1] "George W. Bush 2009-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Barack Obama 2009-01-01"
```

```
## [1] "Barack Obama 2009-04-01"
```

```
## [1] "Barack Obama 2009-07-01"
```

```
## [1] "Barack Obama 2009-10-01"
```

```
## [1] "Barack Obama 2010-01-01"
```

```
## [1] "Barack Obama 2010-04-01"
```

```
## [1] "Barack Obama 2010-07-01"
```

```
## [1] "Barack Obama 2010-10-01"
```

```
## [1] "Barack Obama 2011-01-01"
```

```
## [1] "Barack Obama 2011-04-01"
```

```
## [1] "Barack Obama 2011-07-01"
```

```
## [1] "Barack Obama 2011-10-01"
```

```
## [1] "Barack Obama 2012-01-01"
```

```
## [1] "Barack Obama 2012-04-01"
```

```
## [1] "Barack Obama 2012-07-01"
```

```
## [1] "Barack Obama 2012-10-01"
```

```
## [1] "Barack Obama 2013-01-01"
```

```
## [1] "Barack Obama 2013-04-01"
```

```
## [1] "Barack Obama 2013-07-01"
```

```
## [1] "Barack Obama 2013-10-01"
```

```
## [1] "Barack Obama 2014-01-01"
```

```
## [1] "Barack Obama 2014-04-01"
```

```
## [1] "Barack Obama 2014-07-01"
```

```
## [1] "Barack Obama 2014-10-01"
```

```
## [1] "Barack Obama 2015-01-01"
```

```
## [1] "Barack Obama 2015-04-01"
```

```
## [1] "Barack Obama 2015-07-01"
```

```
## [1] "Barack Obama 2015-10-01"
```

```
## [1] "Barack Obama 2016-01-01"
```

```
## [1] "Barack Obama 2016-04-01"
```

```
## [1] "Barack Obama 2016-07-01"
```

```
## [1] "Barack Obama 2016-10-01"
```

```
## [1] "Barack Obama 2017-01-01"
```

```
## Warning: Unknown column 'PANEL'
```

```
## [1] "Donald J. Trump 2017-01-01"
```

```
## [1] "Donald J. Trump 2017-04-01"
```

```
## Executing: 
## convert -loop 0 -delay 20 Rplot1.png Rplot2.png Rplot3.png
##     Rplot4.png Rplot5.png Rplot6.png Rplot7.png Rplot8.png
##     Rplot9.png Rplot10.png Rplot11.png Rplot12.png Rplot13.png
##     Rplot14.png Rplot15.png Rplot16.png Rplot17.png Rplot18.png
##     Rplot19.png Rplot20.png Rplot21.png Rplot22.png Rplot23.png
##     Rplot24.png Rplot25.png Rplot26.png Rplot27.png Rplot28.png
##     Rplot29.png Rplot30.png Rplot31.png Rplot32.png Rplot33.png
##     Rplot34.png Rplot35.png Rplot36.png Rplot37.png Rplot38.png
##     Rplot39.png Rplot40.png Rplot41.png Rplot42.png Rplot43.png
##     Rplot44.png Rplot45.png Rplot46.png Rplot47.png Rplot48.png
##     Rplot49.png Rplot50.png Rplot51.png Rplot52.png Rplot53.png
##     Rplot54.png Rplot55.png Rplot56.png Rplot57.png Rplot58.png
##     Rplot59.png Rplot60.png Rplot61.png Rplot62.png Rplot63.png
##     Rplot64.png Rplot65.png Rplot66.png Rplot67.png Rplot68.png
##     Rplot69.png Rplot70.png Rplot71.png Rplot72.png Rplot73.png
##     Rplot74.png Rplot75.png Rplot76.png Rplot77.png Rplot78.png
##     Rplot79.png Rplot80.png Rplot81.png Rplot82.png Rplot83.png
##     Rplot84.png Rplot85.png Rplot86.png Rplot87.png Rplot88.png
##     Rplot89.png Rplot90.png Rplot91.png Rplot92.png Rplot93.png
##     Rplot94.png Rplot95.png Rplot96.png Rplot97.png Rplot98.png
##     Rplot99.png Rplot100.png Rplot101.png Rplot102.png
##     Rplot103.png Rplot104.png Rplot105.png Rplot106.png
##     Rplot107.png Rplot108.png Rplot109.png Rplot110.png
##     Rplot111.png Rplot112.png Rplot113.png Rplot114.png
##     Rplot115.png Rplot116.png Rplot117.png Rplot118.png
##     Rplot119.png Rplot120.png Rplot121.png Rplot122.png
##     Rplot123.png Rplot124.png Rplot125.png Rplot126.png
##     Rplot127.png Rplot128.png Rplot129.png Rplot130.png
##     Rplot131.png Rplot132.png Rplot133.png Rplot134.png
##     Rplot135.png Rplot136.png Rplot137.png Rplot138.png
##     Rplot139.png Rplot140.png Rplot141.png Rplot142.png
##     Rplot143.png Rplot144.png Rplot145.png Rplot146.png
##     Rplot147.png Rplot148.png Rplot149.png Rplot150.png
##     Rplot151.png Rplot152.png Rplot153.png Rplot154.png
##     Rplot155.png Rplot156.png Rplot157.png Rplot158.png
##     Rplot159.png Rplot160.png Rplot161.png Rplot162.png
##     Rplot163.png Rplot164.png Rplot165.png Rplot166.png
##     Rplot167.png Rplot168.png Rplot169.png Rplot170.png
##     Rplot171.png Rplot172.png Rplot173.png Rplot174.png
##     Rplot175.png Rplot176.png Rplot177.png Rplot178.png
##     Rplot179.png Rplot180.png Rplot181.png Rplot182.png
##     Rplot183.png Rplot184.png Rplot185.png Rplot186.png
##     Rplot187.png Rplot188.png Rplot189.png Rplot190.png
##     Rplot191.png Rplot192.png Rplot193.png Rplot194.png
##     Rplot195.png Rplot196.png Rplot197.png Rplot198.png
##     Rplot199.png Rplot200.png Rplot201.png Rplot202.png
##     Rplot203.png Rplot204.png Rplot205.png Rplot206.png
##     Rplot207.png Rplot208.png Rplot209.png Rplot210.png
##     Rplot211.png Rplot212.png Rplot213.png Rplot214.png
##     Rplot215.png Rplot216.png Rplot217.png Rplot218.png
##     Rplot219.png Rplot220.png Rplot221.png Rplot222.png
##     Rplot223.png Rplot224.png Rplot225.png Rplot226.png
##     Rplot227.png Rplot228.png Rplot229.png Rplot230.png
##     Rplot231.png Rplot232.png Rplot233.png Rplot234.png
##     Rplot235.png Rplot236.png Rplot237.png Rplot238.png
##     Rplot239.png Rplot240.png Rplot241.png Rplot242.png
##     Rplot243.png Rplot244.png Rplot245.png Rplot246.png
##     Rplot247.png Rplot248.png Rplot249.png Rplot250.png
##     Rplot251.png Rplot252.png Rplot253.png Rplot254.png
##     Rplot255.png Rplot256.png Rplot257.png Rplot258.png
##     Rplot259.png Rplot260.png Rplot261.png Rplot262.png
##     Rplot263.png Rplot264.png Rplot265.png Rplot266.png
##     Rplot267.png Rplot268.png Rplot269.png Rplot270.png
##     Rplot271.png Rplot272.png Rplot273.png Rplot274.png
##     Rplot275.png Rplot276.png Rplot277.png Rplot278.png
##     Rplot279.png Rplot280.png Rplot281.png Rplot282.png
##     Rplot283.png Rplot284.png Rplot285.png Rplot286.png
##     Rplot287.png Rplot288.png Rplot289.png 'pres.gif'
```

```
## Output at: pres.gif
```

```
## [1] TRUE
```
