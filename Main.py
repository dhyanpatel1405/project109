import random
import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff
import statistics 


count=[]
dice_answer=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_answer.append(dice1+dice2)
    count.append(i)
#mean=sum(dice_answer)/len(dice_answer)
#std_dev=statistics.stdev(dice_answer)
#median=statistics.median(dice_answer)
##mode=statistics.mode(dice_answer)




fig=ff.create_distplot([dice_answer],[])
#print(mean,std_dev,median,mode)
fig.show()


