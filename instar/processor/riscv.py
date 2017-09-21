'''
Risc V implementation
'''
import myhdl as hdl
from .registers import *
class RiscVPorts(object):
    def __init__(self):
        self.clk = hdl.Signal(hdl.intbv(0)[1:])

@hdl.block
def processor(Ports):
  reg_ports = registers.RegisterPorts()
  register_file = registers.registers(reg_ports)
