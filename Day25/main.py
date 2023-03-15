# with open("Day25\weather_data.csv","r") as weatherData:
#   data=weatherData.readlines()
#   print(data)
# import csv
# day=[]
# temp=[]
# condition=[]
# with open("Day25\weather_data.csv","r") as weatherData:
#   orderedData=csv.DictReader(weatherData)
#   for col in orderedData:
#     day.append(col["day"])
#     temp.append(int(col["temp"]))
#     condition.append(col["condition"])
# print(temp)
# max= data["temp"].max()
# print(data["temp"])
# data= pd.read_csv(r"C:\Users\Owner\DaysCode100\Day25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# greysquirll_Count=len(data[data["Primary Fur Color"]=="Gray"])
# redsquirll_Count=len(data[data["Primary Fur Color"]=="Cinnamon"])
# blacksquirll_Count=len(data[data["Primary Fur Color"]=="Black"])
# print(greysquirll_Count)
# print(redsquirll_Count)
# print(blacksquirll_Count)
# dict={"Primary Fur Color":["Grey","Cinnamon","Black"],
# "Squirrel Count":[greysquirll_Count,redsquirll_Count,blacksquirll_Count]
# }
# df=pd.DataFrame(dict)
# df.to_csv("Squirrel Count.csv")
# print(max)

# print(average)
# print(data[data.temp==data.temp.max()])

import pandas as pd
  
