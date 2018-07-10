import butools
import butools.fitting as bfit
import butools.trace as btrace
import butools.ph as bph
from scipy.stats import erlang
from scipy.stats import pareto
import numpy as np
import matplotlib.pyplot as plt

butools.verbose = True
tr = pareto.rvs(3, size = 10000)
(xt, yt) = btrace.CdfFromTrace(tr)
plt.plot(xt, yt, label='Trace')

nstates = [3, 5, 7]
for ns in nstates:
    alpha, A, logli = bfit.PHFromTrace(tr, ns)
    intBounds = np.linspace(0, 20, 1000)
    yf = bph.CdfFromPH(alpha, A, intBounds)
    plt.plot(intBounds, yf, label='Fit with ' + str(ns) + ' transient states.' )

plt.legend(loc='best')
plt.title("Fitted CDF v.s. Emprical CDF")
plt.show()

