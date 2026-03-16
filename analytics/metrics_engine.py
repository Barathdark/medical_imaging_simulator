import pandas as pd
import numpy as np

class MetricsEngine:

    def compute(self, results):

        df = pd.DataFrame(results, columns=["latency"])

        metrics = {

            "average_latency": df["latency"].mean(),
            "max_latency": df["latency"].max(),
            "min_latency": df["latency"].min(),
            "std_deviation": np.std(df["latency"]),
            "throughput": len(results) / df["latency"].sum()

        }

        return metrics, df