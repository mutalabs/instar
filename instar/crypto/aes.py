''' Experimental implementation of AES core.
'''
from collections import namedtuple
import myhdl as hdl

Parameters = namedtuple('Parameters', ['FixKeySize', 'KeySize'])
Parameters.__doc__ = '''Parameters sets the configuration for the module.
    :param bool FixKeySize: Selects if the module can handle multiple key sizes
    :param int KeySize:  Set the max key size for the circuit
    '''


class Ports(object):
    def __init__(self, param):
        key_sizes = [128, 192, 256]
        assert isinstance(param.FixedSize, bool), ('You should select if the core '
                                                   'has fix key size using a boolean')
        assert param.KeySize in key_sizes, 'Select key size to be 128, 192 or 256'
        self.param = param
        self.clk = hdl.Signal(hdl.intbv(0)[1:])
        self.start = hdl.Signal(hdl.intbv(0)[1:])
        self.done = hdl.Signal(hdl.intbv(0)[1:])
        self.plain0 = hdl.Signal(hdl.intbv(0)[32:0])
        self.plain1 = hdl.Signal(hdl.intbv(0)[32:0])
        self.plain2 = hdl.Signal(hdl.intbv(0)[32:0])
        self.plain3 = hdl.Signal(hdl.intbv(0)[32:0])
        self.cypher_text0 = hdl.Signal(hdl.intbv(0)[32:0])
        self.cypher_text1 = hdl.Signal(hdl.intbv(0)[32:0])
        self.cypher_text2 = hdl.Signal(hdl.intbv(0)[32:0])
        self.cypher_text3 = hdl.Signal(hdl.intbv(0)[32:0])

@hdl.block
def circuit(ports):
    pass
