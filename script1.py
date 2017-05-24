#insert template header

#load pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import data file including gen time, time at GT and pop size at GT

gdata = pd.read_csv('c:/python/popsize-at-t0/GTdata1.csv',index_col=0)

#calculate k = 0.693/GT 

k = 0.693 / gdata["GT"]

#insert k into gdata array postion 'col'
col=3
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



#create new file with metadata and pop size at t=0, (statistics later)

#calculate a theoretical growth curve and plot along with raw data


def CellN(t,str_k,str_log10n1):
    str_log10N=(str_k*t/2.303)+str_log10n1
    str_N=10**str_log10N
    return str_N
       

for t in range(1,24):
    CellN(t,gdata.loc['strain1',["k" ]] [0], gdata.loc['strain1',["log10n1" ]] [0])
    
   

#def graph(x_range):
    #x=np.array(x_range)
    #y=CellN(x,gdata.loc['strain1',["k" ]] [0], gdata.loc['strain1',["log10n1" ]] [0])
    #plt.plot(x,y)
        

#graph (range(1,25))

#add raw data to graph

#s1data = pd.read_csv('c:/python/popsize-at-t0/strain1data.csv')
#x2=s1data["time"]
#y2=s1data["cellN"]
#plt.scatter(x2,y2)
#plt.show()
#plt.savefig("strain1.png")


#Need for loop for different values of t and create new data set (or some trick?)

def graph():
    for index,row in (gdata.iterrows()):
        x = np.array(range(1,25))
        y = CellN(x,row["k" ],row["log10n1" ])
        plt.plot(x,y)
        print x, y
        plt.show()
    
graph()

    
#Or maybe call one strain's data at a time?

#for index, row in gdata.iterrows():
  # print row["k"]
    
    
    
#for each strain, for t=1 to 24 (each hour), calculate N and create a new array labeled with row lab, t and N in columns  


#can I plot this together with raw data?

#if time, quality assurance, check that time at GT is 'reasonable' :is greater than/less than a user defined value