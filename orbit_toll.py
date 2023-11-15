import numpy as np 
import math

# construct the constant
G = 6.67*10**(-11)
M = 5.965*10**24
R = 6.378*10**6

# construct the data
def cal_r_by_T(T:int)->int:
    """
    param:
        T: the second of the T of satellite
    return:
        r: orbit radium
    """
    return ( (G*M*T**2) / (4*math.pi**2) ) ** (1/3)

# print(cal_r_by_T(1.5*3600)-R)
