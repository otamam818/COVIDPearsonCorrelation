# Imports
# ---------------------------------------------------------------------------
import pandas as pd

from math import sqrt
from pandas.core.groupby.generic import DataFrameGroupBy

# Constants
# ---------------------------------------------------------------------------
# The file to reference from. Must be in the same folder as 
# this python module
DATA_FILE = "WHO-COVID-19-global-data.csv"

# This is a column in the data file you want 
# to base your pearson correlation from
COLUMN: str = "New_cases"

# Select any two countries. Make sure their names are in the "Country" 
# column of the data file
COUNTRY_1: str = "Australia"
COUNTRY_2: str = "Bangladesh"

# Main Function
# ---------------------------------------------------------------------------
def main(): 
    """
        Get the pearsons correlation between two countries and see 
        how related they are
    """
    # Extract data for the two groups we are interested in
    COUNTRIES = [COUNTRY_1, COUNTRY_2]
    country_groups = pd.read_csv(DATA_FILE).groupby("Country")
    country1, country2 = (get_column(country_groups, i) for i in COUNTRIES)
    print(get_pear_corr(country1, country2))

# Helper Functions and a user-defined class object
# ---------------------------------------------------------------------------
def get_column(groups: DataFrameGroupBy, country: str) -> pd.Series:
    """Get the column of the country of interest"""
    return groups.get_group(country)[COLUMN]

def get_pear_corr(series1: pd.Series, series2:pd.Series) -> float: 
    """Get the Pearsons Coefficient between these 2 countries"""
    c1 = pc_data(series1)
    c2 = pc_data(series2)
    num_entries = range(len(c1.dist_mean))

    # Numerator of the pearson's coefficient formula
    numerator = sum([c1.dist_mean[i]*c2.dist_mean[i] 
                     for i in num_entries])
    denominator = sqrt(c1.ssq_dist_mean*c2.ssq_dist_mean)

    return numerator/denominator

class pc_data:
    """
        Pearson's Correlation data: Wrapper class for most of the 
        required data
    """
    def __init__(self, data: pd.Series) -> None:
        self.mean: float = data.mean()
        self.dist_mean: list = self.__get_dist_mean(data)

        # Get the sum of squares for the denominator in later calculations
        self.ssq_dist_mean= sum([i*i for i in self.dist_mean])

    def __get_dist_mean(self, data: pd.Series):
        finlist = []
        for i in data:
            finlist.append(i-self.mean)
        return finlist

# Import convention
# ---------------------------------------------------------------------------
if __name__ == "__main__": 
    main()
