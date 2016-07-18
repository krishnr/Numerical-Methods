# borrowing from Python 3 to make all division floating-point division
from __future__ import division
import math

# Heun's Method of solving DEs
# =============================
#
# The IVP should look like:
# x'(t) = f(t,x) where t belongs to [a,b]
# x(a) = alpha
#
# You should also be given either h (the step-size) or N (the number of sub-intervals)
#
# The solution is approximated by w
#
# Heun's Method is a special case of RK2 where a1=a2=1/2 and beta = gamma = h


# Set these vars with the given information in the problem
# ========================================================

a = 1
b = 6
alpha = 1

def f(x,t):
    return 1 + x/t

# set only 1 of these
h = 0.5
N = None

exact_soln_exists = False
def exact_soln(t):
    return t + 1/t

# ========================================================

if h:
    N = int((b-a)/h)
else:
    h = (b-a)/N

a1, a2 = 1/2, 1/2
beta, gamma = h, h

w, w_prev = None, None

for i in xrange(0,N+1):

    t = a + i*h

    if i == 0:
        w = alpha
    else:
        w_prev = w
        temp_w = w_prev + h*f(w_prev, t-h)
        w = w_prev + h/2 * (f(w_prev, t-h) + f(temp_w, t))

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
