#insert template header

#load pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import data file including gen time, time at GT and pop size at GT

gdata = pd.read_csv('c:/python/popsize-at-t0/GTdata1.csv')

#calculate k = 0.693/GT 

k = 0.693 / gdata["GT"]

#insert k into gdata array postion 'col'
col=4
gdata.insert(col, 'k', k)
col = col + 1

#calculate kt2 (k * Time_GT) (time in hours) and append to array

kt2 = gdata["k"] * (gdata ["Time_GT"]/60)
gdata.insert(col,'kt2',kt2)
col = col + 1

#calculate log10n2 (log10(PopGT)) and append to array

log10n2 = np.log10(gdata["Pop_GT"])
gdata.insert(col, 'log10n2', log10n2)
col = col + 1

#calculate kt2b (kt2/2.303) and append to array

kt2b = gdata["kt2"] / 2.303
gdata.insert(col, "kt2b", kt2b)
col = col + 1

#calculate log10N1 (-kt2b-log10n2) and append to array

log10n1neg = gdata["kt2b"]-gdata["log10n2"]
log10n1 = log10n1neg * -1
gdata.insert(col, "log10n1", log10n1)
col = col + 1

#calculate pop size at t=0 (popt0=10^log10n1)

popt0 = 10 ** log10n1
gdata.insert(col, "popt0", popt0)
print gdata

gdata.plot.line("GT", "popt0")

#create new file with metadata and pop size at t=0, (statistics later)



#graph of calculated growth curve with raw data
#t= time on x-axis
#N= number of cells at t (y-axis) (kt2/2.303)+log10N1

t= 1
log10N=((gdata["k"]*t)/2.303)+gdata["log10n1"]
N=10** log10N
print N

#Need for loop for different values of t and create new data set (or some trick?)
#can I plot this together with raw data?

#if time, quality assurance, check that time at GT is 'reasonable' :is greater than/less than a user defined value