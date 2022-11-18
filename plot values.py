import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quickspikes as qs
from scipy.signal import lfilter
import rainflow
import networkx as nx
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
df = pd.read_csv(r"C:\Users\beeka\Downloads\test_data_20221117-02.csv")
plt.subplot(1, 2, 1)
plt.plot(df.stress_abs)
plt.subplot(1, 2, 2)
plt.plot(df.load_cell_abs)
# plt.subplot(1, 2, 1)
# plt.plot(df.Strain_gauge_left_mpa)
# plt.subplot(1, 2, 2)
# plt.plot(df.Loadcell_reading_kg)
plt.show()


