import myhdl as hdl


def clock_gen(clk_s, Ticks):
    interval = hdl.delay(Ticks)

    @hdl.always(interval)
    def clk():
        clk_s.next = not clk_s

    return clk
