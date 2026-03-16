import pandas as pd
import numpy as np

class PerformanceAnalyzer:

    def analyze(self, results):

        df = pd.DataFrame(results, columns=["response_time"])

        metrics = {

            "avg_time": df["response_time"].mean(),
            "max_time": df["response_time"].max(),
            "min_time": df["response_time"].min(),
            "std_dev": np.std(df["response_time"])

        }

        return metrics, df