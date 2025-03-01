from pyModelChecking import *

K = Kripke(R=[(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)],
           L={0: set(['p']), 1: set(['p', 'q']), 3: set(['p'])})

from pyModelChecking.CTL import *

phi=AU(True,Or('q',Not(EX('p'))))

print(phi)

print(modelcheck(K, phi))