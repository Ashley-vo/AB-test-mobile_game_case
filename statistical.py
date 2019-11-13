import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math



def standard_error(p_pool,n_a,n_b):
    se = math.sqrt(p_pool*(1-p_pool)*(1/n_a + 1/n_b))
    return se

def estimate_differences(a,b):
    return a-b

def margin_for_error(se,d_min):
    margin = se*1.96
    print("With the confident level 95%, the lower bound of confident interval is {} and the upper bound of confident interval is {}".format(d_min-margin,d_min+margin))



if __name__ == '__main__':
    df = pd.read_csv("cookie_cats.csv")
    # Check missing value
    df.info()


