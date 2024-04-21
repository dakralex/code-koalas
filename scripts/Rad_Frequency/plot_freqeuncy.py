import csv
import json

import matplotlib.pyplot as plt
import numpy as np


def get_data (file):


    cyclists = []
    data = json.load(file)
    for i in data:
        l = int(i.get("count"))
        cyclists.append(l)

    return cyclists


data = get_data(open("data/processed/cyclists.json"))

data = np.array(data)

years = [2018, 2019, 2020, 2021, 2022, 2023]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

months_repeated = []
for i in range(2018,2024):
    for j in months:
        months_repeated.append(j+" " + str(i))

x = np.linspace(0,12*6,72)
fig, ax = plt.subplots()
ax.plot(months_repeated, data, color="orange")
ax.fill_between(months_repeated,data,alpha=0.2, color="orange")

plt.xlabel("Months")
plt.ylabel("Number of Cyclists")
plt.xticks(range(0, len(months_repeated), 5), months_repeated[::5])
plt.title("Number of Cyclist in the time of 2018 tp 2023")
plt.show()

