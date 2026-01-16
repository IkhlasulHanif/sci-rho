import random as rnd
import os
import matplotlib.pyplot as plt
from compsci.helper import *

# target folder : "root/dataset/compsci/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "compsci", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Com001:

    def __init__(self):
        self.decimal = rnd.randint(1, 255)
        self.answer = bin(self.decimal)[2:]

        self.description = (
            f"Convert the decimal number shown in the image to its binary form."
        )
        self.topic = "Data representation"
        self.subtopic = "Number systems"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Decimal number}} &= {self.decimal}\\\\"
            f"\\text{{To convert decimal to binary, we repeatedly divide by 2 and record the remainders:}} &\\\\"
            + "\\\\".join([
                f"{self.decimal // (2**i)} \\div 2 &= {self.decimal // (2**(i+1))} \\text{{ remainder }} {(self.decimal // (2**i)) % 2}"
                for i in range(len(bin(self.decimal)[2:]))
            ]) +
            f"\\\\"
            f"\\text{{Reading the remainders from bottom to top:}} &\\\\"
            f"\\text{{Binary}} &= {self.answer}_2"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots()
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        ax.text(500, 500, f"{self.decimal}₁₀ = ___₂", fontsize=24, color='black', fontweight='bold', ha='center', va='center')
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com002:

    def __init__(self):
        self.length = rnd.randint(1, 8)
        self.binary = generate_binary(self.length, allow_leading_zeros=False)
        self.decimal = int(self.binary, 2)
        self.answer = hex(self.decimal)[2:].upper()

        self.description = f"Convert the binary number shown in the image to its hexadecimal form."
        self.topic = "Data representation"
        self.subtopic = "Number systems"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Binary number}} &= {self.binary}_2\\\\"
            f"\\text{{1. Convert binary to decimal:}} &\\\\"
            f"\\text{{Decimal}} &= " + " + ".join([f"({self.binary[i]} \\times 2^{len(self.binary)-1-i})" for i in range(len(self.binary))]) + f"\\\\"
            f"&= " + " + ".join([f"{int(self.binary[i]) * (2**(len(self.binary)-1-i))}" for i in range(len(self.binary))]) + f"\\\\"
            f"&= {self.decimal}_{{10}}\\\\"
            f"\\text{{2. Convert decimal to hexadecimal:}} &\\\\"
            f"\\text{{Divide }} {self.decimal} \\text{{ by 16 and record remainders:}} &\\\\"
            + "\\\\".join([
                f"{self.decimal // (16**i) if i == 0 else (self.decimal // (16**i))} \\div 16 &= {self.decimal // (16**(i+1))} \\text{{ remainder }} {(self.decimal // (16**i)) % 16} \\rightarrow \\text{{HexDigit}}({hex((self.decimal // (16**i)) % 16)[2:].upper()})"
                for i in range(max(1, len(hex(self.decimal)[2:])))
            ]) +
            f"\\\\"
            f"\\text{{Hexadecimal}} &= {self.answer}_{{16}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots()
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        ax.text(500, 500, f"{self.binary}₂ = ___₁₆", fontsize=24, color='black', fontweight='bold', ha='center', va='center')
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com003:

    def __init__(self):
        self.decimal = rnd.randint(1, 255)
        self.hex = f"{self.decimal:02X}"
        self.answer = int(self.hex, 16)

        self.description = f"Convert the hexadecimal number shown in the image to its denary form."
        self.topic = "Data representation"
        self.subtopic = "Number systems"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Hexadecimal number}} &= {self.hex}_{{16}}\\\\"
            f"\\text{{To convert hexadecimal to denary, multiply each digit by its positional power of 16:}} &\\\\"
            f"\\text{{Value}} &= (d_1 \\times 16^1) + (d_0 \\times 16^0)\\\\"
            f"&= (\\text{{HexDigit}}({self.hex[0]}) \\times 16) + (\\text{{HexDigit}}({self.hex[1]}) \\times 1)\\\\"
            f"&= ({int(self.hex[0], 16)} \\times 16) + ({int(self.hex[1], 16)} \\times 1)\\\\"
            f"&= {int(self.hex[0], 16) * 16} + {int(self.hex[1], 16)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots()
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        ax.text(500, 500, f"{self.hex}₁₆ = ___₁₀", fontsize=20, color='black', fontweight='bold', ha='center', va='center')
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com004:

    def __init__(self):
        self.length = 8
        self.decimal_1 = rnd.randint(50, 255)
        self.decimal_2 = rnd.randint(210, 255)
        self.binary_1 = bin(self.decimal_1)[2:]
        self.binary_2 = bin(self.decimal_2)[2:]
        self.total_decimal = self.decimal_1 + self.decimal_2
        self.total_binary = format(self.total_decimal, '09b')
        self.overflow_bit = self.total_binary[0]
        self.binary_8bit = self.total_binary[1:]
        self.answer = int(self.binary_8bit, 2)

        self.description = f"If we calculate the sum of the two 8-bit unsigned binary numbers shown and store the result in a standard 8-bit register, what is the final decimal value after the Carry Out/overflow bit is discarded?"
        self.topic = "Data representation"
        self.subtopic = "Number systems"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Binary 1}} &= {self.binary_1.zfill(8)}_2\\\\"
            f"\\text{{Binary 2}} &= {self.binary_2.zfill(8)}_2\\\\"
            f"\\text{{Note: Column 1 is the rightmost side.}} &\\\\"
            f"\\text{{Perform 8-bit binary addition:}} &\\\\"
            f"\\begin{{array}}{{rcc}} & \\text{{Carry In}} & \\text{{Calculation}} \\\\ \\hline"
            + "\\\\".join([
                f"\\text{{Column }} {i+1} & "
                f"{((self.decimal_1 & ((1 << i) - 1)) + (self.decimal_2 & ((1 << i) - 1)) >> i) if i > 0 else 0} & "
                f"({self.binary_1.zfill(8)[7-i]} + {self.binary_2.zfill(8)[7-i]} + "
                f"{((self.decimal_1 & ((1 << i) - 1)) + (self.decimal_2 & ((1 << i) - 1)) >> i) if i > 0 else 0}) "
                f"\\rightarrow \\text{{Sum }} {self.total_binary[8-i]}"
                for i in range(8)
            ]) +
            f"\\\\ \\text{{Column 9}} & {((self.decimal_1 + self.decimal_2) >> 8) & 1} & \\text{{(Carry Out/Overflow)}} \\rightarrow \\text{{Sum }} {self.total_binary[0]}"
            f"\\end{{array}} &\\\\"
            f"\\text{{Full sum (9-bit)}} &= {self.total_binary}_2\\\\"
            f"\\text{{Carry out (Overflow)}} &= {self.total_binary[0]}_2\\\\"
            f"\\text{{8-bit Register Result}} &= {self.binary_8bit}_2\\\\"
            f"\\text{{Convert to Decimal:}} &\\\\"
            f"\\text{{Value}} &= " + " + ".join([f"({self.binary_8bit[i]} \\times 2^{7-i})" for i in range(8)]) + f"\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots()
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        plt.axis('off')

        ax.text(700, 530, self.binary_1.zfill(8), fontsize=26, ha='right')
        ax.text(700, 450, self.binary_2.zfill(8), fontsize=26, ha='right')
        ax.text(280, 450, "+", fontsize=26, ha='right')
        
        ax.plot([220, 740], [420, 420], color='black', lw=3)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

