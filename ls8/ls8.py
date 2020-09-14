#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load()
cpu.run()

class ls8:

    def LDI(self):
    """load "immediate", store a value in a register, or "set this register to
  this value""""


    def PRN(self):
    """a pseudo-instruction that prints the numeric value stored in a
  register"""


    def HLT(self):
    """halt the CPU and exit the emulator"""

