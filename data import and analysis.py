import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quickspikes as qs
from scipy.signal import lfilter
import rainflow
import networkx as nx
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
df = pd.read_csv(r"C:\Users\beeka\Desktop\strain gauge verification-20221115T072633Z-001\strain gauge "
                 r"verification\load_cell.csv")
print("importing output voltage from csv file")
input_voltage = float(input("enter the input voltage"))
gage_factor = float(input("enter the gage factor"))
df.plot()
plt.show()
strain_swl = df.Strain_gauge / (128 * 1000 * input_voltage * gage_factor)
stress_swl = strain_swl * 2.06 * 100000

# strain_swr = df.Output_voltage1[0:5000] / (128 * 1000 * input_voltage * gage_factor)
# stress_swr = strain_swr * 2.06 * 100000
# round_swl = round(stress_swl, 0)
# round_swr = round(stress_swr, 0)
# rainflow_swl = rainflow.count_cycles(round_swl)
# rainflow_swr = rainflow.count_cycles(round_swr)
# print(rainflow_swl)
# print(rainflow_swr)
Load = (2000 / 7.3) * (df.Load_cell/ 256)
plt.plot(Load, label="load")
plt.plot(stress_swl, label="swing arm left")
plt.grid()
plt.show()
print(max(abs(stress_swl)))
print(max(abs(Load)))
# plt.plot(stress_swr, label="swing arm right")
# plt.legend()
# plt.ylabel("stress")
# plt.show()
# n = 600 # the larger n is, the smoother curve will be
# b = [1.0 / n] * n
# a = 1
# yy = lfilter(b, a, stress_swl)
# plt.plot(yy, linewidth=2, linestyle="-", c="b")  # smooth by filter
# print(yy)
# plt.show()
# x = strain_swl
# peaks, _ = find_peaks(x, height=0)
# plt.plot(x)
# plt.plot(peaks, x[peaks], "x")
# plt.plot(np.zeros_like(x), "--", color="gray")
# plt.show()
# x = strain_swl
# peaks, _ = find_peaks(x, height=(None, 100))
# plt.plot(x)
# plt.plot(peaks, x[peaks], "x")
# plt.plot(np.zeros_like(x), "--", color="gray")
# plt.show()