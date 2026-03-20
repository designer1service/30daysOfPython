
Day 16 — Date and Time  

> **Today’s Focus:** Work with Python’s datetime module to get current time, format dates, parse date strings, and calculate differences between dates. 
> **Author:** Luka Marinkovic  

## What I learned  

I explored the **datetime** module and looked at its available attributes and classes using `dir(datetime)`. I used `datetime.now()` to get the current date and time and then accessed individual components such as `day`, `month`, `year`, `hour`, `minute`, `second`, and the Unix timestamp.  This gave me a clear idea of how to pull out exactly the pieces of time information I need. 

## Working with datetime objects  

I created specific `datetime` instances like `datetime(2020, 1, 1)` and printed their components and formatted output.  Using `strftime`, I formatted dates and times into human‑readable strings in different styles, such as `"HH:MM:SS"`, `"mm/dd/YYYY, HH:MM:SS"`, and `"dd/mm/YYYY, HH:MM:SS"`.  I also converted a date string like `"5 December, 2019"` into a `datetime` object with `strptime`, learning how format codes map to parts of a date string.
## Date, time, and timedelta  

I used the `date` class to work only with calendar dates, created a `date(2020, 1, 1)` and used `date.today()` to get the current date and extract year, month, and day.  I experimented with the `time` class to represent times independently of dates, constructing several time objects with different hours, minutes, seconds, and microseconds.  With `timedelta`, I modeled intervals of time and subtracted one `timedelta` from another, as well as computed how many days are left until the new year from a given date. 

## Practical exercises  

In the exercises, I repeated the process of extracting the current date components and timestamp, then formatted them as strings using `strftime`.  I parsed a date string into a `datetime` object and confirmed its type, then calculated how many days remain until the start of 2027 using `date` subtraction.  Finally, I computed the difference in days between today’s date and a fixed past date (1 January 1970), which reinforced how to combine parsing, conversion to `date`, and date arithmetic. 

| Directive| Description                                      | Example                 |
|----------|--------------------------------------------------|-------------------------|
| %a       | Weekday, short version                           | Wed                     |
| %A       | Weekday, full version                            | Wednesday               |
| %w       | Weekday as a number 0–6, 0 is Sunday             | 3                       |
| %d       | Day of month 01–31                               | 31                      |
| %b       | Month name, short version                        | Dec                     |
| %B       | Month name, full version                         | December                |
| %m       | Month as a number 01–12                          | 12                      |
| %y       | Year, short version, without century             | 18                      |
| %Y       | Year, full version                               | 2018                    |
| %H       | Hour 00–23                                       | 17                      |
| %I       | Hour 00–12                                       | 05                      |
| %p       | AM/PM                                            | PM                      |
| %M       | Minute 00–59                                     | 41                      |
| %S       | Second 00–59                                     | 08                      |
| %f       | Microsecond 000000–999999                        | 548513                  |
| %z       | UTC offset                                       | +0100                   |
| %Z       | Timezone                                         | CST                     |
| %j       | Day number of year 001–366                       | 365                     |
| %U       | Week number of year, Sunday as first day, 00–53  | 52                      |
| %W       | Week number of year, Monday as first day, 00–53  | 52                      |
| %c       | Local version of date and time                   | Mon Dec 31 17:41:00 2018|
| %x       | Local version of date                            | 12/31/18                |
| %X       | Local version of time                            | 17:41:00                |
| %%       | A % character                                    | %                       |
