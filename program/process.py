"""CSC110 Project -- Processing Data"""

from typing import List
import pandas as pd
import statsmodels.api as sm


def intersecting_years(df_list: List[pd.DataFrame]) -> List[pd.DataFrame]:
    """Given a list of DataFrames with a continuous 'Year' column, return a list containing the same
    DataFrames with any years that are not present in the others removed.

    Preconditions:
        - df.empty == False
        - 'Year' in df.columns

    >>> data1 = {'Region': ['National', 'South'], 'Year': [2001, 2001], 'RSI': [3.0, 2.15]}
    >>> data2 = {'Year': [2001, 2002], 'Raw': [0.5, 0.8], 'Smoothed': [0.5, 0.7]}
    >>> df1 = pd.DataFrame(data1)
    >>> df2 = pd.DataFrame(data2)
    >>> intersecting_years([df1, df2])
    [     Region  Year   RSI
    0  National  2001  3.00
    1     South  2001  2.15,    Year  Raw  Smoothed
    0  2001  0.5       0.5]
    """
    upper_bound = min(max(df['Year']) for df in df_list)
    lower_bound = max(min(df['Year']) for df in df_list)

    return [df.query(str(upper_bound) + ' >= Year >= ' + str(lower_bound)) for df in df_list]


def lowess_smooth(df: pd.DataFrame, data: str) -> pd.DataFrame:
    """Given a DataFrame containing a 'Year' column and column with the name of the data input,
    return a lowess smoothed DataFrame with only the year and the smoothed data.

    Preconditions:
        - df.empty == False
        - 'Year' in df.columns
        - data in df.columns
    """
    return pd.DataFrame(sm.nonparametric.lowess(
        endog=df[data],
        exog=df['Year']
    ), columns=['Year', data])


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas', 'statsmodels'],
        'allowed-io': ['import_as_dict'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
