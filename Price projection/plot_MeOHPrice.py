import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


year= np.array([2021,2050])
biom1_LB = np.array([2371.75,1646.44])
biom1_HB = np.array([5541.34,4010.94])
biom2_LB = np.array([3300.14,2574.84])
biom2_HB = np.array([7347.35,6411.70])

em1_LB = np.array([5947.51,1813.26])
em1_HB = np.array([11749.96,4569.43])
em2_LB = np.array([8123.43,2103.39])
em2_HB = np.array([17262.28,4569.43])


fig, ax = plt.subplots()

ax.plot(year, biom1_LB, color="dodgerblue")
ax.plot(year, biom1_HB, color="dodgerblue")

ax.plot(year, biom2_LB, linewidth=3, color="powderblue")
ax.plot(year, biom2_HB, color="powderblue")

ax.fill_between(
    year, biom1_LB, biom1_HB,
    interpolate=True, color="dodgerblue", alpha=0.25)

ax.fill_between(
    year, biom2_LB, biom2_HB,
    interpolate=True, color="powderblue", alpha=0.25)

patch1 = mpatches.Patch(color='dodgerblue', label='Bio-methanol < ¥39/GJ feedstock cost')
patch2 = mpatches.Patch(color='powderblue', label='Bio-methanol ¥39-97/GJ feedstock cost')
plt.legend(handles=[patch1, patch2],
           ncol=6, loc='lower center', bbox_to_anchor=(0.5, 1), fontsize='7', frameon=False)

plt.title("Bio-methanol Price Projection",y=1.1)
plt.xlim(2021,2050)
plt.ylim(0,8000)
plt.xlabel("Year")
plt.ylabel("Price projection (CNY/t)")
plt.subplots_adjust(top=0.8)
plt.show()


fig, ax = plt.subplots()
ax.plot(year, em1_LB, linewidth=3, color="darkorange")
ax.plot(year, em1_HB, color="darkorange")

ax.plot(year, em2_LB, linewidth=3, color="navajowhite")
ax.plot(year, em2_HB, color="navajowhite")

ax.fill_between(year, em1_LB, em1_HB,interpolate=True, color="darkorange", alpha=0.25)

ax.fill_between(year, em2_LB, em2_HB,interpolate=True, color="navajowhite", alpha=0.25)

patch1 = mpatches.Patch(color='darkorange', label='E-methanol CO2 from combined renewable source')
patch2 = mpatches.Patch(color='navajowhite', label='E-methanol CO2 from DAC only')
plt.legend(handles=[patch1, patch2],
           ncol=6, loc='lower center', bbox_to_anchor=(0.5, 1), fontsize='7', frameon=False)

plt.title("E-methanol Price Projection",y=1.1)
plt.xlim(2021,2050)
#plt.ylim(0,16000)
plt.xlabel("Year")
plt.ylabel("Price projection (CNY/t)")
plt.subplots_adjust(top=0.8)
plt.show()