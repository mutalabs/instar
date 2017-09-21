''' RISC V internal registers
    RV32I has 32 registers.
    R0: always zero
    R1-R31: general-purpose registers
'''

import myhdl as hdl
from ..base import hdltypes as tp

class RegisterPorts(object):
    ''' Creates a myhdl interface with the required ports
        clk - clock signal
        wr_en - enable write to rd
        rd_sel - Select destination register
        rs1_sel - Select rs1 register 
        rs2_sel - Select rs2 register 
        rs1 - content of rs1
        rs2 - content of rs2
        rd - data to write to rd
    '''
    def __init__(self):
        self.clk = tp.make_signal(1)
        self.wr_en = tp.make_signal(1)
        self.rd_sel = tp.make_signal(5)
        self.rs1_sel = tp.make_signal(5)
        self.rs2_sel = tp.make_signal(5)
        self.rs1 = tp.make_signal(32)
        self.rs2 = tp.make_signal(32)
        self.rd = tp.make_signal(32)

@hdl.block
def registers(port):
    ''' Implement the internal registers for RiscV RV32I
    :param port: The circuit ports, should be the interface type
                 RegisterPorts
    '''
    regs = [tp.make_signal(32) for i in range(32)]
