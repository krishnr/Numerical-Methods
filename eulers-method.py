# borrowing from Python 3 to make all division floating-point division
from __future__ import division
import math

# Euler's Method of solving DEs
# =============================
#
# The IVP should look like:
# y'(t) = f(t,y) where t belongs to [a,b]
# y(a) = alpha
#
# You should also be given either h (the step-size) or N (the number of sub-intervals)
#
# The solution is approximated by w


# Set these vars with the given information in the problem
# ========================================================

a = 0
b = 2
alpha = 1

def f(y,t):
    return math.exp(t)/y

# set only 1 of these
h = None
N = 4

exact_soln_exists = True
def exact_soln(t):
    return math.sqrt(2 * math.exp(t) - 1)

# ========================================================


if h:
    N = int((b-a)/h)
else:
    h = (b-a)/N

w = [None] * (N+1)

for i in xrange(0,N+1):

    t = a + i*h

    if i == 0:
        w[0] = alpha
    else:
        w[i] = w[i-1] + h*f(w[i-1],t-h)

    spaces = 10*' '
    if exact_soln_exists:
        x_t = exact_soln(t)
        error = x_t - w[i]
        print 't_{0} = {1} {2} w_{0} = {3} {2} y({0}) = {4} {2} y({0}) - w_{0} = {5}'.format(
            str(i), '{:5.2f}'.format(t), spaces, '{:10.6f}'.format(w[i]), '{:10.6f}'.format(x_t), '{:10.6f}'.format(error)
        )
    else:
        print 't_{0} = {1} {2} w_{0} = {3}'.format(
            str(i), '{:5.2f}'.format(t), spaces, '{:10.6f}'.format(w[i])
        )