#insert template header

#load pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import data file including gen time, time at GT and pop size at GT

#EDIT the t0 file name and path
phenotypes_absolute_plate='./popsize-at-t0/phenotypes.Absolute.plate_1t0' 

gdatat0 = pd.read_csv(phenotypes_absolute_plate+'.csv',index_col=3)
gdatat0.boxplot(column='popt0', by='gene')
plt.savefig('test1.svg')