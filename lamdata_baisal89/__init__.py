"""
Lambda - a collection  of data science helper functions
"""

import pandas as pd
import numpy as np

#sample code

#sampe datasets
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

#sample functions
def increment(x):
    return(x + 1)
