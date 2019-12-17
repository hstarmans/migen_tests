
from migen.build.generic_platform import Subsignal, Pins, IOStandard
from migen.build.lattice import LatticePlatform
from migen.build.lattice.programmer import MyStormProgrammer


_io = [
    ("sram", 0,
        Subsignal("adr", Pins("34 33 32 31 25 10 9 4 3 2 107 106 105",
                              "104 102 62 60 61 98")),
        Subsignal("dat", Pins("136 135 134 130 125 124 122 121 62 61 60 56 55",
                              "48 47 45")),
        Subsignal("oe", Pins("76")),
        Subsignal("we", Pins("11")),
        Subsignal("cs", Pins("24")),
        Subsignal("ub", Pins("75")),
        Subsignal("lb", Pins("81")),
        IOStandard("LVCMOS33"),
    ),

    ("clk100", 0, Pins("49"), IOStandard("LVCMOS33")),

    ("user_led", 0, Pins("110"), IOStandard("LVCMOS33")),
    ("user_led", 1, Pins("93"), IOStandard("LVCMOS33")),
    ("user_led", 2, Pins("94"), IOStandard("LVCMOS33")),

]

_connectors = []


class Platform(LatticePlatform):
    default_clk_name = "clk100"
    default_clk_period = 10

    def __init__(self):
        LatticePlatform.__init__(self, "ice40-hx8k-tq144:4k",
                                 _io, _connectors, toolchain="icestorm")

    def create_programmer(self, serial_port="/dev/ttyACM0"):
        return MyStormProgrammer(serial_port)