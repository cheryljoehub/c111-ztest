import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("medium_data.csv")
data=df["Math_score"].tolist()
fig = px.scatter(x = title, y = reading_time)

fig = ff.create_distplot([data], ["Math scores"], show_hist=False)
fig.show()

mean = statistics.mean(data)
print("Mean of sampling distribution :-",mean )

std_deviation = statistics.stdev(data)
print("standard deviation of sampling distribution :-",mean )

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
print("standard deviation of sampling distribution :-",mean )
mean = statistics.mean(mean_list)
print("Mean of sampling distribution :-",mean )
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.02], mode="lines", name="MEAN"))
fig.show()

first_std_deviation_start,first_std_deviation_end = mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation),mean+(3*std_deviation)
print("std1",first_std_deviation_start,first_std_deviation_end)
print("std2",second_std_deviation_start,second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STD deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STD deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="STD deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STD deviation 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="STD deviation 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="STD deviation 3"))
fig.show()
