'''
Risc V implementation
'''
import myhdl as hdl

class RiscVPorts(object):
    ''' Ports definition for the Risc-V implementation '''
    def __init__(self, riscv_formal=False):
        self.clk = hdl.Signal(hdl.intbv(0)[1:])
        self.resetn = hdl.ResetSignal(0, active=0, async=True)
        self.m_addr = hdl.Signal(hdl.intbv(0)[31:0])
        self.m_wdata = hdl.Signal(hdl.intbv(0)[31:0])
        self.m_rdata = hdl.Signal(hdl.intbv(0)[31:0])
        if riscv_formal is True:
            self.rvfi_valid = hdl.Signal(hdl.intbv(0)[1:])
            self.rvfi_order = hdl.Signal(hdl.intbv(0)[63:0])
            self.rvfi_insn = hdl.Signal(hdl.intbv(0)[31:0])
            self.rvfi_trap = hdl.Signal(hdl.intbv(0)[1:])
            self.rvfi_halt = hdl.Signal(hdl.intbv(0)[1:])
            self.rvfi_intr = hdl.Signal(hdl.intbv(0)[1:])
            self.rvfi_rs1_addr = hdl.Signal(hdl.intbv(0)[4:0])
            self.rvfi_rs2_addr = hdl.Signal(hdl.intbv(0)[4:0])
            self.rvfi_rs1_rdata = hdl.Signal(hdl.intbv(0)[31:0])
            self.rvfi_rs2_rdata = hdl.Signal(hdl.intbv(0)[31:0])
            self.rvfi_rd_addr = hdl.Signal(hdl.intbv(0)[4:0])
            self.rvfi_rd_wdata = hdl.Signal(hdl.intbv(0)[31:0])
            self.rvfi_pc_rdata = hdl.Signal(hdl.intbv(0)[31:0])
            self.rvfi_pc_wdata = hdl.Signal(hdl.intbv(0)[31:0])
            self.rvfi_mem_addr = hdl.Signal(hdl.intbv(0)[31:0])
            self.rvfi_mem_rmask = hdl.Signal(hdl.intbv(0)[3:0])
            self.rvfi_mem_wmask = hdl.Signal(hdl.intbv(0)[3:0])
            self.rvfi_mem_rdata = hdl.Signal(hdl.intbv(0)[31:0])
            self.rvfi_mem_wdata = hdl.Signal(hdl.intbv(0)[31:0])

@hdl.block
def processor(Ports):
  reg_ports = registers.RegisterPorts()
  register_file = registers.registers(reg_ports)
