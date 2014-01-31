"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkplot
import thinkstats2


def main():

    d = {
        1: 4,
        2: 12,
        3: 4,
        4: 4,
        5: 1,
        6: 0,
        7: 0,
    }

    # form the pmf
    pmf = thinkstats2.MakePmfFromDict(d, 'family size')
    print 'mean', pmf.Mean()
    print 'var', pmf.Var()
    
    # plot the Pmfs
    thinkplot.Pmf(pmf)
    thinkplot.Show(xlabel='Family size',
                   ylabel='PMF')
    
 
if __name__ == '__main__':
    main()
