import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv('Domestic data.csv')

    pivot_df = df.pivot_table(index='Year', columns='Feedstock', values='Capacity (kt)', aggfunc='sum')

    pivot_df.plot(kind='area', stacked=True)
    plt.title('Domestic Green Methanol Feedstock Composition',y=1.1)
    plt.xlim(2020,2028)
    plt.xlabel('Year')
    plt.ylabel('Capacity (kt)')
    plt.ylim(0,10000)
    plt.subplots_adjust(top=0.8)
    plt.legend(ncol=4, loc='lower center', bbox_to_anchor=(0.45, 1), fontsize='8', frameon=False)
    plt.tight_layout()
    plt.show()