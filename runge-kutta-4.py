# borrowing from Python 3 to make all division floating-point division
from __future__ import division
import math

# Fourth Order Runge-Kutta Method of solving DEs
# =============================
#
# The IVP should look like:
# x'(t) = f(t,x) where t belongs to [a,b]
# x(a) = alpha
#
# You should also be given either h (the step-size) or N (the number of sub-intervals)
#
# The solution is approximated by w


# Set these vars with the given information in the problem
# ========================================================

a = 0
b = 1
alpha = 1

def f(x,t):
    return t/x

# set only 1 of these
h = 1/4
N = None

exact_soln_exists = True
def exact_soln(t):
    return math.sqrt(t**2 + 1)

# ========================================================

if h:
    N = int((b-a)/h)
else:
    h = (b-a)/N

w, w_prev = None, None

for i in xrange(0,N+1):

    t = a + i*h

    if i == 0:
        w = alpha
    else:
        w_prev = w
        k1 = h*f(w_prev,t-h)
        k2 = h*f(w_prev + k1/2,t-h + h/2)
        k3 = h*f(w_prev + k2/2,t-h + h/2)
        k4 = h*f(w_prev + k3,t-h + h)
        w = w_prev + 1/6 * (k1 + 2*k2 + 2*k3 + k4)

    spaces = 10*' '
    if exact_soln_exists:
        x_t = exact_soln(t)
        error = abs(x_t - w)
        print 't_{0} = {1} {2} w_{0} = {3} {2} x({0}) = {4} {2} x({0}) - w_{0} = {5}'.format(
            str(i), '{:5.2f}'.format(t), spaces, '{:10.6f}'.format(w), '{:10.6f}'.format(x_t), '{:10.6f}'.format(error)
        )
    else:
        print 't_{0} = {1} {2} w_{0} = {3}'.format(
            str(i), '{:5.2f}'.format(t), spaces, '{:10.6f}'.format(w)
        )
