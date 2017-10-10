import myhdl as hdl

class RVRegPorts(object):
    ''' Risc-V register file interface signals
    '''
    def __init__(self):
        self.clk = hdl.Signal(hdl.intbv(0)[1:])
        self.en = hdl.Signal(hdl.intbv(0)[1:])
        self.wr_reg_sel = hdl.Signal(hdl.intbv(0)[4:])
        self.rd0_reg_sel = hdl.Signal(hdl.intbv(0)[4:])
        self.rd1_reg_sel = hdl.Signal(hdl.intbv(0)[4:])
        self.wr_reg = hdl.Signal(hdl.intbv(0)[31:0])
        self.rd0_reg = hdl.Signal(hdl.intbv(0)[31:0])
        self.rd1_reg = hdl.Signal(hdl.intbv(0)[31:0])


@hdl.block
def rv_registers(Ports):
    mem = [hdl.Signal(hdl.intbv(0)[31:0]) for i in range(32)]

    @hdl.always(Ports.clk.posedge)
    def write():
        if Ports.en is True:
            mem[Ports.wr_reg_sel].next = Ports.wr_reg

    @hdl.always_comb
    def read():
        if Ports.en is True:
            Ports.rd0_reg.next = mem[Ports.rd0_reg_sel]
            Ports.rd1_reg.next = mem[Ports.rd1_reg_sel]

    return hdl.instances()
