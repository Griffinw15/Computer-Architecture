"""CPU functionality."""

import sys

HLT = 0b00000001 
LDI = 0b10000010 #00000rrr iiiiiiii
PRN = 0b01000111 #00000rrr

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.registers = [0] * 8
        self.memory = [0] * 256
        self.pc = 0
        self.sp = self.registers[7]

    def load(self):
        """Load a program into memory."""

        address = 0

        if len(sys.argv) != 2:
            print("Usage: comp.py program_name")
            sys.exit(1)

        try:
            with open(sys.argv[1]) as f:
		        for line in f:
                    into_list = line.split()
                    whitespace = line.strip()

                    if len(into_list) == 0:
                        continue

                    try:
                        #
                        self.memory[address] = int(into_list[0], 2)

                    except ValueError:
                        print("Invalid number")
                        sys.exit(1)
                    
                    address += 1

        except FileNotFoundError:
            print(f'File not found: {sys.argv[1]}')
            sys.exit(2)

        # For now, we've just hardcoded a program:

        #program = [
        #    # From print8.ls8
        #    0b10000010, # LDI R0,8
        #    0b00000000,
        #    0b00001000,
        #    0b01000111, # PRN R0
        #    0b00000000,
        #    0b00000001, # HLT
        #    
        #]
#
        #for instruction in program:
        #    self.memory[address] = instruction
        #    address += 1
#

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        #need to use ram_read()/write?

        #0b00000001, aka "HLT" is basically 1
        while self.memory[self.pc] is not == 1:
            ir = self.memory[self.pc]

            #LDI = 0b10000010 = 82
            if ir == 82:
                reg_num = self.memory[self.pc + 1]
		        value = self.memory[self.pc + 2]
		        self.registers[reg_num] = value
		        self.pc += 3

            #PRN = 0b01000111 = 47
            if ir == 47:
                reg_num = self.memory[self.pc + 1]
		        print(self.registers[reg_num])
		        self.pc += 2

            else:
                print("invalid entry")

            

    def ram_read(self, MAR):
    """should accept the address to read & return the value stored there"""
        # memory address register
        return self.registers[MAR]

    def ram_write(self, MAR, MDR):
    """should accept a value to write, and the address to write it to"""
        # memory data register 
        # whatever was at MAR now has MDR as its value
        self.registers[MAR] = MDR
