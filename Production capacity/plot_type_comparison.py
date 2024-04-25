import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv('Global/Global data.csv')
    #df.drop(df[(df['Year'] < 2021) & (df['Year'] > 2028) ].index, inplace=True)
    df.drop(df[(df.Year > 2028)].index, inplace=True)
    df.drop(df[(df.Year < 2020)].index, inplace=True)

    pivot_df = df.pivot_table(index='Year', columns='Type', values='Capacity (kt)', aggfunc='sum')

    fig, ax = plt.subplots()
    China_df = pivot_df[['Bio-methanol (China)', 'E-methanol (China)']]
    Global_df = pivot_df[['Bio-methanol (Global)', 'E-methanol (Global)']]
    China_df.plot(kind="bar", stacked=True, width=0.4,
                  ax=ax, position=1)
    Global_df.plot(kind="bar", stacked=True, width=0.4,
                       ax=ax, position=0, hatch='//')
    ax.set_xlim(right=len(Global_df) - 0.5)
    plt.title('Domestic vs Global Green Methanol Market 2020-2028',y=1.1)
    plt.xlabel('Year')
    plt.ylabel('Capacity (kt)')
    plt.subplots_adjust(top=0.8)
    plt.legend(ncol=6, loc='lower center', bbox_to_anchor=(0.5, 1), fontsize='7', frameon=False)
    plt.tight_layout()
    plt.show()