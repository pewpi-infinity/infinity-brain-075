import qutip as qt
import numpy as np

phase = 2.1227
ket00 = qt.tensor(qt.basis(2, 0), qt.basis(2, 0))
ket11 = qt.tensor(qt.basis(2, 1), qt.basis(2, 1))
bell = (ket00 + np.exp(1j * phase) * ket11) / np.sqrt(2)
rho = bell * bell.dag()

print("Node 075 Entangled Density Matrix (core: 'probably made my dad able to get away with all he has'):")
print(rho)
