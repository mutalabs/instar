'''
Risc V implementation
'''
import myhdl as hdl

class RiscVPorts(object):
    def __init__(self):
        self.clk = hdl.Signal(hdl.intbv(0)[1:])

@hdl.block
def processor(Ports):
    #ALU
    #Registers
    # BUS master
    pass
