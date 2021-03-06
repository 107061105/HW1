# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061105.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
#target_data = list(filter(lambda item: (item['station_id'] == 'C0A880' and item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000'), data))
#target_data = list(filter(lambda item: (item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000'), data))
target_data = list(sorted(data, key = lambda item: item['station_id']))

list1 = []
list1.append(target_data[0])

k = 0
list1[k]['HUMD'] = 'None'

for i in range(len(target_data)):
   if target_data[i]['station_id'] == list1[k]['station_id']:
      if target_data[i]['HUMD'] != '-99.000' and target_data[i]['HUMD'] != '-999.000':
         if list1[k]['HUMD'] == 'None':
            list1[k]['HUMD'] = target_data[i]['HUMD']
         else:
            list1[k]['HUMD'] = float(list1[k]['HUMD']) + float(target_data[i]['HUMD'])
   else:
      list1.append(target_data[i])
      k += 1
      if target_data[i]['HUMD'] != '-99.000' and target_data[i]['HUMD'] != '-999.000':
         list1[k]['HUMD'] == target_data[i]['HUMD']
      else:
         list1[k]['HUMD'] = 'None'


list3 = []
for i in range(len(list1)):
   list2 = []
   list2.append(list1[i]["station_id"])
   list2.append(list1[i]['HUMD'])
   list3.append(list2)

#=======================================

# Part. 4
#=======================================
# Print result
print(list3)