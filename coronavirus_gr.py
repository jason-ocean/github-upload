import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pld
import os

os.chdir("D:\Python lessons\coronavirus_case_study")
path = os.getcwd()

df = pd.read_csv(path + "\coronavirus_cases_gr.csv")


#convert column to datetime

df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
#df.head()
day1 = pd.Series([df["Confirmed cases"][0]])
df["New cases"] = day1.append(pd.Series([df["Confirmed cases"][i+1] - df["Confirmed cases"][i] for i in range(len( df["Confirmed cases"])-1)]), ignore_index = True)

### PLOT USING PLT
fig = plt.figure(figsize = (8,8))
# Getting only day and month from timestamp!!!
new_x = plt.gca()
xaxis = pld.date2num(df["Date"])    # Convert to maplotlib format
test = pld.DateFormatter('%d-%m')
new_x.xaxis.set_major_formatter(test)
ax = fig.add_subplot(1, 1, 1)
ax.set_facecolor('grey')

plt.title(label = "Coronavirus confirmed cases, Greece, 2020")
plt.plot(xaxis,df["Confirmed cases"], "-d", label = "Confirmed cases", color = "blue")
plt.plot(xaxis,df["New cases"], "-d", label = "New cases", color = "black")
#plt.plot(xaxis,df["Hospitalized"], "-d", label = "Hospitalized", color = "crimson")
plt.plot(xaxis,df["Severe cases"],"-d", label = "Severe cases", color = "orange")
plt.plot(xaxis,df["Deaths"],"-d", label = "Deaths", color = "red")
plt.plot(xaxis,df["Healed"],"-d", label = "Healed", color = "forestgreen")
plt.yscale('log')
plt.legend()
plt.xlabel("$Date$")
plt.ylabel("$N$")
plt.show()
plt.savefig("coronavirus_cases_gr.pdf")




### PLOT USING BOKEH

from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, output_file, show

colors= ["blue","crimson","orange","red","forestgreen"]

source = ColumnDataSource(data=dict(
    x=df["Date"],
    y1=df["Confirmed cases"],
    y2=df["Hospitalized"],
    y3=df["Severe cases"],
    y4=df["Deaths"],
    y5=df["Healed"],
    colors = colors,
    
))


fig = figure(title = "Coronavirus confirmed cases, Greece, 2020",x_axis_type="datetime",
     tools="hover, save")
fig.plot_width  = 500
fig.plot_height = 500
fig.line(x= "x", y = "y1",source = source, line_width = 5, color=colors[0])
fig.line(x= "x", y = "y2",source = source, line_width = 5, color=colors[1])
fig.line(x= "x", y = "y3",source = source, line_width = 5, color=colors[2])
fig.line(x= "x", y = "y4",source = source, line_width = 5, color=colors[3])
fig.line(x= "x", y = "y5",source = source, line_width = 5, color=colors[4])
#hover = fig.select(dict(type = HoverTool))
#hover.tooltips = {
#    "Location": "(@x, @y)"
#}
output_file("Coronavirus_Greece.html")
show(fig)

