import numpy as np

def bin_data(x_data, y_data, N_bins=100):
    """
    Bins the x-y data into a specified number of bins and calculates the mean value of y-data in each bin.

    Parameters:
        x_data (array-like): The x-values of the data to be binned.
        y_data (array-like): The y-values of the data to be binned.
        N_bins (int, optional): The number of bins to create. Default is 100.

    Returns:
        x_data_binned (array-like): The x-values at the center of each bin.
        y_data_binned (array-like): The mean value of y-data in each bin.

    Notes:
        This function bins the x-y data into N_bins equal-width bins and calculates the mean value of y-data in each bin.
        The bin edges are determined based on the range of x_data.
        The function does not take into account uncertainties or weighted averaging in the binning process.
    """
    x_bin_edges = np.linspace(min(x_data), max(x_data), N_bins+1)  # Define 3 bins (4 edges)
    x_bin_centers = 0.5 * (x_bin_edges[1:] + x_bin_edges[:-1])
    x_bin_indices = np.digitize(x_data, x_bin_edges)
    bin_means = [y_data[x_bin_indices == i].mean() for i in range(1, N_bins+1)]

    x_data_binned = x_bin_centers
    y_data_binned = bin_means
    return x_data_binned, y_data_binned
