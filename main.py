import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Air_Traffic_Passenger_Statistics_1.csv", delimiter=",")

#1. Фильтрация данных

dfATA = df[df["Operating Airline"] == "ATA Airlines"]
dfAC = df[df["Operating Airline"] == "Air Canada"]
dfAWA = df[df["Operating Airline"] == "WestJet Airlines"]

#2. Преобразование даты
ds_date = pd.to_datetime(dfATA.activity_Period, format = "%Y%m")

#3. Построение графика
fig, ax = plt.subplots()
plt.plot(pd.to_datetime(dfATA.activity_Period, format = "%Y%m"), dfATA["Passenger Count"], "-*k")
plt.plot(pd.to_datetime(dfAC.activity_Period, format = "%Y%m"), dfAC["Passenger Count"], "-or")
plt.plot(pd.to_datetime(dfAWA.activity_Period, format = "%Y%m"), dfAWA["Passenger Count"], "-b")
plt.show()