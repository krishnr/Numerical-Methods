# borrowing from Python 3 to make all division floating-point division
from __future__ import division
import math

# Euler's Method of solving DEs
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
# The error rate is defined as e_2h/e_h.
# This is calculated by halving h at every iteration and then checking
# the ratio of the previous error to the current one.


# Set these vars with the given information in the problem
# ========================================================

a = 1
b = 6
alpha = 1

def f(x,t):
    return 2 - x/t

def exact_soln(t):
    return t

# ========================================================

# start at a step size of a half and halve it every iteration
h = 1/2
# iterate up to h=1/2^iterations
iterations = 8

abs_error = [None] * (iterations + 1)

for j in xrange(1,iterations+1):
    N = int((b-a)/h)

    # setting the IC
    w, w_prev = alpha, None

    # calculates the approximate solution
    for i in xrange(1,N+1):
        t = a + i*h
        w_prev = w
        w = w_prev + h*f(w_prev,t-h)

    abs_error[j] = abs(exact_soln(t) - w)

    if (abs_error[j] == 0):
        print 'The approximate solution and the exact solution are equal.'
        print 'Solution = {0}'.format(w)
        break

    # 'or 0' handles the case where j = 0 (the error ratio is meaningless in this case)
    error_rate = (abs_error[j-1] or 0)/abs_error[j]

    spaces = 5*' '
    print 'h = {0} {1} Approx Soln = {2} {1} {1} Abs Error = {3} {1} Error Ratio = {4}'.format(
        '1/'+str(2**j), spaces, '{:10.6f}'.format(w), '{:10.6f}'.format(abs_error[j]), '{:10.6f}'.format(error_rate)
    )

    # halve the step size for the next iteration
    h /= 2