import numpy as np 
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, Gate
from qiskit.quantum_info.operators import Operator

import matplotlib.pyplot as plt 


qc = QuantumCircuit(4)
theta = Parameter(r'$(\theta)$')
uccsd = Gate(name='       UCCSD        ', num_qubits=4, params=[theta])
post_rotate = Gate(name='PR', num_qubits=4, params=[])


# qc.h(0)
qc.x(2)
qc.x(3)
qc.barrier()

# qc.h(0)
# qc.h(1)
# qc.h(2)
# qc.h(3)
# qc.rx(np.pi/2, 0)
# qc.rx(np.pi/2, 3)


# qc.cx(0,1)
# qc.cx(1,2)
# qc.cx(2,3)
# qc.rz(theta, 3)
# qc.cx(2,3)
# qc.cx(1,2)
# qc.cx(0,1)
# qc.barrier()
# qc.h(0)
# qc.h(1)
# qc.h(2)
# qc.h(3)
# qc.rx(-np.pi/2, 0)
# qc.rx(-np.pi/2, 3)
qc.append(uccsd, [0,1,2,3])
qc.append(post_rotate, [0,1,2,3])

qc.measure_all()
qc.draw('mpl', justify='center', plot_barriers=False)
plt.tight_layout()
# plt.savefig('a1a2a3a4_r.pdf')
# plt.savefig('a_4a_1_r.pdf')
plt.savefig('uccsd_qc.pdf')
# plt.savefig('initial_state_r.pdf')
# plt.show()