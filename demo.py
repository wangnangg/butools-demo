import butools
import butools.fitting as bfit
import butools.trace as btrace
import butools.ph as bph
from scipy.stats import erlang
from scipy.stats import pareto
import numpy as np
import matplotlib.pyplot as plt

butools.verbose = True

# generate 10000 samples from a Pareto distribution
tr = pareto.rvs(3, size = 10000)

# draw the empirical CDF of the samples
(xt, yt) = btrace.CdfFromTrace(tr)
plt.plot(xt, yt, label='Trace')

# trying fitting using 3, 5, and 7 states
nstates = [3, 5, 7]
for ns in nstates:

    # use phase type distributions to fit this trace
    # tr: the trace (samples) to be fitted
    # ns: number of transient states to use
    alpha, A, logli = bfit.PHFromTrace(tr, ns)
    # alpha: initial probability of the Markov chain
    # A: transition rate matrix between transient states

    # draw the fitted CDF
    intBounds = np.linspace(0, 20, 1000)
    yf = bph.CdfFromPH(alpha, A, intBounds)
    plt.plot(intBounds, yf, label='Fit with ' + str(ns) + ' transient states.' )

plt.legend(loc='best')
plt.title("Fitted CDF v.s. Emprical CDF")
plt.show()

