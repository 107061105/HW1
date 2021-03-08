# HW1
## Setup and run the program
This assignment is to analyze open-source auto weather station data from Central Weather Bureau (CWB).
To run this program with python3, you need to import csv module, and read cwb data, then write data into a list:
``` py
# Import module
#  csv -- fileIO operation
import csv

# Read cwb weather data
cwb_filename = '107061105.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
```

## How to adress the data
The purpose of this program is to find out the summation of the HUMD value from C0A880, C0F9A0, C0G640, C0R190, C0X260, so we need to imply following steps:
* Remove the data whose value of the HUMD (humidity) column is '-99.000' or '-999.000'.
* Sum all of HUMD data with same name
``` py
# Sum the HUMD data with same station
   if target_data[i]['station_id'] = list1[k]['station_id']:
      if target_data[i]['HUMD'] != '-99.000' and target_data[i]['HUMD'] != '-999.000':
            list1[k]['HUMD'] = float(list1[k]['HUMD']) + float(target_data[i]['HUMD'])
# If there is no more data, continute with next station
   else:
      list1.append(target_data[i])
```
* Output the ID of the station and the summation of it in the lexicographical order.
* If you cannot find the summation, please output 'None'

## Result

Output of the program:
``` py
[['C0A880', 19.330000000000002], ['C0F9A0', 16.83], ['C0G640', 18.96], ['C0R190', 20.110000000000003], ['C0X260', 18.25]]
```
