import pandas as pd
import matplotlib.pyplot as plt
import sys
filename = sys.argv[-1]
# filename = "dist/output/output_2021-01-22_06点29分45秒.csv"
output = pd.read_csv(filename)
output.index = output.time
output.voltage.plot()
output.current.plot()
plt.show()