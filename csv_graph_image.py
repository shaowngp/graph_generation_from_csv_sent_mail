#!/usr/bin/env python
# coding: utf-8
# Author: Imam Uddin Ahamed

# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style 
from datetime import datetime
import runpy
import csv

# Storing pursed datetime function into variable 
now = datetime.now()
dateinfo = now.strftime("%m%d%Y")
print("date and time:",dateinfo)

# Reading the CSV file & storing in a variable
a=pd.read_csv('D:\\Python_test\\tps_report.csv')  #--> sample file path example in windows  


# Creating an  dynamic image file  name based on date
file_name='D:\\Python_test\\daily_avg_tps_'+dateinfo+'.png'
print(file_name)

# Setting graph plot style
plt.style.use('ggplot')


# Setting Column names in a variable
A=a['Day']
B=a['Avg_TPS']


# Setting plot figure Heading
fig = plt.figure()
fig.suptitle('Daily Average TPS')

# Setting X & Y axis label with desired values
plt.xlabel('DATE')
plt.ylabel('AVG_TPS')

# Plotting the graph & save the graph in an image
plt.plot(A,B)
plt.savefig(file_name)

# Calling a python script required for sending mails with 
runpy.run_path(path_name='sending_mails.py')

print("Mail has been sent with attachments. Thanks !!!");
# Thanks for viewing the script. If you want to add more advance features , please comment on github.
