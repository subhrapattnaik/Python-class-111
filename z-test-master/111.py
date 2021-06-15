import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("./111/z-test-master/studentMarks.csv")
data = df["Math_score"].tolist()

#plotting the graph
fig=ff.create_distplot([data],["Math Scores"],show_hist=False)
fig.show()


#find mean and standard deviation

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of popultion:- ",mean)
print("Standard deviation of popultion:- ",std_deviation)

