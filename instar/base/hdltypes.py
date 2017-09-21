'''
    Base HDL type wrappers over MyHDL types to reduce verbosity
'''
import myhdl as hdl

def make_signal(nbits):
    ''' Build a myhdl signal
    The Signal is built slicing an intbv and started to zero
    :param nbits: The number of bits for the Signal
    '''
    return hdl.Signal(hdl.intbv(0)[nbits:0])
