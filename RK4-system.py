# borrowing from Python 3 to make all division floating-point division
from __future__ import division
import math

# Fourth Order Runge-Kutta Method of solving a system of first order DEs
# =============================
# A higher order DE can be converted to a system of 2 first order DEs
#
# The IVP should look like:
# x'(t) = f(t,x,y) where t belongs to [a,b]
# y'(t) = g(t,x,y) where t belongs to [a,b]
# x(a) = alpha
# y(a) = beta
#
# You should also be given either h (the step-size) or N (the number of sub-intervals)
#
# The solutions are approximated by w and v


# Set these vars with the given information in the problem
# ========================================================

a = 0
b = 0.1
alpha = 0
beta = 1

def f(t,x,y):
    return y

def g(t,x,y):
    _lambda = 1/2
    w_0 = 1
    return math.exp(-t) - 2*_lambda*y - w_0**2 * x

# set only 1 of these
h = None
N = 1

exact_soln_exists = False
def exact_soln(t):
    return math.sqrt(t**2 + 1)

# ========================================================

if h:
    N = int((b-a)/h)
else:
    h = (b-a)/N

w, w_prev = None, None
v, v_prev = None, None

for i in xrange(0,N+1):

    t = a + i*h

    if i == 0:
        w = alpha
        v = beta
    else:
        w_prev = w
        v_prev = v

        k1 = h*f(t-h, w_prev, v_prev)
        m1 = h*g(t-h, w_prev, v_prev)
        k2 = h*f(t-h + h/2, w_prev + k1/2, v_prev + m1/2)
        m2 = h*g(t-h + h/2, w_prev + k1/2, v_prev + m1/2)
        k3 = h*f(t-h + h/2, w_prev + k2/2, v_prev + m2/2)
        m3 = h*g(t-h + h/2, w_prev + k2/2, v_prev + m2/2)
        k4 = h*f(t-h + h, w_prev + k3, v_prev + m3)
        m4 = h*g(t-h + h, w_prev + k3, v_prev + m3)

        w = w_prev + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        v = v_prev + 1/6 * (m1 + 2*m2 + 2*m3 + m4)

    spaces = 10*' '
    if exact_soln_exists:
        x_t = exact_soln(t)
        error = abs(x_t - w)
        print 't_{0} = {1} {2} w_{0} = {3} {2} v_{0} = {6} {2} x({0}) = {4} {2} x({0}) - w_{0} = {5}'.format(
            str(i), '{:5.2f}'.format(t), spaces, '{:10.6f}'.format(w), '{:10.6f}'.format(x_t), '{:10.6f}'.format(error), '{:10.6f}'.format(v)
        )
    else:
        print 't_{0} = {1} {2} w_{0} = {3} {2} v_{0} = {4}'.format(
            str(i), '{:5.2f}'.format(t), spaces, '{:10.6f}'.format(w), '{:10.6f}'.format(v)
        )
