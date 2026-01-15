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

