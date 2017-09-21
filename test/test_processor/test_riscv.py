from instar.processor import riscv


def bench(stimulus, verification, circuit_parameters):
    signals = design.CircuitPorts(circuit_parameters)
    dut = design.circuit(signals)
    f_estimulo = stimulus(signals)
    f_verifica = verification(signals)
    return dut, f_estimulo, f_verifica

