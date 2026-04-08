import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BC census 2016 data.csv")

high_burden = df[df["shelt_rent_30plus_rate"] > 50]

plt.figure()
plt.scatter(high_burden["median_household_income"], high_burden["median_rent"])
plt.xlabel("Median Household Income")
plt.ylabel("Median Rent")
plt.title("High Burden Areas (>50%)")
plt.savefig("task1_chart.png")

pha_avg = df.groupby("pha")["rent_subsidy"].mean()

plt.figure()
pha_avg.plot(kind="bar")
plt.title("Average Rent Subsidy by PHA")
plt.ylabel("Average Subsidy")
plt.savefig("task2_chart.png")

plt.figure()
plt.scatter(df["median_rent"], df["rent_subsidy"])
plt.xlabel("Median Rent")
plt.ylabel("Rent Subsidy")
plt.title("Rent vs Subsidy")
plt.savefig("task3_chart.png")

print("Done")
