import numpy as np
import pandas as pd


def sampler(prices: pd.DataFrame):
    '''
    A very simple sampler that can be used to resample a price series

    It uses the Closing price if available else uses the
    Open price

    If neither the Open or Closing price are available, then the average of the High and Low
    will be used.
    '''

    # Take the closing price if available
    if prices.Close != np.NaN and prices.Close >= 0:
        return prices.Close

    if prices.Open != np.NaN and prices.Open >= 0:
        return prices.Open

    if prices.High != np.NaN and prices.High >= 0:
        if prices.Low != np.NaN and prices.Low >= 0:
            return (prices.High + prices.Low) / 2
        else:
            return prices.High
    else:
        # no more other options
        return prices.Low


def resample(tseries: pd.DataFrame) -> pd.DataFrame:
    '''
    Resample a time series with at least the follwoing values:
    Close
    Open
    High
    Low

    '''
    price_series = tseries.apply(sampler, axis=1)
    price_series[price_series == 0] = np.NaN
    price_series.fillna(method="ffill", inplace=True)
    return price_series
