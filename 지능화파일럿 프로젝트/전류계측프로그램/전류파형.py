import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)


sys.setrecursionlimit(100000)

df = pd.read_csv("data/3Phase.CSV", skiprows=[0,1,2]) #0,1,2행 생략

plt.figure(figsize=(12,8))

plt.plot(df['INDEX'], df['R'], 'r-', label='R')
plt.plot(df['INDEX'], df['S'], 'g-', label='S')
plt.plot(df['INDEX'], df['T'], 'b-', label='T')
plt.legend()
#plt.show()
plt.savefig('역상파형(0.5A)/10(S_-245).png')