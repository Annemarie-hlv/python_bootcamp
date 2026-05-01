import pandas as pd
import numpy as np



class DataAnalyzer:
    def __init__ (self, filename):
        self.filename = filename
        self.data=None
        print(f"DataAnalyzer created for file: {self.filename}")

    def load_data(self):
        print(f"Loading {self.filename}")

        raw_values = np.random.randn(5,5)
        self.data = pd.DataFrame(raw_values, columns=['A', 'B', 'C', 'D', 'E'])
        print("Data loaded successfully")

    def get_stats(self):
        if self.data is None:
            print("Data not loaded. Please Load data first.")
        else:
            return self.data.describe()

if __name__ == "__main__":
    my_processor = DataAnalyzer("bootcamp_data.csv")
    my_processor.load_data()
    stats = my_processor.get_stats()
    print(stats)
    







