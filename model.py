"""Reconstruction from manuscript animals-4654775, NOT original author source."""
from math import ceil
import numpy as np
TARGET=70.; F=100; EGGS=20000; SURVIVAL=.065; PRICE=1.50; CF=270.; CM=150.; DISCOUNT=.08; CYCLES=3
REVENUE=F*EGGS*SURVIVAL*PRICE
SCENARIOS=[('Ideal',70.,'#0a9b76'),('Microscopic',29.,'#3c9fc8'),('Visual',12.27,'#126da7'),('Random',6.135,'#e59d13')]
UNCOMPENSATED_PROFIT=72975. # published assumption; not independently derived

def males_per_ten(m): return TARGET/np.asarray(m)
def male_count(m): return ceil((F/10)*TARGET/m)
def total_cost(m,discrete=False):
    m=np.asarray(m)
    n=np.ceil(F/10*TARGET/m) if discrete else F/10*TARGET/m
    return F*CF+CM*n

def annual_npv(p,year): return sum(CYCLES*p/(1+DISCOUNT)**y for y in range(1,year+1))
