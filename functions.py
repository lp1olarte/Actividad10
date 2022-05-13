
from scipy.stats import linregress    

def slope(x,y):
    return linregress(x,y).slope
def intercept(x,y):
    return linregress(x,y).intercept
def corr_coef(x,y):
    return linregress(x,y).rvalue
