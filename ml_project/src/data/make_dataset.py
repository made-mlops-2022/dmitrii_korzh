# -*- coding: utf-8 -*-
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from src.entities import SplittingParams


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def split_train_val_data(
    data: pd.DataFrame, params: SplittingParams, is_predict=False
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """

    :rtype: object
    """
    if not is_predict:
        train_data, val_data = train_test_split(
            data, test_size=params.val_size, random_state=params.random_state
        )
    else:
        train_data = None
        val_data = data
    return train_data, val_data
