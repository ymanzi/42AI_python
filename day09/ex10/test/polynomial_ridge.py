
import numpy as np
import pandas as pd
from ridge import *
import matplotlib.pyplot as mpl

def MSE_cost_function(predicted_values, expected_values):
    i = 0
    summation = 0
    lenght = len(predicted_values)
    while i < lenght:
        summation += (predicted_values[i] - expected_values[i]) ** 2
        i += 1
    return summation / lenght

x = np.array(pd.read_csv("../../resources/spacecraft_data.csv")[["Age", "Terameters", "Thrust_power"]])
x = add_polynomial_features(x, 3)
y = np.array(pd.read_csv("../../resources/spacecraft_data.csv")[["Sell_price"]])
data = data_spliter(x, y)

i = 0
cost = []
lambdas = []
while i <= 1:
    RLR = MyRidge(np.ones(((x.shape[1] + 1, 1))), lambda_=i, alpha=1e-13, n_cycle=10000)
    RLR.fit_(data[0], data[1])
    cost.append(MSE_cost_function(RLR.predict_(data[2]), data[3]))
    lambdas.append(i)
    i += 0.1
print(cost)

mpl.plot(lambdas, cost)
mpl.show()