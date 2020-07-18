from nmigen import *
from nmigen_boards.colorlight_5a_75b_7_0 import Colorlight5a75b70Platform


class Blinker(Elaboratable):
    def __init__(self, maxperiod):
        self.maxperiod = maxperiod

    def elaborate(self, platform):
        led = platform.request("user_led")

        m = Module()

        counter = Signal(range(self.maxperiod + 1))

        with m.If(counter == 0):
            m.d.sync += [
                led.eq(~led),
                counter.eq(self.maxperiod)
            ]
        with m.Else():
            m.d.sync += counter.eq(counter - 1)

        return m


plat = Colorlight5a75b70Platform()
plat.build(Blinker(10000000), do_program=False)
