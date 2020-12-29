import numpy as np
import matplotlib.pyplot as plt

# from analyzer.fitters.Cosine import Cosine
# this is the how at did it at first, but kind of redundant

import plottr.analyzer.fitters as ftr

tvals = np.linspace(0, 2, 51)
data = 1.5 * np.cos(2*np.pi*1 * tvals + np.pi) + 0.5 + np.random.normal(scale=0.2, size=tvals.size)

fit = ftr.Cosine(tvals, data)
fit_guess = fit.run(dry=True)
fit_result = fit.run()

fig, ax = plt.subplots(1,1)
ax.plot(tvals, data, 'o', label='data')
ax.plot(tvals, fit_guess.eval(coordinates=tvals), '--', zorder=-1, label='guess')
ax.plot(tvals, fit_result.eval(coordiantes=tvals), '-', label='fit to: ' + fit.model.__doc__, lw=2)
ax.legend(loc=0, fontsize='small')

print(fit_result.lmfit_result.fit_report())





