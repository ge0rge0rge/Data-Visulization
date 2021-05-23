
import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
with open('dataset.csv') as csvfile:
  file = csv.reader(csvfile)
  data = []

  for item in file:

      data.append(item)

  # print(data)
print(len(data))
csvfile.close()

#transform data

data=np.array(data)
# data=np.delete(data,0, axis = 0)


x= np.arange(15)
bac=data[1:16,1]
pen=data[1:16,2].astype(float)
stre=data[1:16,3].astype(float)
neo=data[1:16,4].astype(float)
gra=data[1:16,5]
width=0.2
# plt.bar(x, pen, width=0.2,color="red",label='Penicilin')
# plt.bar(x+width, stre, width=0.2,color="green", label='Streptomycin ')
# plt.bar(x+2*width, neo, width=0.2,color="blue",label='Neomycin')
plt.plot(x,pen,'r--o',label='Penicilin')
plt.plot(x,stre,'g--v',label='Streptomycin')
plt.plot(x,neo,'b--x',label='Neomycin')



negaorpos=[]
for i in range(len(gra)):
    if gra[i] == 'negative':
        negaorpos.append('grey')
    else:negaorpos.append('orange')
plt.yscale('log')
plt.xticks(x+1, bac,rotation=-60,fontsize=7)
# plt.gca().tick_params(axis='x', labelcolor=negaorpos)   #Works
for i in range(len(negaorpos)):
    plt.gca().get_xticklabels()[i].set_color(negaorpos[i])

plt.ylabel('MIC')
plt.title("MIC for Penicilin,Streptomycin and Neomycin on 16 bacteria")
# plt.text("negative",color='grey',verticalalignment='center', horizontalalignment='right')
# plt.text("postive",color='orange')
plt.text(9, 60, "Positive", size = 7,\
         family = "fantasy", color = "orange", style = "italic", weight = "light",\
         bbox = dict(facecolor = "orange", alpha = 0.2))
plt.text(9, 260, "Negative", size = 7,\
         family = "fantasy", color = "grey", style = "italic", weight = "light",\
         bbox = dict(facecolor = "grey", alpha = 0.2))
plt.legend(loc='best')

plt.show()