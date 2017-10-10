import myhdl as hdl
from instar.processor import rv_registers
from instar.resources.resources import clock_gen

def bench(stimulus, verification):
    sim_signals = rv_registers.RVRegPorts()
    gen_clk = clock_gen(sim_signals.clk, Ticks=10)
    dut = rv_registers.rv_registers(sim_signals)
    dt_create = stimulus(sim_signals)
    dt_verif = verification(sim_signals)
    return gen_clk, dut, dt_create, dt_verif

def test_read_from_R0():
    '''
    The return from R0 must always be zero, since it's supposed to be hardcoded.
    '''
    def stimulus(signals):
        yield signals.clk.posedge

    def verification(signals):
        while True:
            yield signals.clk.posedge
            raise hdl.StopSimulation

    simulation = hdl.Simulation(bench(stimulus, verification))
    simulation.run()
