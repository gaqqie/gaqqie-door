# gaqqie-door: a client library for users to access the quantum computer cloud platform gaqqie-sky in gaqqie suite

**This is a beta version.**

[![License](https://img.shields.io/github/license/gaqqie/gaqqie-door)](https://opensource.org/licenses/Apache-2.0)


## What is **gaqqie-door**?

**gaqqie-door** is a client library for users to access the quantum computer cloud platform **gaqqie-sky** in **gaqqie** suite.  
For more information on **gaqqie**, see [this](https://github.com/gaqqie/gaqqie).


## Installation

```bash
pip install gaqqie-door
```


## How to use gaqqie-door

The currently supported quantum programming language is Qiskit.

```python
from qiskit import QuantumCircuit, execute
from gaqqie_door import QiskitGaqqie


circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

url = "https://<api-id>.execute-api.<region>.amazonaws.com/<stage>" # rewrite to the endpoint URL of the user API
QiskitGaqqie.enable_account(url)
backend = QiskitGaqqie.get_backend("qiskit_simulator")

job = execute(circuit, backend)
result = job.result()
print(f"result job_id={job.job_id()}, counts={result.get_counts()}")
```

Sample output:
```
result job_id=6abff77e-4fda-4880-b3a5-ea8f49ff7cf0, counts={'00': 482, '11': 542}
```

