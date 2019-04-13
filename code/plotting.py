"""This model contains helper functions for plotting"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def ecdf(data):
    """
        This methods caculcates the x,y coordinates for an ecdf-plot

    parameters:
        data: numpy array of pandas series of data

    return parameters:
        sorted numpy array of values, numpy array of percentage of values below indexed value

    """
    if type(data) is np.ndarray:
        data = data[~np.isnan(data)]
        return np.sort(data), np.arange(1, len(data) + 1) / len(data)
    else:
        data = data.dropna()
        return np.sort(data.values), np.arange(1, len(data.values) + 1) / len(data.values)


def plot_ecdf(x=None, y=None, series=None,
              ax=None, xlim=None, xlabel=None, flg_annotation=True, flg_median=True, flg_interquartile_range=False,
              flg_ylabel=True, label=None,
              path=None, **kwargs):
    """

    :param x                            numpy array or pandas series of x-values for ecdf curve
    :param y:                           numpy array or pandas series of y-values for ecdf curve
    :param series                       pandas series for which to calculate the ecdf curve
    :param ax:                          axis object on which ecdf curve is to be plotted
    :param xlim:                        tuple of x limits of plot
    :param xlabel:                      string xlabel of plot
    :param flg_annotation:              boolean for annotation in title
    :param flg_median:                  boolean if hline of median to be plotted
    :param flg_interquartile_range:     boolean if hlines of interquartile range to be plotted
    :param flg_ylabel:                  boolean if ylabel to be displayed
    :param label:                       string legend label
    :param path:                        string for save path
    :param kwargs:                      kwargs for scatterplot
    :return:                            axis object on which ecdf curve is plotted
    """

    if series is not None:
        x, y = ecdf(series)
    if ax is None:
        f, ax = plt.subplots(1, 1)
    ax.scatter(x, y, label=label, **kwargs)

    if flg_median:
        ax.vlines(np.nanmedian(x), 0, 0.5, linestyles="--")
    if flg_interquartile_range:
        ax.vlines(np.nanpercentile(x, 25), 0, 0.25, linestyles="--")
        ax.vlines(np.nanpercentile(x, 75), 0, 0.75, linestyles="--")
    if xlim is not None:
        ax.set_xlim(xlim)
    else:
        xlim = ax.get_xlim()
    if flg_annotation:
        ax.set_title(f"Contains {y[x<xlim[1]][-1]*100:.2f} % of all measurements")
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if flg_ylabel:
        ax.set_ylabel("Cumulative density")

    if path is not None:
        ax.get_figure().savefig(path, dpi=600)

    return ax