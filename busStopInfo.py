"""
This was created for fun for personal use to track buses from within Python. 
The idea is to not leave the IDE to check for buses. Hope to build on this in the future,
so as to automatically get alerts at pre-destined times according to class schedule.
"""

import requests
import pandas as pd

# the base CUMTD url
url = "https://www.cumtd.com/maps-and-schedules/bus-stops/info/"

# add favorite bus-stops here
stops = {'Wright and Springfield': 'wrtspfld',
         'Green and Mathews': 'grnmat',
         'White and Second': 'wht2nd'}

# Print list of your favorite bus-stops
for i, stop in enumerate(stops):
    print('%d. %s' % (i, stops.keys()[i]))

# /TODO: add an option for user to select multiple bus-stops
user_in = int(raw_input("Select a stop: "))

if user_in in range(i+1):
    url = url + stops.values()[user_in]
else:
	# Incorrect choice
    raise ValueError

a = requests.get(url)
# find the table in html source
st = a.text.find("initialData: ")
# find the end of the dictionary
ed = a.text[st:].find("\r\n\t")

# cast values in dictionary to Python datatypes
true = True
false = False
null = None
data = eval(a.text[st + 13: st+ed])

# put all Departure data in a nice data frame
stopInfo = pd.DataFrame(data['Departures'])

# Print what is required
out = stopInfo[['Route', 'Headsign', 'IsIStop', 'RealTime', 'DestinationText']].to_string
print out.im_self
