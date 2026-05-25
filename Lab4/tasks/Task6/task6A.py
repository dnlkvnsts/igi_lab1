"""
The task number 6A

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1
Developer: Danilkova Anastasia Alexandrovna
Date: 17.04.2026
"""

import pandas as pd
import os
import base.input as inp
import base.output as out

def display(data, title=""):
    """
    Implementation of the display function (Requirement #4).
    Displays a Pandas object with a formatted header.
    """
    if title:
        print(f"\n{'='*15} {title} {'='*15}")
    print(data)
    print(f"{'=' * (32 + len(title))}")

class AutoStatsMixin:
    """
    Mixin class providing statistical analysis capabilities.
    """
    def get_summary(self, data):
        """
        Generates descriptive statistics for a given DataFrame.
        """
        return data.describe(include='all').round(2)

class PandasTaskBase:
    """
    Base class for tasks involving the Pandas library and file operations.
    """
    LIBRARY_NAME = "Pandas"

    def __init__(self, task_name):
        self._task_name = task_name
        self._dataset_name = "Automobile Dataset"
        self.file_path = os.path.join(os.path.dirname(__file__), 'Automobile_data.csv')

    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        if value.strip():
            self._task_name = value
        else:
            raise ValueError("Task name cannot be empty")

    def __str__(self):
        return f"Task: {self._task_name} using {self.LIBRARY_NAME}"

    def _load_real_data(self):
        """
        Reads the CSV file. Requirement #1: Pandas Import usage.
        """
        return pd.read_csv(self.file_path, na_values='?')

class CarDataAnalyzer(PandasTaskBase, AutoStatsMixin):
    """
    Specialized class for analyzing automobile data.
    """
    def __init__(self, task_name):
        super().__init__(task_name)

    def get_info(self):
        return f"Analysis scope: {self._dataset_name} (Series & DataFrames)"

    def create_series(self):
        """
         Series Structure and Creation.
        """
        df = self._load_real_data()
       
        subset = df.dropna(subset=['price', 'make']).head(4)
        prices = subset['price'].tolist()
        brands = subset['make'].tolist()
        
        
        car_series = pd.Series(data=prices, index=brands)
        
      
        loc_example = car_series.loc[brands[1]]
        iloc_example = car_series.iloc[1]
        
        return car_series, loc_example, iloc_example

    def create_car_dataframe(self):
        """
        DataFrame Creation from a list of lists.
        """
        df = self._load_real_data()
        temp_df = df[['body-style', 'horsepower', 'fuel-type', 'price']].dropna().head(3)
        
        
        data_list = temp_df.values.tolist()
        
        columns = ['Body-Style', 'Horsepower', 'Fuel-Type', 'Price']
        car_features = pd.DataFrame(data_list, columns=columns)
        car_features.index = ['car_A', 'car_B', 'car_C']
        return car_features

def run_task6A():
    """
    Main execution logic for Task 6A.
    """
    while True:
        out.print_message("Task 6A: Pandas Structures (English Version)")
        try:
            analyzer = CarDataAnalyzer("Automobile Research")
            print(analyzer)
            print(analyzer.get_info())

           
            series_obj, val_loc, val_iloc = analyzer.create_series()
            
            
            display(series_obj, "Pandas Series (Prices by Brand)")
            
            print(f"Access via .loc (label-based search for second brand):\n{val_loc}")
            print(f"\nAccess via .iloc[1] (position-based search for second item): {val_iloc}")
            
            
            df_small = analyzer.create_car_dataframe()
            display(df_small, "DataFrame 'car_features' (From List of Lists)")

            
            stats = analyzer.get_summary(df_small)
            display(stats, "Descriptive Statistics")

        except FileNotFoundError:
            print("\nError: Automobile_data.csv not found. Please ensure the file is in the same directory.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

        if not inp.repeat_task():
            break

if __name__ == "__main__":
    run_task6A()
