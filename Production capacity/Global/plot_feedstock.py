import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    df = pd.read_csv('Global data.csv')
    df = df[~df['Type'].isin(['Bio-methanol (China)','E-methanol (China)'])]

    pivot_df = df.pivot_table(index='Year', columns='Feedstock', values='Capacity (kt)', aggfunc='sum')

    pivot_df.plot(kind='area', stacked=True)
    plt.title('Global Green Methanol Feedstock Composition',y=1.15)
    plt.xlim(2010,2029)
    plt.xticks(np.arange(2010, 2029, step=2))
    plt.xlabel('Year')
    plt.ylabel('Capacity (kt)')
    plt.ylim(0,24000)
    plt.subplots_adjust(top=0.8)
    plt.legend(ncol=4, loc='lower center', bbox_to_anchor=(0.45, 1), fontsize='8', frameon=False)
    plt.tight_layout()
    plt.show()