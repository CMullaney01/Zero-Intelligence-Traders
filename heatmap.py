import multiprocessing
from multiprocessing import Pool
import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import pandas as pd


def strategy_values(avg_file_path):
    buy_dict = {}
    sell_dict = {}
    times = []
    for i in range(41):
      #round to 2 decimal places
      buy_dict[round(i * 0.05 - 1, 2)] = []
      sell_dict[round(i * 0.05 - 1, 2)] = []   
  
    # read the csv file
    with open(avg_file_path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
        num_traders = int((len(row) - 15) / 7)
        for i in range(num_traders):
          time = int(row[1])
          id = row[3 + (7 * i)]
          trader_type = row[4 + (7 * i)]
          active_strategy = float(row[6 + (7 * i)])
          active_prof = row[8 + (7 * i)]
          best_Buy_ID = row[-12]
          best_Buy_Prof = row[-10]
          best_Buy_strat = row[-8]
          best_Sell_ID = row[-6]
          best_Sell_Prof = row[-4]
          best_Sell_strat = row[-2]
          
          if time not in times:
            times.append(time)

          strat = round(active_strategy * 20) / 20
          # print(id[0])

          if id[0] == 'B':
            buy_dict[strat].append(time)
          else:
            sell_dict[strat].append(time)
    return buy_dict, sell_dict, times


file_path = "./BristolStockExchange-master/csvs/test_prde_0_4_0.01_strats.csv"
buy_dict, sell_dict, times = strategy_values(file_path)


df = pd.DataFrame(columns=['time', 'Buy_Strategy', "buy_occurences", "Sell_Strategy", "sell_occurences"])

for i in range(len(times)):
  for j in range(41):
    df.loc[len(df)] = [times[i], round(j * 0.05 - 1, 2), buy_dict[round(j * 0.05 - 1, 2)].count(times[i]), round(j * 0.05 - 1, 2), sell_dict[round(j * 0.05 - 1, 2)].count(times[i])]

buyHeat = df.pivot("Buy_Strategy", "time", "buy_occurences")
sellHeat = df.pivot("Sell_Strategy", "time", "sell_occurences")

ax = sns.heatmap(buyHeat)
plt.title("Heatmap of buy strategies over time")
plt.show()

ax = sns.heatmap(sellHeat)
plt.title("Heatmap of sell strategies over time")
plt.show()