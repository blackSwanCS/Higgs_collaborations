import numpy as np
from HiggsML.systematics import systematics


def tes_fitter(
    model,
    train_set,
):
    """
    Task 1 : Analysis TES Uncertainty
    1. Loop over different values of tes and make store the score
    2. Make a histogram of the score

    Task 2 : Fit the histogram
    1. Write a function to loop over different values of tes and histogram and make fit function for each bin in the histogram
    2. store the fit functions in an array
    3. return the fit functions

      histogram and make fit function which transforms the histogram for any given TES

    """
    syst_set = systematics(train_set, tes=1)
    score = model.predict(syst_set["data"])

    histogram = np.histogram(score, bins=100, range=(0, 1))

    # Write a function to loop over different values of tes and histogram and make fit function which transforms the histogram for any given TES

    def fit_function(array, tes):
        # Dummy fit function, replace with actual fitting procedure
        return [array[i] * f[i](tes) for i in range(len(array))]

    return fit_function


def jes_fitter(
    model,
    train_set,
):
    """
    Task 1 : Analysis JES Uncertainty
    1. Loop over different values of jes and store the score
    2. Make a histogram of the score

    Task 2 : Fit the histogram
    1. Write a function to loop over different values of JES and histogram and make fit function for each bin in the histogram
    2. store the fit functions in an array
    3. return the fit functions

      histogram and make fit function which transforms the histogram for any given jes

    """
    syst_set = systematics(train_set, jes=1)
    score = model.predict(syst_set["data"])

    histogram = np.histogram(score, bins=100, range=(0, 1))

    # Write a function to loop over different values of jes and histogram and make fit function which transforms the histogram for any given JES

    def fit_function(array, jes):
        # Dummy fit function, replace with actual fitting procedure
        return array * jes

    return fit_function
