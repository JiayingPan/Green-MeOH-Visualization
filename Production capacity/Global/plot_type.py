import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv('Global data.csv')
    df = df[~df['Type'].isin(['Bio-methanol (China)','E-methanol (China)'])]

    pivot_df = df.pivot_table(index='Year', columns='Type', values='Capacity (kt)', aggfunc='sum')

    pivot_df.plot(kind='bar', stacked=True)
    plt.title('Global Green Methanol Market 2020-2029',y=1.1)
    plt.xlabel('Year')
    plt.ylabel('Capacity (kt)')
    plt.subplots_adjust(top=0.8)
    plt.legend(ncol=3, loc='lower center', bbox_to_anchor=(0.45, 1), fontsize='8', frameon=False)
    plt.tight_layout()
    plt.show()