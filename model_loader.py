from functools import lru_cache
import pandas as pd

class DummyModel:
    def sample(self, n):
        return pd.DataFrame([{"id": i, "amount": i * 10} for i in range(n)])

@lru_cache
def get_model(domain: str):
    return DummyModel()
