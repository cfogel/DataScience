"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkstats2
import thinkplot

import relay


def BiasPmf(pmf, speed, name=None):
    """Returns a new Pmf representing speeds observed at a given speed.

    The chance of observing a runner is proportional to the difference
    in speed.

    Args:
        pmf: distribution of actual speeds
        speed: speed of the observing runner
        name: string name for the new dist

    Returns:
        Pmf object
    """
    new = pmf.Copy(name=name)
    for val, prob in new.Items():
        diff = abs(val - speed)
        new.Mult(val, diff)
    new.Normalize()
    return new


def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    # plot the distribution of actual speeds
    pmf = thinkstats2.MakePmfFromList(speeds, 'actual speeds')

    # plot the biased distribution seen by the observer
    biased = BiasPmf(pmf, 7.5, name='observed speeds @ 7.5mph')
    biased2 = BiasPmf(pmf, 5, name='observed speeds @ 5mph')
    biased3 = BiasPmf(pmf, 10, name='observed speeds @ 10mph')

    thinkplot.Hist(biased)
    thinkplot.Hist(biased2)
    thinkplot.Hist(biased3)
    thinkplot.Save(root='observed_speeds',
                   title='PMF of running speed',
                   xlabel='speed (mph)',
                   ylabel='probability')

    cdf = thinkstats2.MakeCdfFromPmf(biased)
    cdf2 = thinkstats2.MakeCdfFromPmf(biased2)
    cdf3 = thinkstats2.MakeCdfFromPmf(biased3)

    thinkplot.Clf()
    thinkplot.Cdf(cdf)
    thinkplot.Cdf(cdf2)
    thinkplot.Cdf(cdf3)
    thinkplot.Save(root='observed_speeds_cdf',
                   title='CDF of running speed',
                   xlabel='speed (mph)',
                   ylabel='cumulative probability')


if __name__ == '__main__':
    main()
