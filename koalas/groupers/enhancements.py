"""
GroupBy Enhancements
---------
These functions add common functionality directly to DataFrame behavior,
in order to avoid common code being written over and over
"""
import pandas as pd
import numpy as np

from pandas.core.dtypes.inference import is_list_like


def _group_consecutive_values(frame, cols=None, level=None):
    """
    Groups a frame by consecutive equal values

    Parameters
    ----------
    frame
    cols
    level

    Returns
    -------

    """
    if cols is None:

        if is_list_like(level):

            idx = frame.index.to_frame()[level]
            grouper = (idx != idx.shift()).any(1).cumsum()

        else:

            idx = frame.index.get_level_values(level).to_series()
            grouper = (idx != idx.shift()).cumsum()

    else:

        if is_list_like(cols):

            vals = frame[cols]
            grouper = (vals != vals.shift()).any(1).cumsum()

        else:

            vals = frame[cols]
            grouper = (vals != vals.shift()).cumsum()

    return frame.groupby(grouper)
