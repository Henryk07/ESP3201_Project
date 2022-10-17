# 画二维坐标图
# 读取csv并作图
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

readData = pd.read_csv("ECG_2_data/archive/INCART 2-lead Arrhythmia Database.csv",
                       header=None)
print(readData.iloc[1, :])
data = readData.iloc[105729, 2:33].tolist()
xData = list(range(1, len(data)+1))

plt.plot(xData, data, 'r')
plt.title("time-distance")
plt.xlabel("bits")
plt.ylabel("distance")
plt.show()
N = S = V = F = Q = 0
for i in range(175729):  # 87553
    if readData.iloc[i, 1] == 'N':
        N = N+1
    if readData.iloc[i, 1] == 'VEB':
        S = S+1
    if readData.iloc[i, 1] == 'SVEB':
        V = V+1
    if readData.iloc[i, 1] == 'F':
        F = F+1
    if readData.iloc[i, 1] == 'Q':
        Q = Q+1
TT = N+S+V+F+Q
print(N, S, V, F, Q, TT)
