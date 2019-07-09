"""
Koalas Primary DataFrame Updates
---------
This is where all utility functions provided by koalas are
namespaced to a pandas DataFrame.  Users can also optionally monkey-patch
pandas itself in order to add the accessors directly to a DataFrame,
although that approach is not as recommended as simply use the `kl` accessor
"""
import pandas as pd
import numpy as np
from koalas.groupers.enhancements import _group_consecutive_values


@pd.api.extensions.register_dataframe_accessor("kl")
class Koalas:
    """
    Class to add attributes to a pandas DataFrame
    """

    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(obj):
        return obj is not None

    def consecutive(self, cols=None, level=None):
        return _group_consecutive_values(self._obj, cols, level)
