# 画二维坐标图
# 读取csv并作图
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

readData = pd.read_csv("ECG_Image_data/mitbih_test.csv",
                       header=None)
print(readData.iloc[:, 187])
data = readData.iloc[21000, 0:186].tolist()
xData = list(range(1, len(data)+1))

plt.plot(xData, data, 'r')
plt.title("time-distance")
plt.xlabel("bits")
plt.ylabel("distance")
# plt.show()
N = S = V = F = Q = 0
for i in range(21891):  # 87553
    if readData.iloc[i, 187] == 0:
        N = N+1
    if readData.iloc[i, 187] == 1:
        S = S+1
    if readData.iloc[i, 187] == 2:
        V = V+1
    if readData.iloc[i, 187] == 3:
        F = F+1
    if readData.iloc[i, 187] == 4:
        Q = Q+1
TT = N+S+V+F+Q
print(N, S, V, F, Q, TT)
