from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class CustomScaler(BaseEstimator, TransformerMixin):

    def __init__(self) -> None:
        super().__init__()
        self.mean = None
        self.std = None
    
    def fit(self, col):
        self.mean = np.mean(col)
        self.std = np.std(col)

        return self

    def transform(self, col):
        if (None in self.mean or None in self.std):
            raise ValueError('You probably havent fitted the scaler yet')
        x = col.copy()
        x = (x - self.mean) / self.std
        return x