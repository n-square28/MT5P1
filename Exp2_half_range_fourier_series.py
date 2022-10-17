from sympy import *
from sympy.abc import x
from sympy import Piecewise as pw

def hrfs(f,L):
    a = (x>=0)&(x<=L)
    b = (x>=-L)&(x<0)
    
    f_odd = pw((f,a),(-f,b))
    f_even = pw((f,a),(f,b))
    
    f_sin = fourier_series(f_odd,(x,-L,L))
    f_cos = fourier_series(f_even,(x,-L,L))
    
    print("fourier sine series is, ")
    pprint(f_sin.truncate(3))
    print("\n")
    print("fourier Cosine series is, ")
    pprint(f_cos.truncate(3))
    print("\n")

    
hrfs(pi*x-x**2, pi)
hrfs(x, 1)

    
