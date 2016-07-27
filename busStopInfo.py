import requests
import pandas as pd

url = "https://www.cumtd.com/maps-and-schedules/bus-stops/info/"

stops = {'Wright and Springfield': 'wrtspfld',
         'Green and Mathews': 'grnmat',
         'White and Second': 'wht2nd'}

for i, stop in enumerate(stops):
    print('%d. %s' % (i, stops.keys()[i]))

user_in = int(raw_input("Select stop(s) in comma separated fashion: "))

if user_in in range(i+1):
    url = url + stops.values()[user_in]
else:
    raise ValueError

a = requests.get(url)
# find the table in html source
st = a.text.find("initialData: ")
# find the
ed = a.text[st:].find("\r\n\t")

true = True
false = False
null = None
data = eval(a.text[st + 13: st+ed])

stopInfo = pd.DataFrame(data['Departures'])

out = stopInfo[['Route', 'Color', 'IsIStop', 'RealTime']].to_string

print out.im_self
