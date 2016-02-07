import pprint
from collections import namedtuple
from openpyxl import load_workbook
import csv

pp = pprint.PrettyPrinter(indent=4)

#Import workbook to manipulate
wb = load_workbook(filename = 'refugee_stats.xlsx')
ws_source = wb.get_sheet_by_name('Refugee Origins')
ws_target = wb.get_sheet_by_name('Refugee Sheet Organized')

#named tuple
country = namedtuple("country", ["name", "year"])

#custom dictionary with two keys
my_dict = {}

#Fetch all the rows from the source sheet
for rowOfCellObjects in ws_source['A1':'C80429']:
	my_list = list()
	for cellObj in rowOfCellObjects:
		my_list.append(cellObj.value)
	country = my_list[0]
	refugees = my_list[1]
	
	value = my_dict.get(country, None)
	
	if(value == None):
		value = refugees
	else:
		if(value == None):
			continue
		elif(refugees == None):
			continue
		else:
			value += refugees
	my_dict[country] = value

dict_size = len (my_dict)

pp.pprint(dict_size)

writer = csv.writer(open('dict.csv', 'wb'))
for key, value in my_dict.iteritems():
   writer.writerow([key, value])