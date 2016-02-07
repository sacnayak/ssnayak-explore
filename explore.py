import csv
import httplib2
from apiclient.discovery import build
import urllib
import json
import numpy as np
import matplotlib.pyplot as plt

# This API key is provided by google as described in the tutorial
API_KEY = 'AIzaSyBeO38viomvIbJ1Ed6oKUfJFLgAilysdSg'

# This is the table id for the fusion table
TABLE_ID = '1Ohk5XVdXtFFD1NeaJGljO_FClO-b0_WQv5q5__Ov'

try:
	fp = open("data.json")
	response = json.load(fp)
except IOError:
	service = build('fusiontables', 'v1', developerKey=API_KEY)
	query = "SELECT * FROM " + TABLE_ID
	response = service.query().sql(sql=query).execute()
	fp = open("data.json", "w+")
	json.dump(response, fp)

columns = response['columns'] # the names of all columns
rows = response['rows'] # the actual data

#bar chart
num = len(rows) #number of countries

refugee_num = []
width = 0.1
fig, ax = plt.subplots()
x_ticklabels = []

for i in range(num):
	row = rows[i]
	num_refugees = row[0]
	count = int(row[1])
	if(count > 500000):
		num_refugees = num_refugees.encode('ascii', 'ignore')
		x_ticklabels.append(num_refugees)
		refugee_num.append(count)

ind = np.arange(len(refugee_num)) #the x locations for the groups
#print x_ticklabels
#print refugee_num
rect = ax.bar(ind, refugee_num, width, color='r', yerr = 0)

ax.set_ylabel('Refugee Population')
ax.set_xlabel('Countries of Origin')
ax.set_xticks(ind + width)
ax.set_xticklabels(x_ticklabels)
# We change the fontsize of minor ticks label 
plt.tick_params(axis='both', which='major', labelsize=10)
plt.tick_params(axis='both', which='minor', labelsize=10)

plt.show()