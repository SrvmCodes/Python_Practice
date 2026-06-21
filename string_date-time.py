# Using datetime module
from datetime import datetime
date = "Feb 19 2018 11:30AM"
date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")
print(date_time)
print(type(date_time))

#Using dateutil Module
from dateutil import parser
date_time = parser.parse("Feb 19 2018 11:30AM")

print(date_time)
print(type(date_time))
