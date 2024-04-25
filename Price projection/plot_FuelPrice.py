import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


year1= np.array([2023,2030,2050])
MeOH_LB = np.array([884.28,294.76,171.55])
MeOH_HB = np.array([884.28,442.14,321.88])

year2 = np.array([2023,2050])
HFO_LB = np.array([84.01,49.52])
HFO_HB = np.array([107.97,91.96])
VLSFO_LB = np.array([106.63,63.67])
VLSFO_HB = np.array([129.66,120.26])

# Initialize figure and axis
fig, ax = plt.subplots()

# Plot lines
ax.plot(year1, MeOH_LB, color="green")
ax.plot(year1, MeOH_HB, color="green")

ax.plot(year2, HFO_LB, linewidth=3, color="darkgray")
ax.plot(year2, HFO_HB, color="darkgray")

ax.plot(year2, VLSFO_LB, linewidth=3, color="lightsteelblue")
ax.plot(year2, VLSFO_HB, color="lightsteelblue")

# Fill area
ax.fill_between(
    year1, MeOH_LB, MeOH_HB,
    interpolate=True, color="green", alpha=0.25)

ax.fill_between(
    year2, HFO_LB, HFO_HB,
    interpolate=True, color="darkgray", alpha=0.25)

ax.fill_between(
    year2, VLSFO_LB, VLSFO_HB,
    interpolate=True, color="lightsteelblue", alpha=0.25)

patch1 = mpatches.Patch(color='green', label='Green MeOH')
patch2 = mpatches.Patch(color='darkgray', label='HFO')
patch3 = mpatches.Patch(color='lightsteelblue', label='VLSFO')
plt.legend(handles=[patch1, patch2, patch3],
           ncol=6, loc='lower center', bbox_to_anchor=(0.5, 1), fontsize='9', frameon=False)

plt.title("Global Marine Fuels Price Projection",y=1.1)
plt.xlim(2023,2050)
plt.ylim(0,900)
plt.xlabel("Year")
plt.ylabel("Price projection (CNY/GJ)")
plt.subplots_adjust(top=0.8)
plt.show()