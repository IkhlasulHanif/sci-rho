import random as rnd
import os
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
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

class Com005:

    def __init__(self):
        self.length = 7
        self.positive_binary = "0" + generate_binary(self.length, allow_leading_zeros=True)
        self.invert = "".join(["1" if bit == "0" else "0" for bit in self.positive_binary])
        result = []
        carry = 1
        for bit in reversed(self.invert):
            total = int(bit) + carry
            if total == 2:
                result.append("0")
                carry = 1
            elif total == 1:
                result.append("1")
                carry = 0
            else:
                result.append("0")
                carry = 0
        self.answer = "".join(reversed(result))

        self.description = f"Represent the binary numbers shown in the image into its negative form with two's complement."
        self.topic = "Data representation"
        self.subtopic = "Number systems"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial positive binary}} &= {self.positive_binary}_2\\\\"
            f"\\text{{Step 1: Invert all bits (One's Complement)}} &\\\\"
            f"\\text{{Original: }} & {self.positive_binary}\\\\"
            f"\\text{{Inverted: }} & {self.invert}\\\\"
            f"\\text{{Step 2: Add 1 to the least significant bit (Two's Complement)}} &\\\\"
            f"\\text{{Operation: }} & {self.invert}_2 + 1_2\\\\"
            + "\\\\".join([
                f"\\text{{Bit {i}: }} {self.invert[7-i]} + {1 if i==0 else 'carry(' + str(1 if int(self.invert[8-i]) + (1 if (i==1) else 0) >= 2 else 0) + ')'} \\rightarrow \\text{{Result }} {self.answer[7-i]}"
                for i in range(8)
            ]) + "\\\\"
            f"\\text{{Final Result (Two's Complement)}} &= {self.answer}_2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots()
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        plt.axis('off')

        ax.plot([180, 812], [450, 450], color='black', lw=3)
        ax.plot([180, 812], [600, 600], color='black', lw=3)
        ax.plot([180, 180], [450, 600], color='black', lw=3)

        gap = 0
        for bit in self.positive_binary:
            x = 200 + gap
            ax.text(x, 500, bit, fontsize=22)
            ax.plot([x + 60, x + 60], [450, 600], color='black', lw=3)
            gap = gap + 80

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com006:

    def __init__(self):
        self.type = "Odd"
        self.num_bytes = 7
        self.bytes = [generate_binary(length=7, allow_leading_zeros=True) for _ in range(self.num_bytes)]
        self.parity_bits = []
        for byte in self.bytes:
            ones_count = byte.count('1')
            p_bit = 1 if ones_count % 2 == 0 else 0
            self.parity_bits.append(p_bit)
        self.parity_byte = []
        for col_i in range(7):
            col_ones = sum(int(byte[col_i]) for byte in self.bytes)
            # To make the column odd:
            self.parity_byte.append(1 if col_ones % 2 == 0 else 0)
        self.parity_byte.insert(0, 1 if sum(self.parity_bits) % 2 == 0 else 0)

        self.target_byte_idx = rnd.randint(0, 6) # Which byte, 
        self.target_bit_idx = rnd.randint(0, 6) # which bit to be flipped
        self.row_sum = sum(int(bit) for bit in self.bytes[self.target_byte_idx]) + self.parity_bits[self.target_byte_idx]
        self.column_sum = sum(int(byte[self.target_bit_idx]) for byte in self.bytes) + self.parity_byte[self.target_bit_idx + 1]
        self.answer = self.row_sum + self.column_sum

        corrected_bits_list = list(self.bytes[self.target_byte_idx]) 
        corrected_col_list = [byte[self.target_bit_idx] for byte in self.bytes]
        
        target_byte = self.bytes[self.target_byte_idx]
        bit_list = list(target_byte)
        target_bit = bit_list[self.target_bit_idx]
        bit_list[self.target_bit_idx] = "1" if target_bit == "0" else "0"
        self.bytes[self.target_byte_idx] = "".join(bit_list)

        self.description = f"A sensor transmits data in a {self.num_bytes}x{self.num_bytes} block using {self.type} Parity. After identifying the corrupted bit in the data block below, and flip it to its correct value, what is the total sum of the bits in the corrected row and corrected column combined now?"
        self.topic = "Data transmission"
        self.subtopic = "Methods of error detection"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Parity Type}} &= \\text{{{self.type}}}\\\\"
            f"\\text{{1. Identify the corrupted bit:}} &\\\\"
            f"\\text{{In {self.type} parity, the total number of 1s in each row and column (including parity) must be odd.}} &\\\\"
            f"\\text{{Check Row Parity:}} &\\\\"
            f"\\text{{Byte }} {self.target_byte_idx + 1} \\text{{ has an even count of 1s, indicating an error in this row.}} &\\\\"
            f"\\text{{Check Column Parity:}} &\\\\"
            f"\\text{{Bit }} {self.target_bit_idx + 1} \\text{{ has an even count of 1s, indicating an error in this column.}} &\\\\"
            f"\\text{{The intersection of Byte }} {self.target_byte_idx + 1} \\text{{ and Bit }} {self.target_bit_idx + 1} \\text{{ identifies the corrupted bit.}} &\\\\"
            f"\\text{{2. Correct the corrupted bit:}} &\\\\"
            f"\\text{{The bit at this position is flipped to its opposite value to restore odd parity.}} &\\\\"
            f"\\text{{3. Calculate the sum of bits in the corrected row:}} &\\\\"
            f"\\text{{Row sum}} &= {' + '.join(corrected_bits_list)} + {self.parity_bits[self.target_byte_idx]}\\\\"
            # f"\\text{{Row sum}} &= " + " + ".join([f"{bit}" for bit in list(self.bytes[self.target_byte_idx])]) + f" + {self.parity_bits[self.target_byte_idx]}\\\\"
            f"&= {self.row_sum}\\\\"
            f"\\text{{4. Calculate the sum of bits in the corrected column:}} &\\\\"
            f"\\text{{Column sum}} &= {' + '.join(corrected_col_list)} + {self.parity_byte[self.target_bit_idx + 1]}\\\\"
            # f"\\text{{Column sum}} &= " + " + ".join([f"{byte[self.target_bit_idx]}" for byte in self.bytes]) + f" + {self.parity_byte[self.target_bit_idx + 1]}\\\\"
            f"&= {self.column_sum}\\\\"
            f"\\text{{5. Final combined sum:}} &\\\\"
            f"\\text{{Total}} &= \\text{{Row sum}} + \\text{{Column sum}}\\\\"
            f"&= {self.row_sum} + {self.column_sum}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 5))
        plt.axis('off')

        table_data = []
        for i, byte_str in enumerate(self.bytes):
            row = [f"Byte {i+1}"] + [str(self.parity_bits[i])] + list(byte_str)
            table_data.append(row)

        parity_row = ["Parity Byte"] + [str(b) for b in self.parity_byte]
        table_data.append(parity_row)

        headers = [""] + ["Parity Bit"] + [f"Bit {i+1}" for i in range(7)]
        
        table = ax.table(
            cellText=table_data,
            colLabels=headers,
            loc='center', 
            cellLoc='center'
        )

        table.auto_set_font_size(False)
        table.set_fontsize(14)
        table.scale(1.2, 2.0)

        for (row, col), cell in table.get_celld().items():
            cell.set_text_props(fontfamily='serif')
            cell.set_linewidth(0.5)

            if row == 0:
                cell.set_text_props(weight='bold')
                cell.set_facecolor('#f0f0f0')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()
        
class Com007:

    def __init__(self):
        self.elements = rnd.randint(7, 9)
        self.array = [rnd.randint(1, 100) for _ in range(self.elements)]
        self.target = rnd.choice([self.array[rnd.randint(0, len(self.array) - 1)], rnd.randint(50, 125)])
        self.found = False
        index = 0
        result = -1
        while (index < self.elements) and self.found == False:
            if self.array[index] == self.target:
                self.found = True
                result = index
            else:
                index = index + 1
        self.answer = result

        self.description = f"This image is showing a pseudocode for a searching algorithm. If the target (x) is set to {self.target}, what is the final output displayed?"
        self.topic = "Algorithm design and problem-solving"
        self.subtopic = "Understand standard methods of solution"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial Array}} &= [{', '.join(map(str, self.array))}]\\\\"
            f"\\text{{Target Value}} &= {self.target}\\\\"
            f"\\text{{Linear Search Logic:}} &\\\\"
            + "\\\\".join([
                f"\\text{{Step {i+1}: Check index }} {i} \\text{{ (Value: }} {self.array[i]} \\text{{)}} &\\rightarrow " + 
                (f"\\text{{Match found! (Stop searching)}}" if self.array[i] == self.target else f"\\text{{No match, move to index }} {i+1}")
                for i in range(self.answer + 1 if self.found else self.elements)
            ]) + "\\\\"
            f"\\text{{Search Outcome:}} &\\\\"
            + (f"\\text{{Found target at index }} {self.answer}" if self.found else f"\\text{{Target not found in array, output is }} -1") + "\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        pseudocode = [
            f"DECLARE Numbers : ARRAY[0:{len(self.array)}] OF INTEGER",
            "DECLARE Target : INTEGER",
            "DECLARE Index : INTEGER",
            "DECLARE Result : INTEGER",
            "DECLARE Found : BOOLEAN",
            "",
            f"Numbers <- {self.array}",
            "Target <- x",
            "Found <- FALSE",
            "Index <- 0",
            "Result <- -1",
            "",
            f"WHILE Index < {len(self.array)} AND Found = FALSE",
            "    IF Numbers[Index] = Target THEN",
            "        Found <- TRUE",
            "        Result <- Index",
            "    ELSE",
            "        Index <- Index + 1",
            "    END IF",
            "END WHILE",
            "",
            "OUTPUT Result"
        ]
        
        fig, ax = plt.subplots(figsize=(8, 10))
        plt.axis('off')
        
        y_pos = 0.95
        line_height = 0.035
                
        for line in pseudocode:
            color = 'black'
            weight = 'normal'
            
            ax.text(0.05, y_pos, line, 
                    fontsize=14, 
                    family='monospace', 
                    verticalalignment='top', 
                    color=color, 
                    weight=weight)
            
            y_pos -= line_height

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com008:

    def __init__(self):
        self.days = 7
        self.steps = [rnd.randint(3000, 7000) for _ in range(self.days)]
        self.total_steps = 0
        for day in range(self.days):
            self.total_steps += self.steps[day]
        self.average = self.total_steps / self.days
        count_above_avg = 0
        for day in range(self.days):
            if self.steps[day] > self.average:
                count_above_avg += 1
        self.answer = count_above_avg

        self.description = f"A person is measuring the number of their walking steps for each day of the week: {self.steps}. According to this pseudocode shown below, what is the final output displayed?"
        self.topic = "Algorithm design and problem-solving"
        self.subtopic = "Understand standard methods of solution"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Daily steps (S)}} &= [{', '.join(map(str, self.steps))}]\\\\"
            f"\\text{{1. Calculate Total Steps:}} &\\\\"
            f"\\Sigma S &= " + " + ".join(map(str, self.steps)) + f"\\\\"
            f"&= {self.total_steps}\\\\"
            f"\\text{{2. Calculate Average Steps (A):}} &\\\\"
            f"A &= \\frac{{\\Sigma S}}{{\\text{{days}}}}\\\\"
            f"&= \\frac{{{self.total_steps}}}{{{self.days}}}\\\\"
            f"&= {round(self.average, 10)}\\\\"
            f"\\text{{3. Identify days above average:}} &\\\\"
            + "\\\\".join([
                f"\\text{{Day }} {i+1} \\text{{ ({self.steps[i]})}} &> {round(self.average, 10)} \\rightarrow " + 
                ("\\text{{True}}" if self.steps[i] > self.average else "\\text{{False}}")
                for i in range(self.days)
            ]) + "\\\\"
            f"\\text{{4. Final Count:}} &\\\\"
            f"\\text{{CountAbove}} &= {self.answer}\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com008temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com009:

    def __init__(self):
        self.elements = 6
        self.array = [rnd.randint(20, 150) for _ in range(self.elements)]
        self.array_copy = self.array.copy()
        self.steps = []
        swap_count = 0
        for i in range(self.elements-1):
            for j in range(0, self.elements - i - 1):
                a = self.array[j]
                b = self.array[j + 1]

                did_swap = False
                if a > b:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swap_count += 1
                    did_swap = True

                self.steps.append({
                    "pass": i + 1,
                    "j": j,
                    "a": a,
                    "b": b,
                    "swap": did_swap,
                    "array": self.array.copy()
                })
        self.answer = swap_count

        self.description = f"This image is showing a pseudocode for a sorting algorithm. Given the unsorted array of numbers, how many swaps will it take to sort the data?"
        self.topic = "Algorithm design and problem-solving"
        self.subtopic = "Understand standard methods of solution"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial array (Data)}} &= [{', '.join(map(str, self.array_copy))}]\\\\"
            "\\text{The bubble sort algorithm compares adjacent elements and swaps them if they are in the wrong order.}\\\\"
            + "\\\\".join(
                (f"\\text{{Pass }} {p}: &\\\\"
                + "\\\\".join(
                    f"\\text{{Compare }} {s['a']} \\text{{ and }} {s['b']} \\rightarrow "
                    + (
                        f"\\text{{Swap! Array: }} [{', '.join(map(str, s['array']))}]"
                        if s["swap"] else "\\text{{No swap}}"
                    )
                    for s in self.steps if s["pass"] == p
                )
                for p in range(1, self.elements))
            ) + "\\\\"
            f"\\text{{Total number of swaps performed (SwapCount)}} &= {self.answer}\\\\"
            f"\\text{{Final sorted array}} &= [{', '.join(map(str, self.array))}]\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com009temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        pseudocode = [
            f"DECLARE Data : ARRAY[0:{self.elements}] OF INTEGER",
            "DECLARE N, I, J, Temp, SwapCount : INTEGER",
            "",
            # f"Data <- {self.array_copy}",
            f"N <- Number of Data Elements",
            "SwapCount <- 0",
            "",
            "FOR I <- 0 TO N - 2",
            "    FOR J <- 0 TO N - I - 2",
            "        IF Data[J] > Data[J + 1] THEN",
            "            Temp <- Data[J]",
            "            Data[J] <- Data[J + 1]",
            "            Data[J + 1] <- Temp",
            "            ",
            "            SwapCount <- SwapCount + 1",
            "        END IF",
            "    NEXT J",
            "NEXT I",
            "",
            # "OUTPUT \"Sorted array: \", Data",
            "OUTPUT \"Total swaps: \", SwapCount"
        ]
        
        y_pos = 0.96
        line_height = 0.042
                
        keywords = ["DECLARE", "ARRAY", "OF", "INTEGER", "<-", "FOR", "TO", "IF", "THEN", "ENDIF", "NEXT", "OUTPUT"]
        for line in pseudocode:
            words = line.split(' ')
            x_pos = 0.07
            char_width = 0.011
            
            for word in words:
                if word == "":
                    x_pos += char_width 
                    continue
                    
                clean_word = word.strip("[]:,")
                
                if clean_word in keywords:
                    word_color = 'orange'
                else:
                    word_color = 'white'

                word_weight = 'normal'

                ax.text(x_pos, y_pos, word, 
                        fontsize=5.8, 
                        family='monospace', 
                        verticalalignment='top', 
                        color=word_color, 
                        weight=word_weight,
                        transform=ax.transAxes)
                
                x_pos += (len(word) + 1) * char_width

            y_pos -= line_height  

        values = self.array_copy
        n = self.elements

        x = 0.76
        y_top = 0.90
        box_w = 0.135
        box_h = 0.135

        for i, val in enumerate(values):
            y1 = y_top - i * box_h
            y0 = y1 - box_h

            xs = [x, x + box_w, x + box_w, x]
            ys = [y0, y0, y1, y1]
            ax.fill(xs, ys, transform=ax.transAxes, color="#fffca8", zorder=5)

            ax.plot([x, x + box_w, x + box_w, x, x], [y0, y0, y1, y1, y0], transform=ax.transAxes, color="white", linewidth=2, zorder=6)

            if i < n - 1:
                ax.plot([x, x + box_w], [y0, y0],
                        transform=ax.transAxes, color="white", linewidth=2, zorder=7)

            ax.text(x + box_w/2, (y0 + y1)/2, str(val),
                    transform=ax.transAxes, ha="center", va="center",
                    fontsize=12, family="monospace", color="black", zorder=8)  

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com010:

    def __init__(self):
        self.N = rnd.randint(5, 8)
        self.N_copy = self.N
        self.steps = []
        total = 0
        
        while (self.N > 0):
            total_before = total
            if self.N % 2 == 0:
                added = self.N
            else:
                added = 2 * self.N
            total += added
            self.steps.append((self.N, total_before, added, total))
            self.N = self.N - 1
        self.answer = total

        self.description = f"A flowchart for a program is given in the image below. What is the final value of total, if input N is {self.N_copy}?"
        self.topic = "Algorithm design and problem-solving"
        self.subtopic = "Understand standard methods of solution"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial Input }} N &= {self.N_copy}\\\\"
            f"\\text{{Initial }} \\text{{total}} &= 0\\\\"
            f"\\text{{The program executes a loop while }} N > 0: \\\\"
            + "\\\\".join(
                [
                    f"\\text{{Iteration }} {i}: \\\\"
                    f"N &= {n}\\\\"
                    f"\\text{{Condition: }} {n} \\% 2 == 0 \\rightarrow "
                    + ("\\text{{True}}" if n % 2 == 0 else "\\text{{False}}") + "\\\\"
                    f"\\text{{Update: }} \\text{{total}} = {t_before} + "
                    + (f"{n}" if n % 2 == 0 else f"2 \\times {n}")
                    + f" = {t_after}\\\\"
                    f"\\text{{Next }} N &= {n} - 1 = {n-1}"
                    for i, (n, t_before, added, t_after) in enumerate(self.steps, 1)
                ]
            )
            + f"\\\\\\text{{Final }} \\text{{total}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com010temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com011:

    def __init__(self):
        self.elements = 16
        self.array = rnd.sample(range(20, 100), self.elements)
        self.current_idx = rnd.randint(0, 7)
        self.target_idx = rnd.randint(8, 15)
        self.current = self.array[self.current_idx]
        self.target = self.array[self.target_idx]
        self.found = False
        index = self.current_idx + 1
        compare_counter = 0
        while (index < self.elements) and self.found == False:
            compare_counter += 1
            if self.array[index] == self.target:
                self.found = True
            else:
                index = index + 1
        self.answer = compare_counter

        self.description = f"A searching algorithm is used to find a target value (y) in an array (x). The pseudocode for the algorithm is shown in the image below. If we start the next comparison from the current position, how many comparisons are made including the comparison where the target value is found?"
        self.topic = "Algorithm design and problem-solving"
        self.subtopic = "Understand standard methods of solution"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial search index}} &= i = {self.current_idx + 1}\\\\"
            f"\\text{{Target value to find}} &= T = {self.target}\\\\"
            "\\text{{Step-by-step comparisons:}} &\\\\"
            + "\\\\".join([
                f"\\text{{Step {c+1}: Compare Array}}[{self.current_idx + 1 + c}] ({self.array[self.current_idx + 1 + c]}) \\text{{ with }} {self.target} \\rightarrow " + 
                (f"\\text{{Match!}}" if self.array[self.current_idx + 1 + c] == self.target else f"\\text{{No match}}")
                for c in range(self.answer)
            ]) + "\\\\"
            f"\\text{{Total comparisons made}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        bg_color = "#fcfaef"
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        plt.axis('off')

        ax.plot([20, 980], [970, 970], color='black', lw=3)
        ax.plot([20, 980], [880, 880], color='black', lw=3)
        ax.plot([20, 20], [880, 970], color='black', lw=3)

        gap = 0
        for i, value in enumerate(self.array):
            x = 36 + gap

            is_current = (i == self.current_idx)
            is_target  = (i == self.target_idx)

            color = 'red' if (is_current or is_target) else 'black'

            if is_current:
                ax.text(x - 17, 835, "current", fontsize=11, color='red', weight='bold')
            elif is_target:
                ax.text(x - 12, 835, "target", fontsize=11, color='red', weight='bold')

            ax.text(x, 910, str(value), fontsize=16, color=color)
            ax.plot([x + 45, x + 45], [880, 970], color='black', lw=3)
            gap += 60

        pseudocode = [
            f"DECLARE Numbers : ARRAY[0:{self.elements}] OF INTEGER",
            "DECLARE Target : INTEGER",
            "DECLARE Index : INTEGER",
            "DECLARE CompareCounter : INTEGER",
            "DECLARE Found : BOOLEAN",
            "",
            "Numbers <- x",
            "Target <- y",
            "",
            "Found <- FALSE",
            "Index <- CurrentIndex + 1",
            "CompareCounter <- 0",
            "",
            f"WHILE Index < {self.elements} AND Found = FALSE",
            "    CompareCounter <- CompareCounter + 1",
            "    IF Numbers[Index] = Target THEN",
            "        Found <- TRUE",
            "    ELSE",
            "        Index <- Index + 1",
            "    END IF",
            "END WHILE",
            "",
            "OUTPUT CompareCounter"
        ]

        y_pos = 780
        line_height = 40
                
        for line in pseudocode:
            color = 'black'
            weight = 'normal'
            
            ax.text(30, y_pos, line, 
                    fontsize=12, 
                    family='monospace', 
                    verticalalignment='top', 
                    color=color, 
                    weight=weight)
            
            y_pos -= line_height

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close()

class Com012:
    
    def __init__(self):
        self.n = rnd.randint(6, 12)
        total = 0
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                if i % 3 == 0:
                    total = total + 3
                else:
                    total = total + 1
            else:
                if i > 5:
                    total = total + 2
        self.answer = total

        self.description = f"Here is an image showing a simple Python program. If we give the input = {self.n}, what will be the printed total value?"
        self.topic = "Programming"
        self.subtopic = "Programming concepts"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Input }} n &= {self.n}\\\\"
            f"\\text{{Initial total}} &= 0\\\\"
            f"\\text{{Iterating through }} i \\text{{ from 1 to }} {self.n}:\\\\"
            + "\\\\".join([
                f"i = {i}: & \\quad " + (
                    f"i \\text{{ is even, }}" + (
                        f"i \\text{{ is divisible by 3}} \\rightarrow \\text{{total}} = {sum([ (3 if j % 6 == 0 else 1) if j % 2 == 0 else (2 if j > 5 else 0) for j in range(1, i)])} + 3 = {sum([ (3 if j % 6 == 0 else 1) if j % 2 == 0 else (2 if j > 5 else 0) for j in range(1, i+1)])}"
                        if i % 3 == 0 else
                        f"i \\text{{ is not divisible by 3}} \\rightarrow \\text{{total}} = {sum([ (3 if j % 6 == 0 else 1) if j % 2 == 0 else (2 if j > 5 else 0) for j in range(1, i)])} + 1 = {sum([ (3 if j % 6 == 0 else 1) if j % 2 == 0 else (2 if j > 5 else 0) for j in range(1, i+1)])}"
                    ) if i % 2 == 0 else
                    f"i \\text{{ is odd, }}" + (
                        f"i > 5 \\rightarrow \\text{{total}} = {sum([ (3 if j % 6 == 0 else 1) if j % 2 == 0 else (2 if j > 5 else 0) for j in range(1, i)])} + 2 = {sum([ (3 if j % 6 == 0 else 1) if j % 2 == 0 else (2 if j > 5 else 0) for j in range(1, i+1)])}"
                        if i > 5 else
                        f"i \\leq 5 \\rightarrow \\text{{total stays }} {sum([ (3 if j % 6 == 0 else 1) if j % 2 == 0 else (2 if j > 5 else 0) for j in range(1, i)])}"
                    )
                )
                for i in range(1, self.n + 1)
            ]) +
            f"\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com012temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com013:

    def __init__(self):
        self.length = rnd.randint(5, 10)
        self.input_text = ''.join(chr(rnd.randint(65, 75)) for _ in range(self.length))
        self.input_ch = chr(rnd.randint(66, 75))
        self.text = self.input_text.lower()
        self.ch = self.input_ch.lower()
        self.steps = []
        count = 0
        for i in range(self.length):
            char = self.text[i]
            total_before = count
            if char == self.ch or char == "a":
                change = 6
                is_match = True
            else:
                change = -2
                is_match = False
            count += change
            self.steps.append((i, char, is_match, total_before, change, count))
        self.answer = count

        self.description = f"This image is showing a simple string handling code. If input s is \"{self.text}\" and input c is \"{self.ch}\", what will be printed as the output of this code?"
        self.topic = "Programming"
        self.subtopic = "Programming concepts"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Original Input: }} s &= \"{self.input_text}\",\\, c = '{self.input_ch}'\\\\"
            f"\\text{{Processed (Lowercase): }} s &= \"{self.text}\",\\, c = '{self.ch}'\\\\"
            f"\\text{{Initial count}} &= 0\\\\"
            "\\text{{Condition: }} (\\text{{char}} == '{self.ch}') \\lor (\\text{{char}} == 'a')\\\\"
            "\\text{{Iterating through the string:}}\\\\"
            + "\\\\".join(
                [
                    f"\\text{{Step }} {idx+1}: \\text{{ char }} '{char}' \\\\"
                    f"('{char}' == '{self.ch}') \\lor ('{char}' == 'a') &\\rightarrow "
                    + ("\\text{{True (+6)}}" if match else "\\text{{False (-2)}}") + "\\\\"
                    f"\\text{{count}} &= {t_before} + ({change}) = {t_after}"
                    for idx, char, match, t_before, change, t_after in self.steps
                ]
            )
            + f"\\\\\\text{{Final Output}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com013temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com014:

    def __init__(self):
        self.length = 9
        self.input = [rnd.randint(2, 11) for _ in range(self.length)]
        self.grid = []
        i = 0
        for r in range(3):
            row = []
            for c in range(3):
                row.append(self.input[i])
                i += 1
            self.grid.append(row)

        result = 0
        for r in range(3):
            for c in range(3):
                if r == c:
                    result += self.grid[r][c] * 2

        self.answer = result

        self.description = f"The given image contains a Python code involving two-dimensional array. What will the final result be, if the input is {self.input}?"
        self.topic = "Programming"
        self.subtopic = "Arrays"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The program reads 9 integers to fill a }} 3 \\times 3 \\text{{ grid.}}\\\\"
            f"\\text{{Input list (read in order): }} [a_1, a_2, \\dots, a_9] = {self.input}\\\\"
            f"\\text{{Grid mapping:}}\\\\"
            f"\\begin{{bmatrix}} g_{{0,0}} & g_{{0,1}} & g_{{0,2}} \\\\ g_{{1,0}} & g_{{1,1}} & g_{{1,2}} \\\\ g_{{2,0}} & g_{{2,1}} & g_{{2,2}} \\end{{bmatrix}} &= "
            f"\\begin{{bmatrix}} {self.input[0]} & {self.input[1]} & {self.input[2]} \\\\ {self.input[3]} & {self.input[4]} & {self.input[5]} \\\\ {self.input[6]} & {self.input[7]} & {self.input[8]} \\end{{bmatrix}}\\\\"
            f"\\text{{The code adds only diagonal entries (where }} r=c \\text{{), each multiplied by 2.}}\\\\"
            f"\\text{{So the accumulated result is:}}\\\\"
            f"\\text{{result}} &= \\sum_{{r=0}}^2 \\sum_{{c=0}}^2 \\mathbf{{1}}_{{r=c}}\\,(2\\,g_{{r,c}})\\\\"
            f"&= 2\\,(g_{{0,0}} + g_{{1,1}} + g_{{2,2}})\\\\"
            f"&= 2\\,(a_1 + a_5 + a_9)\\\\"
            f"&= 2\\,({self.input[0]} + {self.input[4]} + {self.input[8]})\\\\"
            f"&= 2\\,({round(self.input[0] + self.input[4] + self.input[8], 10)})\\\\"
            f"&= {round(2 * (self.input[0] + self.input[4] + self.input[8]), 10)}\\\\"
            f"\\text{{Final result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        img = Image.open('compsci/temp_image/Com014temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com015:

    def __init__(self):
        self.length = 12
        self.items_threshold = rnd.randint(3, 5)
        self.total_threshold = rnd.randrange(30, 60, 5)
        self.items = [1, 4, 3, 2, 5, 2, 6, 1, 3, 2, 4, 2]
        self.totals = [25, 80, 45, 60, 110, 40, 150, 15, 75, 35, 95, 55]
        count = 0
        for i in range(self.length):
            if (self.items[i] < self.items_threshold) and (self.totals[i] >= self.total_threshold):
                count += 1
        self.answer = count

        self.description = f"Sales data from an online shop is stored in a table called Orders, as shown in the image. The owner runs the query: SELECT COUNT(OrderID) FROM Orders WHERE Items < {self.items_threshold} AND Total >= {self.total_threshold};. What should be the output?"
        self.topic = "Databases"
        self.subtopic = "Understand structured query language scripts (custom subtopic)"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Query conditions: Items}} &< {self.items_threshold} \\text{{ AND Total}} \\ge {self.total_threshold}\\\\"
            f"\\text{{Thresholds: Items threshold}} &= {self.items_threshold}, \\text{{ Total threshold}} = {self.total_threshold}\\\\"
            f"\\text{{Evaluating each row:}} &\\\\"
            + "\\\\".join([
                f"\\text{{Row {i+1}: (Items={self.items[i]}, Total={self.totals[i]})}} \\rightarrow "
                f"({self.items[i]} < {self.items_threshold}) \\text{{ AND }} ({self.totals[i]} \\ge {self.total_threshold}) \\rightarrow "
                f"({'True' if self.items[i] < self.items_threshold else 'False'}) \\text{{ AND }} ({'True' if self.totals[i] >= self.total_threshold else 'False'}) \\rightarrow "
                f"\\text{{{'Match' if (self.items[i] < self.items_threshold and self.totals[i] >= self.total_threshold) else 'No Match'}}}"
                for i in range(self.length)
            ]) + "\\\\"
            f"\\text{{Total matching records (COUNT)}} &= {self.answer}\\\\"
            f"\\text{{Final result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com015temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com016:

    def __init__(self):
        self.length = 12
        self.query_type = rnd.choice(['L0456', 'L0457', 'L0458'])
        self.types = ['L0456', 'L0457', 'L0458', 'L0456', 'L0457', 'L0458', 'L0456', 'L0457', 'L0458', 'L0456', 'L0458', 'L0456']
        self.quantities = [rnd.randint(2, 9) for _ in range(self.length)]
        sum = 0
        for i in range(self.length):
            if self.types[i] == self.query_type:
                sum += self.quantities[i]
        self.answer = sum

        self.description = f"The following table in the image shows laptop sales made in January 2025. What value is output by the SQL statement below it, if x is {self.query_type}?"
        self.topic = "Databases"
        self.subtopic = "Understand structured query language scripts (custom subtopic)"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Query Condition: LaptopType}} &= \\text{{{self.query_type}}}\\\\"
            f"\\text{{SQL Operation: }} & \\text{{SUM(Quantity)}}\\\\"
            f"\\text{{Evaluating records in table:}} &\\\\"
            + "\\\\".join([
                f"\\text{{Row {i+1}: }} ({self.types[i]}, {self.quantities[i]}) \\rightarrow " + 
                (f"\\text{{Match! Add }} {self.quantities[i]}" if self.types[i] == self.query_type else "\\text{{No Match}}")
                for i in range(self.length)
            ]) + "\\\\"
            f"\\text{{Summation calculation:}} &\\\\"
            f"\\text{{Total}} &= " + " + ".join([str(self.quantities[i]) for i in range(self.length) if self.types[i] == self.query_type]) + f"\\\\"
            f"&= {self.answer}\\\\"
            f"\\text{{Final result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com016temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        y_pos = 100
        line_height = 35
                
        for qty in self.quantities:
            color = 'black'
            weight = 'normal'
            
            ax.text(512, y_pos, str(qty), 
                    fontsize=10, 
                    color=color,
                    family="sans-serif",
                    weight=weight)
            
            y_pos += line_height

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com017:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.answer = int(not(not self.input_1 and not self.input_2))
        
        self.description = f"Given this image of a logic circuit, determine the output of OUT1 if IN1 is {self.input_1} and IN2 is {self.input_2}."
        self.topic = "Boolean logic"
        self.subtopic = "Logic circuits"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Input 1 (IN1)}} &= {self.input_1}\\\\"
            f"\\text{{Input 2 (IN2)}} &= {self.input_2}\\\\"
            f"\\text{{1. Process through first layer (NOT gates):}} &\\\\"
            f"A &= \\neg \\text{{IN1}} = {int(not self.input_1)}\\\\"
            f"B &= \\neg \\text{{IN2}} = {int(not self.input_2)}\\\\"
            f"\\text{{2. Process through second layer (AND gate):}} &\\\\"
            f"C &= A \\wedge B = {int(not self.input_1)} \\wedge {int(not self.input_2)} = {int(not self.input_1 and not self.input_2)}\\\\"
            f"\\text{{3. Process through final layer (NOT gate):}} &\\\\"
            f"\\text{{OUT1}} &= \\neg C = \\neg({int(not self.input_1 and not self.input_2)})\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        img = Image.open('compsci/temp_image/Com017temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com018:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.answer = int(not((not(self.input_1 or self.input_1)) or (not(self.input_2 or self.input_2))))
        
        self.description = f"Given this image of a logic circuit, determine the output of Z if Input A is {self.input_1} and B is {self.input_2}."
        self.topic = "Boolean logic"
        self.subtopic = "Logic circuits"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Input A}} &= {self.input_1}\\\\"
            f"\\text{{Input B}} &= {self.input_2}\\\\"
            f"\\text{{1. Analyze the first stage (NOR gates acting as NOT gates):}} &\\\\"
            f"\\text{{NOT A}} &= \\neg(A \\lor A) = \\neg({self.input_1} \\lor {self.input_1}) = {int(not self.input_1)}\\\\"
            f"\\text{{NOT B}} &= \\neg(B \\lor B) = \\neg({self.input_2} \\lor {self.input_2}) = {int(not self.input_2)}\\\\"
            f"\\text{{2. Analyze the second stage (NOR gate):}} &\\\\"
            f"\\text{{Output Z}} &= \\neg(\\text{{NOT A}} \\lor \\text{{NOT B}})\\\\"
            f"&= \\neg({int(not self.input_1)} \\lor {int(not self.input_2)})\\\\"
            f"&= \\neg({int(not self.input_1 or not self.input_2)})\\\\"
            f"&= {int(self.answer)}\\\\"
            f"\\text{{Note: By De Morgan's Law, }} \\neg(\\neg A \\lor \\neg B) \\iff A \\land B &\\\\"
            f"\\text{{Final result Z}} &= {int(self.answer)}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        img = Image.open('compsci/temp_image/Com018temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com019:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.answer = int(not((not(self.input_1 or self.input_2)) or (not(self.input_1 or self.input_2))))
        
        self.description = f"Given this image of a logic circuit, what is the output of Z if Input X is {self.input_1} and Y is {self.input_2}?"
        self.topic = "Boolean logic"
        self.subtopic = "Logic circuits"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Input X}} &= {self.input_1}\\\\"
            f"\\text{{Input Y}} &= {self.input_2}\\\\"
            f"\\text{{1. Analyze the first stage (NOR gate):}} &\\\\"
            f"\\text{{Intermediate Output (A)}} &= \\neg(X \\lor Y)\\\\"
            f"&= \\neg({self.input_1} \\lor {self.input_2})\\\\"
            f"&= {int(not(self.input_1 or self.input_2))}\\\\"
            f"\\text{{2. Analyze the second stage (NOR gate acting as a NOT gate):}} &\\\\"
            f"\\text{{Output Z}} &= \\neg(A \\lor A)\\\\"
            f"&= \\neg({int(not(self.input_1 or self.input_2))} \\lor {int(not(self.input_1 or self.input_2))})\\\\"
            f"&= {self.answer}\\\\"
            f"\\text{{Summary: The circuit simplifies to (X OR Y) using two NOR gates.}} &\\\\"
            f"\\text{{Final Result Z}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        img = Image.open('compsci/temp_image/Com019temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com020:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.input_3 = rnd.choice([0, 1])
        self.answer = int(((self.input_1 or self.input_2) and self.input_3) or (self.input_1 and self.input_2))
        
        self.description = f"Given this image of a logic circuit, what is the output of F if Input A is {self.input_1}, B is {self.input_2}, and C is {self.input_3}?"
        self.topic = "Boolean logic"
        self.subtopic = "Logic circuits"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Inputs: }} A &= {self.input_1}, B = {self.input_2}, C = {self.input_3} \\\\"
            f"\\text{{1. Analyze the first OR gate (A OR B):}} & \\\\"
            f"G_1 &= A \\lor B \\\\"
            f"&= {self.input_1} \\lor {self.input_2} \\\\"
            f"&= {int(self.input_1 or self.input_2)} \\\\"
            f"\\text{{2. Analyze the first AND gate (G1 AND C):}} & \\\\"
            f"G_2 &= G_1 \\land C \\\\"
            f"&= {int(self.input_1 or self.input_2)} \\land {self.input_3} \\\\"
            f"&= {int((self.input_1 or self.input_2) and self.input_3)} \\\\"
            f"\\text{{3. Analyze the second AND gate (A AND B):}} & \\\\"
            f"G_3 &= A \\land B \\\\"
            f"&= {self.input_1} \\land {self.input_2} \\\\"
            f"&= {int(self.input_1 and self.input_2)} \\\\"
            f"\\text{{4. Analyze the final OR gate (G2 OR G3):}} & \\\\"
            f"F &= G_2 \\lor G_3 \\\\"
            f"&= {int((self.input_1 or self.input_2) and self.input_3)} \\lor {int(self.input_1 and self.input_2)} \\\\"
            f"&= {self.answer} \\\\"
            f"\\text{{Final Output F}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        img = Image.open('compsci/temp_image/Com020temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com021:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.input_3 = rnd.choice([0, 1])
        self.answer = int((not((not self.input_1) and self.input_2)) or ((not self.input_2) and self.input_3))
        
        self.description = f"Given this image of a logic circuit, what is the output of F if Input A is {self.input_1}, B is {self.input_2}, and C is {self.input_3}?"
        self.topic = "Boolean logic"
        self.subtopic = "Logic circuits"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Inputs: }} A &= {self.input_1}, B = {self.input_2}, C = {self.input_3} \\\\"
            f"\\text{{1. Analyze the first branch:}} & \\\\"
            f"\\text{{Let }} G_1 &= \\neg A \\land B \\\\"
            f"&= \\neg({self.input_1}) \\land {self.input_2} \\\\"
            f"&= {int(not self.input_1)} \\land {self.input_2} \\\\"
            f"&= {int((not self.input_1) and self.input_2)} \\\\"
            f"G_2 &= \\neg G_1 \\\\"
            f"&= \\neg({int((not self.input_1) and self.input_2)}) \\\\"
            f"&= {int(not((not self.input_1) and self.input_2))} \\\\"
            f"\\text{{2. Analyze the second branch (Lower logic):}} & \\\\"
            f"G_3 &= \\neg B \\land C \\\\"
            f"&= \\neg({self.input_2}) \\land {self.input_3} \\\\"
            f"&= {int(not self.input_2)} \\land {self.input_3} \\\\"
            f"&= {int((not self.input_2) and self.input_3)} \\\\"
            f"\\text{{3. Final Output (OR operation):}} & \\\\"
            f"F &= G_2 \\lor G_3 \\\\"
            f"&= {int(not((not self.input_1) and self.input_2))} \\lor {int((not self.input_2) and self.input_3)} \\\\"
            f"&= {self.answer} \\\\"
            f"\\text{{Final Result }} F &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com021temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com022:

    def __init__(self):
        self.BCD = [bin(rnd.randint(0, 9))[2:].zfill(4) for _ in range(3)]
        self.digits = [int(b, 2) for b in self.BCD] 
        self.answer = int("".join(map(str, self.digits)))  

        self.description = f"This image is displaying a BCD (Binary Coded Decimal). Convert the BCD to its decimal representation."
        self.topic = "Information representation"
        self.subtopic = "Data representation"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{BCD Input Sequence:}} & \\text{{ [{', '.join([b.zfill(4) for b in self.BCD])}]}} \\\\"
            f"\\text{{1. Convert each 4-bit Binary group to a Decimal digit:}} & \\\\"
            + "\\\\".join([
                f"\\text{{Group {i+1} (}}{self.BCD[i].zfill(4)}\\text{{)}} &= " + 
                " + ".join([f"({self.BCD[i].zfill(4)[j]} \\times 2^{3-j})" for j in range(4)]) + 
                f" = {self.digits[i]}"
                for i in range(len(self.BCD))
            ]) + "\\\\"
            f"\\text{{2. Concatenate the decimal digits:}} & \\\\"
            f"\\text{{Decimal}} &= " + "".join(map(str, self.digits)) + " \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots()
        plt.axis('off')
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)

        ax.text(180, 600, f"{self.BCD[0]} {self.BCD[1]} {self.BCD[2]}", fontsize=25, color='green', fontweight='bold')
        arrow_x_coords = [250, 470, 690]
        for x in arrow_x_coords:
            ax.text(x, 490, "↓", fontsize=28, color='green', fontweight='bold')
        
        box_width = 80
        box_height = 110
        top_y = 345

        for x in arrow_x_coords:
            rect = patches.Rectangle(
                (x-10, top_y),
                box_width, 
                box_height, 
                linewidth=2, 
                edgecolor='green', 
                facecolor='none'
            )
            ax.add_patch(rect)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com023:

    def __init__(self):
        self.length = 8
        self.decimal_1 = rnd.randint(150, 255)
        self.decimal_2 = rnd.randint(1, 149)
        self.binary_1 = bin(self.decimal_1)[2:]
        self.binary_2 = bin(self.decimal_2)[2:]
        self.total_decimal = self.decimal_1 - self.decimal_2
        self.total_binary = format(self.total_decimal, '08b')
        self.answer = self.total_decimal

        self.description = f"Find the subtraction of these two 8-bit numbers (shown in the image) in the form of decimal value."
        self.topic = "Information representation"
        self.subtopic = "Data representation"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Binary 1 (Minuend)}} &= {self.binary_1.zfill(8)}_2 ({self.decimal_1}_{{10}})\\\\"
            f"\\text{{Binary 2 (Subtrahend)}} &= {self.binary_2.zfill(8)}_2 ({self.decimal_2}_{{10}})\\\\"
            f"\\text{{Binary Subtraction Rules:}} &\\\\"
            f"0 - 0 &= 0\\\\"
            f"1 - 0 &= 1\\\\"
            f"1 - 1 &= 0\\\\"
            f"0 - 1 &= 1 \\text{{ (with a borrow of 1 from the next column)}}\\\\"
            f"\\text{{Step-by-step subtraction (from right to left):}} &\\\\"
            f"\\begin{{array}}{{rcc}} & \\text{{Borrow In}} & \\text{{Calculation (Bit1 - Bit2 - Borrow)}} \\\\ \\hline"
            + "\\\\".join([
                f"\\text{{Column }} {i+1} & "
                f"{(1 if (self.decimal_1 % (2**(i+1))) < (self.decimal_2 % (2**(i+1))) else 0)} & "
                f"({self.binary_1.zfill(8)[7-i]} - {self.binary_2.zfill(8)[7-i]} - "
                f"{(1 if (self.decimal_1 % (2**i)) < (self.decimal_2 % (2**i)) else 0)}) "
                f"\\rightarrow \\text{{Bit }} {self.total_binary[7-i]}"
                for i in range(8)
            ]) +
            f"\\end{{array}} &\\\\"
            f"\\text{{Final Binary Result}} &= {self.total_binary}_2\\\\"
            f"\\text{{Convert binary to decimal:}} &\\\\"
            f"\\text{{Value}} &= " + " + ".join([f"({self.total_binary[i]} \\times 2^{7-i})" for i in range(8)]) + f"\\\\"
            f"&= {round(float(self.total_decimal), 10)}\\\\"
            f"\\text{{The final answer is }} {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots()
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        plt.axis('off')

        ax.text(700, 530, self.binary_1.zfill(8), fontsize=26, ha='right')
        ax.text(700, 450, self.binary_2.zfill(8), fontsize=26, ha='right')
        ax.text(280, 450, "-", fontsize=26, ha='right')
        
        ax.plot([220, 740], [420, 420], color='black', lw=3)
       
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com024:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.input_3 = rnd.choice([0, 1])
        self.answer = (not(self.input_1 or self.input_2)) ^ self.input_3
        
        self.description = f"A computer scientist has created the following logic circuit shown in this image. What is the output of P if Input A is given {self.input_1}, B is given {self.input_2}, and C is given {self.input_3}?"
        self.topic = "Hardware"
        self.subtopic = "Logic Gates and Logic Circuits"
        self.source = "Adapted from OCR H446/01 12 June 2023"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Inputs: }} A &= {self.input_1}, B = {self.input_2}, C = {self.input_3} \\\\"
            "\\text{{1. Analyze the first stage (NOR gate):}} & \\\\"
            "Q &= \\neg(A \\lor B) \\\\"
            f"&= \\neg({self.input_1} \\lor {self.input_2}) \\\\"
            f"&= \\neg({int(self.input_1 or self.input_2)}) \\\\"
            f"&= {int(not(self.input_1 or self.input_2))} \\\\"
            "\\text{{2. Analyze the final stage (XOR gate):}} & \\\\"
            "P &= Q \\oplus C \\\\"
            f"&= {int(not(self.input_1 or self.input_2))} \\oplus {self.input_3} \\\\"
            f"&= {int(self.answer)} \\\\"
            f"\\text{{Final Result P}} &= {int(self.answer)}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com024temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com025:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.S = self.input_1 ^ self.input_2
        self.C = self.input_1 and self.input_2
        self.concatenated = str(self.S) + str(self.C)
        self.answer = int(self.concatenated, 2)
        
        self.description = f"The diagram shows a logic circuit where D0 will be given the input {self.input_1} and D1 will be given the input {self.input_2}. The circuit produces outputs S and C, which are concatenated to form a two-bit binary number with S as the most significant bit. Convert this two-bit binary number into its decimal value and state this as the final answer."
        self.topic = "Hardware"
        self.subtopic = "Logic Gates and Logic Circuits"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Input }} D_0 &= {self.input_1} \\\\"
            f"\\text{{Input }} D_1 &= {self.input_2} \\\\"
            "\\text{{1. Calculate S (Sum) using XOR logic:}} & \\\\"
            "S &= D_0 \\oplus D_1 \\\\"
            f"&= {self.input_1} \\oplus {self.input_2} \\\\"
            f"&= {self.S} \\\\"
            "\\text{{2. Calculate C (Carry) using AND logic:}} & \\\\"
            "C &= D_0 \\wedge D_1 \\\\"
            f"&= {self.input_1} \\wedge {self.input_2} \\\\"
            f"&= {int(self.C)} \\\\"
            "\\text{{3. Form the two-bit binary number (S as MSB):}} & \\\\"
            f"\\text{{Binary}} &= (S, C)_2 \\\\"
            f"&= ({self.S}{int(self.C)})_2 \\\\"
            "\\text{{4. Convert binary to decimal:}} & \\\\"
            f"\\text{{Value}} &= (S \\times 2^1) + (C \\times 2^0) \\\\"
            f"&= ({self.S} \\times 2) + ({int(self.C)} \\times 1) \\\\"
            f"&= {self.answer} \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com025temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com026:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.input_3 = rnd.choice([0, 1])
        self.S = (self.input_1 ^ self.input_2) ^ self.input_3
        self.C = ((self.input_1 ^ self.input_2) and self.input_3) or (self.input_1 and self.input_2)
        self.concatenated = str(self.S) + str(self.C)
        self.answer = int(self.concatenated, 2)
        
        self.description = f"The diagram shows a logic circuit where X is given the input {self.input_1}, Y is given the input {self.input_2} and Z is given the input {self.input_3}. The circuit produces outputs S and C, which are concatenated to form a two-bit binary number with S as the most significant bit. Convert this two-bit binary number into its decimal value and state this as the final answer."
        self.topic = "Hardware"
        self.subtopic = "Logic Gates and Logic Circuits"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Inputs: }} X &= {self.input_1}, Y = {self.input_2}, Z = {self.input_3} \\\\"
            "\\text{{1. Calculate S (Sum) using XOR logic:}} & \\\\"
            "S &= (X \\oplus Y) \\oplus Z \\\\"
            f"&= ({self.input_1} \\oplus {self.input_2}) \\oplus {self.input_3} \\\\"
            f"&= {int(self.input_1 ^ self.input_2)} \\oplus {self.input_3} \\\\"
            f"&= {self.S} \\\\"
            "\\text{{2. Calculate C (Carry) using logic:}} & \\\\"
            "C &= ((X \\oplus Y) \\land Z) \\lor (X \\land Y) \\\\"
            f"&= (({self.input_1} \\oplus {self.input_2}) \\land {self.input_3}) \\lor ({self.input_1} \\land {self.input_2}) \\\\"
            f"&= ({int(self.input_1 ^ self.input_2)} \\land {self.input_3}) \\lor {int(self.input_1 and self.input_2)} \\\\"
            f"&= {int((self.input_1 ^ self.input_2) and self.input_3)} \\lor {int(self.input_1 and self.input_2)} \\\\"
            f"&= {int(self.C)} \\\\"
            "\\text{{3. Form the two-bit binary number (S as MSB):}} & \\\\"
            "\\text{{Binary}} &= (S, C)_2 \\\\"
            f"&= ({self.S}{int(self.C)})_2 \\\\"
            "\\text{{4. Convert binary to decimal:}} & \\\\"
            "\\text{{Value}} &= (S \\times 2^1) + (C \\times 2^0) \\\\"
            f"&= ({self.S} \\times 2) + ({int(self.C)} \\times 1) \\\\"
            f"&= {int(str(self.S) + str(int(self.C)), 2)} \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com026temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com027:

    def __init__(self):
        self.temp_threshold = 80
        self.pressure_threshold = 200
        self.RPM_threshold = 5000
        self.temp = rnd.randint(70, 90)
        self.pressure = rnd.randint(190, 210)
        self.RPM = rnd.randint(4900, 5100)
        self.input_A = 1 if self.temp > self.temp_threshold else 0
        self.input_B = 1 if self.pressure > self.pressure_threshold else 0
        self.input_C = 1 if self.RPM > self.RPM_threshold else 0
        self.answer = int(((not(self.input_C)) or self.input_B) and self.input_A)

        self.description = (f"The figure given below shows a logic circuit that gives a warning light to the pilot of an aircraft depending on the engine conditions. The warning light becomes ON when there is a HIGH (1) level at output W." 
                            f"The temperature sensor outputs HIGH when temperature > {self.temp_threshold}°C. The pressure sensor outputs HIGH when pressure > {self.pressure_threshold} kPa. The RPM sensor outputs HIGH when RPM > {self.RPM_threshold} rpm. "
                            f"If the measured values are: Temperature = {self.temp}°C, Pressure = {self.pressure} kPa, RPM = {self.RPM} rpm, determine the state of the warning light W (0 or 1).")
        self.topic = "Hardware"
        self.subtopic = "Logic Gates and Logic Circuits"
        self.source = "Adapted from Chegg"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Determine input states from sensor values:}} &\\\\"
            f"\\text{{Input A (Temperature)}} &= ({self.temp} > {self.temp_threshold}) \\rightarrow {self.input_A}\\\\"
            f"\\text{{Input B (Pressure)}} &= ({self.pressure} > {self.pressure_threshold}) \\rightarrow {self.input_B}\\\\"
            f"\\text{{Input C (RPM)}} &= ({self.RPM} > {self.RPM_threshold}) \\rightarrow {self.input_C}\\\\"
            f"\\text{{2. Analyze the logic circuit gates:}} &\\\\"
            f"\\text{{The RPM input (C) passes through a NOT gate:}} &\\\\"
            f"\\text{{NOT C}} &= \\neg {self.input_C} = {int(not self.input_C)}\\\\"
            f"\\text{{The output of the NOT gate and Pressure (B) enter an OR gate:}} &\\\\"
            f"\\text{{OR Output}} &= (\\neg C \\lor B) = ({int(not self.input_C)} \\lor {self.input_B}) = {int(not self.input_C or self.input_B)}\\\\"
            f"\\text{{The OR output and Temperature (A) enter an AND gate for the final output W:}} &\\\\"
            f"W &= ((\\neg C \\lor B) \\land A)\\\\"
            f"&= ({int(not self.input_C or self.input_B)} \\land {self.input_A})\\\\"
            f"&= {self.answer}\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com027temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com028:

    def __init__(self):
        self.input_1 = rnd.choice([0, 1])
        self.input_2 = rnd.choice([0, 1])
        self.input_3 = rnd.choice([0, 1])
        self.answer = int((self.input_1 ^ self.input_3) or (not(self.input_2 and (not(self.input_3)))))

        self.description = f"Here is an image of a logic circuit where input A = {self.input_1}, input B = {self.input_2}, and input C = {self.input_3}. Based on the circuit shown, what is the final output X?"
        self.topic = "Hardware"
        self.subtopic = "Logic Gates and Logic Circuits"
        self.source = "Adapted from PapaCambridge 1.3.1 Logic Gates"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Inputs: }} A &= {self.input_1}, B = {self.input_2}, C = {self.input_3} \\\\"
            "\\text{{1. Analyze the XOR gate (Inputs A and C):}} & \\\\"
            "G_1 &= A \\oplus C \\\\"
            f"&= {self.input_1} \\oplus {self.input_3} \\\\"
            f"&= {int(self.input_1 ^ self.input_3)} \\\\"
            "\\text{{2. Analyze the lower branch (Inputs B and C):}} & \\\\"
            f"\\text{{NOT C}} &= \\neg C = \\neg({self.input_3}) = {int(not self.input_3)} \\\\"
            "G_2 &= B \\land (\\neg C) \\\\"
            f"&= {self.input_2} \\land {int(not self.input_3)} \\\\"
            f"&= {int(self.input_2 and (not self.input_3))} \\\\"
            "\\text{{3. Analyze the NAND logic in the lower branch:}} & \\\\"
            "G_3 &= \\neg G_2 \\\\"
            f"&= \\neg({int(self.input_2 and (not self.input_3))}) \\\\"
            f"&= {int(not (self.input_2 and (not self.input_3)))} \\\\"
            "\\text{{4. Analyze the final OR gate (G1 or G3):}} & \\\\"
            "X &= G_1 \\lor G_3 \\\\"
            f"&= {int(self.input_1 ^ self.input_3)} \\lor {int(not (self.input_2 and (not self.input_3)))} \\\\"
            f"&= {self.answer} \\\\"
            f"\\text{{Final Result X}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com028temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com029:

    def __init__(self):
        self.input_1 = rnd.randint(10, 20)
        self.input_2 = rnd.randint(1, self.input_1-1)
        self.subtract = self.input_1 - self.input_2
        self.add = self.subtract + 3
        if self.add == 7:
            self.answer = 0
        else:
            self.answer = self.add

        self.description = f"The following image shows a sequence of assembly language instructions. Given the inputs {self.input_1} (for the first IN) and {self.input_2} (for the second IN), trace the execution of the program then state the value of the final output."
        self.topic = "Processor Fundamentals"
        self.subtopic = "Assembly Language"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Input Phase:}} & \\\\"
            f"\\text{{First input (IN) stored at address 100:}} & \\quad \\text{{[100]}} = {self.input_1} \\\\"
            f"\\text{{Second input (IN) stored at address 101:}} & \\quad \\text{{[101]}} = {self.input_2} \\\\"
            f"\\text{{2. Arithmetic Operations:}} & \\\\"
            f"\\text{{Load value from 100:}} & \\quad \\text{{ACC}} = {self.input_1} \\\\"
            f"\\text{{Subtract value from 101:}} & \\quad \\text{{ACC}} = {self.input_1} - {self.input_2} = {self.subtract} \\\\"
            f"\\text{{Add immediate value 3:}} & \\quad \\text{{ACC}} = {self.subtract} + 3 = {self.add} \\\\"
            f"\\text{{3. Conditional Branching:}} & \\\\"
            f"\\text{{Compare ACC with 7 (CMP \#7):}} & \\quad {self.add} = 7? \\\\"
            + (f"\\text{{Condition is True: Jump not taken (JPN), load 0 to ACC.}} & \\quad \\text{{ACC}} = 0 \\\\" if self.add == 7 else 
            f"\\text{{Condition is False: Jump to OUT (address 31) is taken.}} & \\quad \\text{{ACC}} = {self.add} \\\\") +
            f"\\text{{4. Output:}} & \\\\"
            f"\\text{{Final value of ACC is printed:}} & \\quad \\text{{OUT}} = {self.answer} \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com029temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com030:
    
    def __init__(self):
        self.length = 5
        self.input = rnd.randint(5, 35)
        self.array = [10, 12, 23, 19, self.input]
        sum = 0
        for i in range(self.length):
            sum += self.array[i]
        self.answer = sum

        self.description = f"The following image shows a sequence of assembly language instructions. Given the input {self.input}, trace the execution of the program then state the value of the final output."
        self.topic = "Processor Fundamentals"
        self.subtopic = "Assembly Language"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Initializing Memory and Inputs:}} & \\\\"
            f"\\text{{Input value }} (IN) &= {self.input} \\\\"
            f"\\text{{Store input at address 304:}} & \\quad \\text{{[304]}} = {self.input} \\\\"
            f"\\text{{Initialize sum at 310:}} & \\quad \\text{{[310]}} = 0 \\\\"
            f"\\text{{Initialize counter at 311:}} & \\quad \\text{{[311]}} = 0 \\\\"
            f"\\text{{Address 300-303:}} & \\quad [10, 12, 23, 19] \\\\"
            f"\\text{{2. Trace Loop Execution (5 iterations):}} & \\\\"
            f"\\text{{Iteration 1: }} IX=0, \\text{{ ACC}} = [300] = 10, \\text{{ Sum}} = 0 + 10 = 10 \\\\"
            f"\\text{{Iteration 2: }} IX=1, \\text{{ ACC}} = [301] = 12, \\text{{ Sum}} = 10 + 12 = 22 \\\\"
            f"\\text{{Iteration 3: }} IX=2, \\text{{ ACC}} = [302] = 23, \\text{{ Sum}} = 22 + 23 = 45 \\\\"
            f"\\text{{Iteration 4: }} IX=3, \\text{{ ACC}} = [303] = 19, \\text{{ Sum}} = 45 + 19 = 64 \\\\"
            f"\\text{{Iteration 5: }} IX=4, \\text{{ ACC}} = [304] = {self.input}, \\text{{ Sum}} = 64 + {self.input} = {self.answer} \\\\"
            f"\\text{{3. Final Output:}} & \\\\"
            f"\\text{{Exit loop when counter reaches 5, load sum from 310, and output.}} & \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com030temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com031:

    def __init__(self):
        self.length = 13
        self.health_scores = [72, 44, 12, 45, 43, 90, 39, 50, 46, 44, 48, 45, 49]
        self.increase = rnd.randint(4, 12)
        self.threshold = rnd.randint(32, 51)
        self.updated_health_scores = [self.health_scores[i] + self.increase if self.health_scores[i] < self.threshold else self.health_scores[i] for i in range(self.length)]
        self.answer = sum(self.updated_health_scores)

        self.description = (
            f"The table 'plant_shipment' stores details about plant shipments. A database administrator runs the following SQL statement: "
            f"UPDATE plant_shipment "
            f"SET health_score = health_score + {self.increase} "
            f"WHERE health_score < {self.threshold};"
            f"After the query is executed, calculate the total (sum) of the `health_score` column."
        )
        self.topic = "Databases"
        self.subtopic = "Data Definition Language (DDL) and Data Manipulation Language (DML)"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial health scores}} &= [{', '.join(map(str, self.health_scores))}]\\\\"
            f"\\text{{Update criteria}} &: \\text{{If health score}} < {self.threshold}, \\text{{add }} {self.increase}\\\\"
            f"\\text{{Step 1: Evaluate and update each score:}} &\\\\"
            + "\\\\".join([
                f"\\text{{Score }} {i+1} ({self.health_scores[i]}) &: " + 
                (f"{self.health_scores[i]} < {self.threshold} \\rightarrow {self.health_scores[i]} + {self.increase} = {self.updated_health_scores[i]}" 
                if self.health_scores[i] < self.threshold else 
                f"{self.health_scores[i]} \\not< {self.threshold} \\rightarrow {self.health_scores[i]}")
                for i in range(self.length)
            ]) + "\\\\"
            f"\\text{{Step 2: Calculate the total sum of updated scores:}} &\\\\"
            f"\\text{{Total}} &= " + " + ".join(map(str, self.updated_health_scores)) + "\\\\"
            f"&= {self.answer}\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com031temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com032:

    def __init__(self):
        self.length = 12
        self.duration_min = [rnd.randint(18, 50) for _ in range(self.length)]
        self.central_park_group_avg = np.mean(self.duration_min[0:3])
        self.riverside_group_avg = np.mean(self.duration_min[3:6])
        self.downtown_group_avg = np.mean(self.duration_min[6:])
        self.answer = round(self.central_park_group_avg + self.riverside_group_avg + self.downtown_group_avg, 2)

        self.description = (
            f"The table bike_rental stores data about bike rentals, including the station used, the type of user, and the duration of each rental in minutes. The following SQL query is executed: \n"
            f"SELECT SUM(avg_duration) AS sum_of_group_averages\n"
            f"FROM (\n"
            f"SELECT user_type, AVG(duration_min) AS avg_duration \n"
            f"FROM bike_rental \n"
            f"GROUP BY station_name \n"
            f") group_averages;\n"
            f"Using the data shown in the table, determine the output of this query. Round the answer to two decimal places."
        )
        self.topic = "Databases"
        self.subtopic = "Data Definition Language (DDL) and Data Manipulation Language (DML)"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Group by station and calculate individual averages:}} & \\\\"
            f"\\text{{Central Park Group: }} [ {', '.join(map(str, self.duration_min[0:3]))} ] \\rightarrow \\mu_1 &= \\frac{{{sum(self.duration_min[0:3])}}}{{3}} = {round(self.central_park_group_avg, 10)} \\\\"
            f"\\text{{Riverside Group: }} [ {', '.join(map(str, self.duration_min[3:6]))} ] \\rightarrow \\mu_2 &= \\frac{{{sum(self.duration_min[3:6])}}}{{3}} = {round(self.riverside_group_avg, 10)} \\\\"
            f"\\text{{Downtown Group: }} [ {', '.join(map(str, self.duration_min[6:]))} ] \\rightarrow \\mu_3 &= \\frac{{{sum(self.duration_min[6:])}}}{{6}} = {round(self.downtown_group_avg, 10)} \\\\"
            f"\\text{{2. Calculate the sum of these group averages:}} & \\\\"
            f"S &= \\mu_1 + \\mu_2 + \\mu_3 \\\\"
            f"&= {round(self.central_park_group_avg, 10)} + {round(self.riverside_group_avg, 10)} + {round(self.downtown_group_avg, 10)} \\\\"
            f"&= {self.answer} \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com032temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        y_pos = 100
        line_height = 35
                
        for duration in self.duration_min:
            color = "#2A2A2A"
            weight = 'normal'
            
            ax.text(718, y_pos, str(duration), 
                    fontsize=8, 
                    color=color,
                    family="sans-serif",
                    weight=weight)
            
            y_pos += line_height

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com033:

    def __init__(self):
        self.number = rnd.randint(100, 999999)
        self.temp = str(self.number)
        self.num_length = len(self.temp)
        total = 0
        for i in range(self.num_length):
            total += int(self.temp[i])
        self.answer = total % 10

        self.description = f"A doCheck() function takes an integer value as a parameter, carries out a series of calculations and returns an integer value. The function is shown in this image. State the value returned from the function when doCheck({self.number}) is called."
        self.topic = "Algorithm Design and Problem-solving"
        self.subtopic = "Algorithms"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Input Parameter (number)}} &= {self.number}\\\\"
            f"\\text{{1. Convert number to string (temp):}} & \\quad \\text{{temp}} = \"{self.temp}\"\\\\"
            f"\\text{{2. Identify digits and calculate sum (total):}} &\\\\"
            + " \\\\ ".join([f"\\text{{Digit }} {i} &= {self.temp[i]}" for i in range(self.num_length)]) + "\\\\"
            f"\\text{{total}} &= \\sum_{{i=0}}^{{{self.num_length - 1}}} \\text{{digit}}_i\\\\"
            f"&= {' + '.join([self.temp[i] for i in range(self.num_length)])}\\\\"
            f"&= {sum(int(d) for d in self.temp)}\\\\"
            f"\\text{{3. Perform MOD 10 calculation:}} &\\\\"
            f"\\text{{Result}} &= \\text{{total}} \\pmod{{10}}\\\\"
            f"&= {sum(int(d) for d in self.temp)} \\pmod{{10}}\\\\"
            f"&= {self.answer}\\\\"
            f"\\text{{Final return value}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        pseudocode = [
            "function doCheck(number)",
            "    temp = str(number)",
            "    max = temp.length - 1",
            "    total = 0",
            "    for x = 0 to max",
            "        total = total + int(temp.subString(x, 1))",
            "    next x",
            "    return total MOD 10",
            "endfunction"
        ]
        
        fig, ax = plt.subplots(figsize=(6, 4))
        plt.axis('off')
        
        y_pos = 0.95
        line_height = 0.08
                
        for line in pseudocode:
            color = 'black'
            weight = 'normal'
            
            ax.text(0.05, y_pos, line, 
                    fontsize=14, 
                    family='monospace', 
                    verticalalignment='top', 
                    color=color, 
                    weight=weight)
            
            y_pos -= line_height

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com034:

    def __init__(self):
        self.input_1 = rnd.randint(1, 50)
        self.input_2 = rnd.randint(1, 50)
        self.input_3 = rnd.randint(1, 50)
        if (self.input_1 >= self.input_2 and self.input_1 >= self.input_3):
            self.ans = self.input_1
        elif self.input_2 >= self.input_3:
            self.ans = self.input_2
        else:
            self.ans = self.input_3
        self.avg = (self.input_1 + self.input_2 + self.input_3) / 3
        self.answer = round(self.ans - self.avg, 2)

        self.description = f"A program is being developed. An algorithm for part of the program is shown in the given image below. The algorithm will input three numeric values and assign them to identifiers Num1, Num2 and Num3. If the input are {self.input_1}, {self.input_2}, and {self.input_3}, what will be displayed as the final output? Round the answer to two decimal places."
        self.topic = "Algorithm Design and Problem-solving"
        self.subtopic = "Algorithms"
        self.source = "Adapted from CAIE COMPUTER SCIENCE 9618/22 Paper 2 Fundamental Problem-solving and Programming Skills May/June 2024"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Inputs: }} \\text{{Num1}} &= {self.input_1}, \\text{{Num2}} = {self.input_2}, \\text{{Num3}} = {self.input_3}\\\\"
            f"\\text{{1. Determine the maximum value (ans):}} &\\\\"
            f"\\text{{If (Num1}} \\ge \\text{{Num2 AND Num1}} \\ge \\text{{Num3): ans}} &= \\text{{Num1}}\\\\"
            f"\\text{{Else if (Num2}} \\ge \\text{{Num3): ans}} &= \\text{{Num2}}\\\\"
            f"\\text{{Else: ans}} &= \\text{{Num3}}\\\\"
            f"\\text{{Substituting values: }} \\text{{ans}} &= {self.ans}\\\\"
            f"\\text{{2. Calculate the average (avg):}} &\\\\"
            f"\\text{{avg}} &= \\frac{{\\text{{Num1}} + \\text{{Num2}} + \\text{{Num3}}}}{{3}}\\\\"
            f"&= \\frac{{{self.input_1} + {self.input_2} + {self.input_3}}}{{3}}\\\\"
            f"&= \\frac{{{self.input_1 + self.input_2 + self.input_3}}}{{3}}\\\\"
            f"&= {round(self.avg, 10)}\\\\"
            f"\\text{{3. Calculate final output:}} &\\\\"
            f"\\text{{Output}} &= \\text{{ans}} - \\text{{avg}}\\\\"
            f"&= {self.ans} - {round(self.avg, 10)}\\\\"
            f"&= {self.answer}\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com034temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com035:

    def __init__(self):
        self.initial_num_elements = rnd.randint(2, 4)
        self.initial_stack_elements = rnd.sample(range(6, 50), self.initial_num_elements)
        stack = self.initial_stack_elements.copy()
        stack.pop()
        self.answer = stack[-1]

        self.description = f"The diagram shows a stack containing the following values. A pop() operation is carried out on the stack. What is the value at the top of the stack after this operation?"
        self.topic = "Data Types and Structures"
        self.subtopic = "Introduction to Abstract Data Types (ADT)"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial stack (bottom to top)}} &= [{', '.join(map(str, self.initial_stack_elements))}] \\\\"
            f"\\text{{Current top of the stack}} &= {self.initial_stack_elements[-1]} \\\\"
            f"\\text{{Perform pop() operation:}} & \\\\"
            f"\\text{{Value removed}} &= {self.initial_stack_elements[-1]} \\\\"
            f"\\text{{Updated stack (bottom to top)}} &= [{', '.join(map(str, self.initial_stack_elements[:-1]))}] \\\\"
            f"\\text{{New top of the stack}} &= \\text{{stack}}[-1] \\\\"
            f"&= {self.answer} \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig_w, fig_h = 3.0, max(3.2, 0.9 * self.initial_num_elements + 1.2)
        fig, ax = plt.subplots(figsize=(fig_w, fig_h))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

        x_left, x_right = 2.0, 8.0
        y_bottom, y_top = 1.3, 9.2
        n = self.initial_num_elements

        # Stack container (two sides + base)
        ax.plot([x_left, x_left], [y_bottom, y_top], linewidth=3, color="black")
        ax.plot([x_right, x_right], [y_bottom, y_top], linewidth=3, color="black")
        ax.plot([x_left, x_right], [y_bottom, y_bottom], linewidth=3, color="black")

        # Element boxes
        inner_margin = 0.6
        box_x = x_left + inner_margin
        box_w = (x_right - x_left) - 2 * inner_margin

        # Vertical layout
        available_h = (y_top - y_bottom) - 1.0
        gap = 0.35
        box_h = (available_h - gap * (n - 1)) / n
        start_y = y_bottom + 0.5

        # Draw from bottom -> top (last element is the top)
        for i, value in enumerate(self.initial_stack_elements):
            y = start_y + i * (box_h + gap)
            rect = patches.Rectangle((box_x, y), box_w, box_h, facecolor="#f7ead7", edgecolor="#e3b27a", linewidth=1.5,)
            ax.add_patch(rect)
            ax.text(box_x + box_w / 2, y + box_h / 2, str(value), ha="center", va="center", fontsize=18, fontweight="bold", color="black",)

        ax.text((x_left + x_right) / 2, y_bottom - 0.55, "Stack", ha="center", va="top", fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com036:

    def __init__(self):
        self.stack_length = 10
        self.filled_length = rnd.randint(4, 9)
        self.values = [rnd.randint(100, 400) for _ in range(self.filled_length)]
        stack = self.values.copy()
        stack.pop()
        self.push_1 = rnd.randint(100, 400)
        self.push_2 = rnd.randint(100, 400)
        stack.append(self.push_1)
        stack.append(self.push_2)
        self.answer = self.filled_length

        self.description = f"The diagram shows a stack implemented using an array, where top stores the index of the current top element. A pop() operation is carried out, followed by push({self.push_1}) and then push({self.push_2}). What is the value of top after these operations?"
        self.topic = "Data Types and Structures"
        self.subtopic = "Introduction to Abstract Data Types (ADT)"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial number of elements}} &= {self.filled_length}\\\\"
            f"\\text{{Initial top index (0-indexed)}} &= {self.filled_length - 1}\\\\"
            f"\\text{{1. Perform pop() operation:}} &\\\\"
            f"\\text{{New count}} &= {self.filled_length} - 1 = {self.filled_length - 1}\\\\"
            f"\\text{{New top index}} &= {self.filled_length - 1} - 1 = {self.filled_length - 2}\\\\"
            f"\\text{{2. Perform push({self.push_1}) operation:}} &\\\\"
            f"\\text{{New count}} &= {self.filled_length - 1} + 1 = {self.filled_length}\\\\"
            f"\\text{{New top index}} &= {self.filled_length - 2} + 1 = {self.filled_length - 1}\\\\"
            f"\\text{{3. Perform push({self.push_2}) operation:}} &\\\\"
            f"\\text{{New count}} &= {self.filled_length} + 1 = {self.filled_length + 1}\\\\"
            f"\\text{{New top index}} &= {self.filled_length - 1} + 1 = {self.filled_length}\\\\"
            f"\\text{{Final index value of top}} &= {self.answer}\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig_w = max(9, self.stack_length * 1.05)
        fig_h = 3
        fig, ax = plt.subplots(figsize=(fig_w, fig_h))
        ax.axis("off")

        top_index = self.filled_length - 1

        cell_w = 1.0
        cell_h = 0.7
        left = 0.5
        bottom = 1.4

        ax.set_xlim(0, left + self.stack_length * cell_w + 0.5)
        ax.set_ylim(0, 3.2)

        # Title
        ax.text(left + (self.stack_length * cell_w) / 2, bottom + 1.3, "Stack", ha="center", va="bottom", fontsize=14)

        for i in range(self.stack_length):
            x = left + i * cell_w
            y = bottom

            ax.add_patch(patches.Rectangle((x, y), cell_w, cell_h, fill=False, linewidth=1.5))

            ax.text(x + cell_w / 2, y + cell_h + 0.15, str(i), ha="center", va="center", fontsize=11)

            # Value (only if filled)
            if i < self.filled_length:
                ax.text(x + cell_w / 2, y + cell_h / 2, str(self.values[i]), ha="center", va="center", fontsize=11)

        top_box_w = 1.0
        top_box_h = 0.55
        top_box_x = left
        top_box_y = 0.25

        ax.text(top_box_x, top_box_y + top_box_h + 0.1, "top", ha="left", va="bottom", fontsize=11)
        ax.add_patch(patches.Rectangle((top_box_x, top_box_y), top_box_w, top_box_h, fill=False, linewidth=1.2))
        ax.text(top_box_x + top_box_w / 2, top_box_y + top_box_h / 2, str(top_index), ha="center", va="center", fontsize=12)
    
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com037:

    def __init__(self):
        self.size = 10
        self.queue = rnd.sample(range(1, 50), self.size)
        front = 0
        self.dequeued = self.queue[front]
        self.current_front = self.queue[front + 1]
        self.answer = self.current_front

        self.description = f"The diagram shows a queue implemented using an array. One dequeue() operation is carried out. What value is now at the front of the queue?"
        self.topic = "Data Types and Structures"
        self.subtopic = "Introduction to Abstract Data Types (ADT)"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial Queue}} &= [{', '.join(map(str, self.queue))}]\\\\"
            f"\\text{{Initial Front Index}} &= 0\\\\"
            f"\\text{{Initial Front Value}} &= {self.dequeued}\\\\"
            f"\\text{{1. Perform dequeue() operation:}} &\\\\"
            f"\\text{{Value removed from the front}} &= {self.dequeued}\\\\"
            f"\\text{{2. Update front pointer:}} &\\\\"
            f"\\text{{New Front Index}} &= \\text{{front}} + 1 = 1\\\\"
            f"\\text{{3. Identify value at new front index:}} &\\\\"
            f"\\text{{New Front Value}} &= \\text{{queue}}[1]\\\\"
            f"&= {self.answer}\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.axis("off")

        cell_w = 1.2
        cell_h = 0.8
        left = 0.6
        bottom = 1.3

        for i in range(self.size):
            x = left + i * cell_w
            y = bottom

            ax.add_patch(patches.Rectangle((x, y), cell_w, cell_h, fill=False, linewidth=1.5))
            ax.text(x + cell_w / 2, y + cell_h / 2, str(self.queue[i]), ha="center", va="center", fontsize=12, fontweight="bold", color="black")

        front_x = left + (0 * cell_w) + cell_w / 2
        front_label_y = bottom - 0.65

        ax.annotate("", xy=(front_x, bottom), xytext=(front_x, front_label_y + 0.2), arrowprops=dict(arrowstyle="->", linewidth=2.5, color="red"))
        ax.text(front_x, front_label_y, "FRONT", ha="center", va="top", fontsize=11, fontweight="bold", bbox=dict(boxstyle="square,pad=0.25", fc="white", ec="black", lw=1))

        rear_x = left + ((self.size - 1) * cell_w) + cell_w / 2
        rear_label_y = bottom - 0.65

        ax.annotate("", xy=(rear_x, bottom), xytext=(rear_x, rear_label_y + 0.2), arrowprops=dict(arrowstyle="->", linewidth=2.5, color="red"))
        ax.text(rear_x, rear_label_y, "REAR", ha="center", va="top", fontsize=11, fontweight="bold", bbox=dict(boxstyle="square,pad=0.25", fc="white", ec="black", lw=1))

        ax.set_xlim(0, left + self.size * cell_w + 0.6)
        ax.set_ylim(0, 3.0)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com038:

    def __init__(self):
        self.queue_max_length = 10
        self.filled_length = rnd.randint(4, 8)
        self.values = rnd.sample(range(50, 300), self.filled_length)
        self.enq_1 = rnd.randint(50, 300)
        self.enq_2 = rnd.randint(50, 300)

        arr = [None] * self.queue_max_length
        for i, v in enumerate(self.values):
            arr[i] = v

        front = 0
        rear = self.filled_length - 1

        # enqueue enq_1
        rear += 1
        arr[rear] = self.enq_1
        # dequeue
        arr[front] = None
        front += 1
        # enqueue enq_2
        rear += 1
        arr[rear] = self.enq_2

        self.answer = sum(v for v in arr if v is not None)

        self.description = f"The diagram shows an implementation of queue ADT. The operations enqueue({self.enq_1}), dequeue, and then enqueue({self.enq_2}) are carried out in that order. What is the sum of all values currently stored in the queue after these operations?"
        self.topic = "Data Types and Structures"
        self.subtopic = "Introduction to Abstract Data Types (ADT)"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial queue values}} &= [{', '.join(map(str, self.values))}] \\\\"
            f"\\text{{Initial sum}} &= {sum(self.values)} \\\\"
            f"\\text{{1. enqueue({self.enq_1}):}} & \\\\"
            f"\\text{{Add }} {self.enq_1} \\text{{ to the rear of the queue.}} & \\\\"
            f"\\text{{Current values}} &= [{', '.join(map(str, self.values))}, {self.enq_1}] \\\\"
            f"\\text{{2. dequeue():}} & \\\\"
            f"\\text{{Remove the front element }} ({self.values[0]}) \\text{{ from the queue.}} & \\\\"
            f"\\text{{Current values}} &= [{', '.join(map(str, self.values[1:]))}, {self.enq_1}] \\\\"
            f"\\text{{3. enqueue({self.enq_2}):}} & \\\\"
            f"\\text{{Add }} {self.enq_2} \\text{{ to the rear of the queue.}} & \\\\"
            f"\\text{{Final values}} &= [{', '.join(map(str, self.values[1:]))}, {self.enq_1}, {self.enq_2}] \\\\"
            f"\\text{{4. Calculate the final sum:}} & \\\\"
            f"\\text{{Sum}} &= " + " + ".join(map(str, self.values[1:])) + f" + {self.enq_1} + {self.enq_2} \\\\"
            f"&= {self.answer} \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(11, 3.2))
        ax.axis("off")

        # Container
        cont_x, cont_y = 0.6, 1.2
        cont_w, cont_h = 12.0, 1.6
        ax.add_patch(
            patches.FancyBboxPatch(
                (cont_x, cont_y),
                cont_w,
                cont_h,
                boxstyle="round,pad=0.2,rounding_size=0.25",
                linewidth=2.2,
                edgecolor="#1b5e20",
                facecolor="#e8f5e9",
            )
        )

        filled = self.filled_length
        front_idx = 0
        rear_idx = filled - 1

        # Title
        ax.text(cont_x + cont_w / 2, cont_y + cont_h + 0.55, "QUEUE", ha="center", va="center", fontsize=16, fontweight="bold", color="#1b5e20")

        # Cells
        cell_w = cont_w / self.queue_max_length
        cell_h = 1.0
        cell_y = cont_y + (cont_h - cell_h) / 2

        for i in range(self.queue_max_length):
            cell_x = cont_x + i * cell_w

            is_filled = i < filled
            ax.add_patch(
                patches.Rectangle((cell_x, cell_y), cell_w, cell_h, linewidth=1.8, edgecolor="#2e7d32", facecolor=("#c8e6c9" if is_filled else "white"))
            )

            if is_filled:
                ax.text(cell_x + cell_w / 2, cell_y + cell_h / 2, str(self.values[i]), ha="center", va="center", fontsize=12, fontweight="bold", color="#1b5e20")

        # FRONT arrow + label (pointing to front cell)
        fx = cont_x + front_idx * cell_w + cell_w / 2
        ax.annotate("Front", xy=(fx, cont_y + cont_h), xytext=(fx, cont_y + cont_h + 0.8), ha="center", va="bottom", fontsize=12, fontweight="bold", color="#1b5e20", arrowprops=dict(arrowstyle="-|>", linewidth=2.5, color="#1b5e20"))

        # REAR arrow + label (pointing to rear cell)
        rx = cont_x + rear_idx * cell_w + cell_w / 2
        ax.annotate("Rear", xy=(rx, cont_y + cont_h), xytext=(rx, cont_y + cont_h + 0.8), ha="center", va="bottom", fontsize=12, fontweight="bold", color="#1b5e20", arrowprops=dict(arrowstyle="-|>", linewidth=2.5, color="#1b5e20"))

        ax.set_xlim(0, 13.5)
        ax.set_ylim(0, 4.0)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com039:

    def __init__(self):
        self.length = 10
        self.data = rnd.sample(range(1000, 2000), self.length)
        order = list(range(self.length))
        rnd.shuffle(order)

        self.ptr = [0] * self.length
        for i in range(self.length - 1):
            self.ptr[order[i]] = order[i + 1]
        self.ptr[order[-1]] = None

        self.nodes = list(zip(self.data, self.ptr))
        self.startptr = order[0]
        self.next_node_ptr = self.ptr[self.startptr]
        self.answer = self.data[self.next_node_ptr]

        self.description = f"A linked list abstract data type (ADT) is to be used to store and organise data. This will be implemented with a 1D array and a start pointer. State the value stored in the node immediately after LinkedList[StartPtr]."
        self.topic = "Data Types and Structures"
        self.subtopic = "Introduction to Abstract Data Types (ADT)"
        self.source = "Adapted from PastPapersCo CAIE A-Level 4.1.2"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial Parameters:}} &\\\\"
            f"\\text{{Start Pointer (StartPtr)}} &= {self.startptr} \\\\"
            f"\\text{{1. Identify the first node:}} &\\\\"
            f"\\text{{Node at index StartPtr}} &= \\text{{LinkedList}}[{self.startptr}] \\\\"
            f"\\text{{Value at index StartPtr}} &= {self.data[self.startptr]} \\\\"
            f"\\text{{Next pointer at index StartPtr}} &= {self.ptr[self.startptr]} \\\\"
            f"\\text{{2. Identify the node immediately after StartPtr:}} &\\\\"
            f"\\text{{Next Node Pointer}} &= \\text{{LinkedList}}[{self.startptr}].\\text{{ptr}} \\\\"
            f"&= {self.next_node_ptr} \\\\"
            f"\\text{{3. Extract value from the identified node:}} &\\\\"
            f"\\text{{Value}} &= \\text{{LinkedList}}[{self.next_node_ptr}].\\text{{data}} \\\\"
            f"&= {self.data[self.next_node_ptr]} \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig_w = max(9, self.length * 1.05)
        fig_h = 3.1
        fig, ax = plt.subplots(figsize=(fig_w, fig_h))
        ax.axis("off")

        left_margin = 1.9
        top_y = 2.0
        cell_w = 1.0
        cell_h = 0.7

        ax.text(0.1, top_y + cell_h + 0.65, f"StartPtr: {self.startptr}", ha="left", va="center", fontsize=14, family="monospace")

        for i in range(self.length):
            x = left_margin + i * cell_w
            ax.text(x + cell_w / 2, top_y + cell_h + 0.15, str(i), ha="center", va="center", fontsize=12, fontweight="bold")

        ax.text(left_margin - 0.25, top_y + cell_h / 2, "Data", ha="right", va="center", fontsize=14, fontweight="bold")
        ax.text(left_margin - 0.25, top_y - cell_h / 2, "Ptr", ha="right", va="center", fontsize=14, fontweight="bold")

        for i in range(self.length):
            x = left_margin + i * cell_w

            # Data row cell
            ax.add_patch(
                patches.Rectangle(
                    (x, top_y), cell_w, cell_h,
                    fill=False, linewidth=1.5, edgecolor="black"
                )
            )
            ax.text(x + cell_w / 2, top_y + cell_h / 2, str(self.data[i]), ha="center", va="center", fontsize=12)

            # Ptr row cell
            ax.add_patch(
                patches.Rectangle(
                    (x, top_y - cell_h), cell_w, cell_h,
                    fill=False, linewidth=1.5, edgecolor="black"
                )
            )
            ptr_val = self.ptr[i]
            ptr_text = "NULL" if ptr_val is None else str(ptr_val)
            ax.text(
                x + cell_w / 2, top_y - cell_h / 2,
                ptr_text,
                ha="center", va="center",
                fontsize=12
            )

        ax.set_xlim(0, left_margin + self.length * cell_w + 1.2)
        ax.set_ylim(0.1, top_y + cell_h + 1.0)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com040:

    def __init__(self):
        self.length = 8
        self.data = rnd.sample(range(500, 900), self.length)
        order = list(range(self.length))
        rnd.shuffle(order)

        self.ptr = [0] * self.length
        for i in range(self.length - 1):
            self.ptr[order[i]] = order[i + 1]
        self.ptr[order[-1]] = None

        self.nodes = list(zip(self.data, self.ptr))
        deletable_positions = list(range(1, len(order) - 1))  # excludes head (0) and tail (last)
        pos = rnd.choice(deletable_positions)
        self.delete_idx = order[pos] 
        self.delete_value = self.data[self.delete_idx]
        self.prev_idx = order[pos - 1]
        self.next_idx = self.ptr[self.delete_idx]

        self.answer = self.next_idx

        self.description = f"The following image is showing an example of linked list. If the node containing {self.delete_value} is deleted from the linked list, what value should be stored in the pointer field of the node immediately before it after the deletion?"
        self.topic = "Data Types and Structures"
        self.subtopic = "Introduction to Abstract Data Types (ADT)"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Identify the node to be deleted:}} &\\\\"
            f"\\text{{Target value to delete}} &= {self.delete_value}\\\\"
            f"\\text{{Index of target node (delete\\_idx)}} &= {self.delete_idx}\\\\"
            f"\\text{{2. Identify the surrounding nodes in the linked list:}} &\\\\"
            f"\\text{{Node immediately before (prev\\_idx)}} &= {self.prev_idx}\\\\"
            f"\\text{{Node immediately after (next\\_idx)}} &= {self.next_idx}\\\\"
            f"\\text{{3. Update the pointer of the preceding node:}} &\\\\"
            f"\\text{{To delete a node, the predecessor's pointer must bypass it:}} &\\\\"
            f"\\text{{New Pointer}} &= \\text{{Pointer of current node to be deleted}}\\\\"
            f"\\text{{New Pointer}} &= \\text{{next\\_idx}}\\\\"
            f"\\text{{New Pointer}} &= {self.answer}\\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Build traversal order starting from the head (which is order[0])
        head_idx = None
        # Find head by finding the node that is never pointed TO (except None)
        pointed_to = {p for p in self.ptr if p is not None}
        for i in range(self.length):
            if i not in pointed_to:
                head_idx = i
                break

        chain = []
        cur = head_idx
        seen = set()
        while cur is not None and cur not in seen:
            seen.add(cur)
            chain.append(cur)
            cur = self.ptr[cur]

        data_color = "#AF9AB2"
        next_color = "#D1C3D3"
        arrow_color = "black"
        text_color = "black"

        n = len(chain)
        fig_w = max(12, 3.4 * n + 3.0)
        fig_h = 2.8
        fig, ax = plt.subplots(figsize=(fig_w, fig_h))
        ax.axis("off")

        node_w = 3.2
        half_w = node_w / 2
        node_h = 1.1
        gap = 1.6
        start_x = 3.0
        y0 = 1.0

        # head ->
        ax.text(0.5, y0 + node_h * 0.55, "head", fontsize=22, fontweight="bold", ha="left", va="center", color="black")
        ax.annotate("", xy=(start_x, y0 + node_h * 0.55), xytext=(2.0, y0 + node_h * 0.55), arrowprops=dict(arrowstyle="->", linewidth=3, color=arrow_color))

        # Draw nodes
        for i, idx in enumerate(chain):
            x = start_x + i * (node_w + gap)
            data_val = self.data[idx]
            next_ptr = self.ptr[idx]

            # Data block
            ax.add_patch(patches.Rectangle((x, y0), half_w, node_h, facecolor=data_color, edgecolor="none"))
            # Next block
            ax.add_patch(patches.Rectangle((x + half_w, y0), half_w, node_h, facecolor=next_color, edgecolor="none"))
            # Node border (single outline around both halves)
            ax.add_patch(patches.Rectangle((x, y0), node_w, node_h, fill=False, edgecolor="black", linewidth=2))

            # Address above node
            ax.text(x + half_w * 0.5, y0 + node_h + 0.4, str(idx), ha="center", va="center", fontsize=20, fontweight="bold", color="black")

            # Data text
            ax.text(x + half_w / 2, y0 + node_h / 2, str(data_val), ha="center", va="center", fontsize=20, fontweight="bold", color=text_color)

            # Next pointer text, show NULL for None
            ax.text(x + half_w + (half_w / 2), y0 + node_h / 2, "NULL" if next_ptr is None else str(next_ptr), ha="center", va="center", fontsize=20, fontweight="bold", color=text_color)

            # "data" label under left half
            ax.text(x + half_w / 2, y0 - 0.35, "data", ha="center", va="center", fontsize=18, fontweight="bold", color=text_color)

            # Arrow to next node (except last)
            if i < n - 1:
                ax.annotate(
                    "",
                    xy=(x + node_w + gap - 0.15, y0 + node_h * 0.55),
                    xytext=(x + node_w + 0.15, y0 + node_h * 0.55),
                    arrowprops=dict(arrowstyle="->", linewidth=3, color=arrow_color),
                )

        ax.set_xlim(0, start_x + n * (node_w + gap) + 0.8)
        ax.set_ylim(0, 2.8)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com041:

    def __init__(self):
        self.vowels = ["a", "e", "i", "o", "u"]
        self.num_char = rnd.randint(5, 8)
        self.input = "".join([rnd.choice(["a", "e", "i", "o", "u", "b", "c", "g"]) * rnd.randint(3, 8) for _ in range(self.num_char)])
        max_run = 0
        current_run = 0
        prev_char = ""
        steps = []
        for idx, char in enumerate(self.input, start=1):
            prev_before = prev_char
            is_vowel = char in self.vowels
            same_as_prev = (char == prev_char)

            if is_vowel:
                if same_as_prev:
                    current_run += 1
                else:
                    current_run = 1

                if current_run > max_run:
                    max_run = current_run
            else:
                current_run = 0

            prev_char = char
            steps.append((idx, char, prev_before, is_vowel, same_as_prev, current_run, max_run))

        self.answer = max_run

        self.description = f"A Python code snippet is shown in this image. What will longest_run(\"{self.input}\") return?"
        self.topic = "Programming"
        self.subtopic = "Structured Programming"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given string}}\\; s &= \\texttt{{\"{self.input}\"}}\\\\"
            f"\\text{{Vowels set}}\\; V &= \\{{a,e,i,o,u\\}}\\\\"
            f"\\text{{Initialize}}\\; \\text{{current\\_run}} &= 0,\\; \\text{{max\\_run}} = 0,\\; \\text{{prev}} = \\texttt{{\"\"}}\\\\"
            f"\\text{{Update rules per character }} c:\\; &\\\\"
            f"\\quad c\\in V\\ \\land\\ c=\\text{{prev}}\\Rightarrow \\text{{current\\_run}}\\leftarrow \\text{{current\\_run}}+1\\\\"
            f"\\quad c\\in V\\ \\land\\ c\\neq\\text{{prev}}\\Rightarrow \\text{{current\\_run}}\\leftarrow 1\\\\"
            f"\\quad c\\notin V\\Rightarrow \\text{{current\\_run}}\\leftarrow 0\\\\"
            f"\\quad \\text{{max\\_run}}\\leftarrow \\max(\\text{{max\\_run}},\\text{{current\\_run}})\\\\"
            f"\\text{{Now scan left-to-right and count:}}\\\\"
            + "".join(
                f"{idx}:\\; c=\\texttt{{\"{ch}\"}},\\; \\text{{prev}}=\\texttt{{\"{prev}\"}}"
                f" &\\Rightarrow\\; "
                + (
                    f"c\\in V,\\; c=\\text{{prev}}\\Rightarrow \\text{{current\\_run}}\\leftarrow \\text{{current\\_run}}+1"
                    if is_vowel and same_as_prev
                    else f"c\\in V,\\; c\\neq\\text{{prev}}\\Rightarrow \\text{{current\\_run}}\\leftarrow 1"
                    if is_vowel and (not same_as_prev)
                    else f"c\\notin V\\Rightarrow \\text{{current\\_run}}\\leftarrow 0"
                )
                + (
                    f",\\; \\text{{max\\_run}}\\leftarrow \\max(\\text{{max\\_run}},\\text{{current\\_run}})"
                    if is_vowel
                    else ",\\; \\text{{max\\_run}}\\text{ unchanged}"
                )
                + f",\\; \\text{{current\\_run}}={round(float(cur_after),10)},\\; \\text{{max\\_run}}={round(float(max_after),10)}\\\\"
                for (idx, ch, prev, is_vowel, same_as_prev, cur_after, max_after) in steps
            )
            + f"\\text{{Final longest identical-vowel run}}\\; \\text{{max\\_run}} &= {self.answer}\\\\"
            f"\\text{{Therefore}}\\; \\texttt{{longest\\_run}}(s) &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com041temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com042:

    def __init__(self):
        self.input = rnd.randint(6, 30)
        # func2
        if self.input % 3 == 0:
            self.res2 = self.input * 2 + 5
        else:
            self.res2 = self.input * 3 - (self.input % 4)
        
        # func1
        self.res1 = self.res2 * self.res2 - 4 * self.res2
        if self.res1 % 2 == 0:
            self.res1 += self.res1 % 5
        else:
            self.res1 -= 3 * (self.res1 % 3)

        self.answer = self.res1

        self.description = f"Observe this image below. Let inp be an integer. If the function call func1(func2(inp)) is made where inp is {self.input}, what value will be printed out?"
        self.topic = "Programming"
        self.subtopic = "Structured Programming"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Evaluate inner function:}} &\\ \\text{{func2(inp) where inp}} = {self.input} \\\\"
            f"\\text{{Check condition:}} &\\ {self.input} \\pmod{{3}} = {self.input % 3} \\\\"
            + (
                f"\\text{{Since }} {self.input} \\pmod{{3}} = 0: & \\\\"
                f"res_2 &= (inp \\times 2) + 5 \\\\"
                f"&= ({self.input} \\times 2) + 5 \\\\"
                f"&= {self.res2}"
                if self.input % 3 == 0 else
                f"\\text{{Since }} {self.input} \\pmod{{3}} \\neq 0: & \\\\"
                f"res_2 &= (inp \\times 3) - (inp \\pmod{{4}}) \\\\"
                f"&= ({self.input} \\times 3) - ({self.input % 4}) \\\\"
                f"&= {self.res2}"
            ) + " \\\\"
            f"\\text{{2. Evaluate outer function:}} &\\ \\text{{func1(res\\_2) where res\\_2}} = {self.res2} \\\\"
            f"\\text{{Initial }} res\\_1 \\text{{ calculation:}} & \\\\"
            f"res_1 &= (res_2)^2 - (4 \\times res_2) \\\\"
            f"&= ({self.res2})^2 - (4 \\times {self.res2}) \\\\"
            f"&= {self.res2**2} - {4 * self.res2} \\\\"
            f"&= {self.res2**2 - 4 * self.res2} \\\\"
            f"\\text{{Check }} res\\_1 \\text{{ parity:}} &\\ {self.res2**2 - 4 * self.res2} \\pmod{{2}} = {(self.res2**2 - 4 * self.res2) % 2} \\\\"
            + (
                f"\\text{{Since }} res\\_1 \\text{{ is even:}} & \\\\"
                f"res_1 &= res_1 + (res_1 \\pmod{{5}}) \\\\"
                f"&= {self.res2**2 - 4 * self.res2} + ({(self.res2**2 - 4 * self.res2) % 5}) \\\\"
                f"&= {self.answer}"
                if (self.res2**2 - 4 * self.res2) % 2 == 0 else
                f"\\text{{Since }} res\\_1 \\text{{ is odd:}} & \\\\"
                f"res_1 &= res_1 - (3 \\times (res_1 \\pmod{{3}})) \\\\"
                f"&= {self.res2**2 - 4 * self.res2} - (3 \\times {(self.res2**2 - 4 * self.res2) % 3}) \\\\"
                f"&= {self.answer}"
            ) + " \\\\"
            f"\\text{{Final Output}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com042temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com043:

    def __init__(self):
        self.x = rnd.randint(1, 23)
        self.x_copy = self.x
        steps = []
        k = 0

        while True:
            x_before = self.x
            parity = x_before % 2

            if parity == 0:
                self.x = self.x + 5
            else:
                self.x = self.x * 2 + 1

            x_after = self.x
            k += 1
            steps.append((k, x_before, parity, x_after))

            if self.x > 20:
                break

        self.answer = self.x

        self.description = f"A pseudocode is provided in the image below. What value is output at the end?"
        self.topic = "Programming"
        self.subtopic = "Structured Programming"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial value}}\\; x_0 &= {self.x_copy}\\\\"
            f"\\text{{Update rule (UpdateX):}}\\; x_{{k+1}} &= \\begin{{cases}}"
            f"x_k + 5, & x_k\\equiv 0\\pmod{{2}}\\\\"
            f"2x_k + 1, & x_k\\equiv 1\\pmod{{2}}"
            f"\\end{{cases}}\\\\"
            f"\\text{{Repeat until }} x_k &> 20\\\\"
            f"\\text{{Step-by-step updates:}}\\\\"
            + "".join(
                (
                    f"\\text{{Step {k}:}}\\; x_{{{k-1}}} &= {x_before}\\\\"
                    + f"x_{{{k-1}}}\\bmod 2 &= {parity}\\\\"
                    + (
                        f"\\text{{Since }} x_{{{k-1}}}\\equiv 0\\pmod{{2}},\\; x_{{{k}}} &= x_{{{k-1}}} + 5\\\\"
                        f"&= {x_before} + 5\\\\"
                        f"&= {x_after}\\\\"
                        if parity == 0
                        else
                        f"\\text{{Since }} x_{{{k-1}}}\\equiv 1\\pmod{{2}},\\; x_{{{k}}} &= 2x_{{{k-1}}} + 1\\\\"
                        f"&= 2\\big({x_before}\\big) + 1\\\\"
                        f"&= {x_after}\\\\"
                    )
                    + (
                        f"\\text{{Check stop:}}\\; x_{{{k}}} > 20\\;?\\; &\\Rightarrow\\; \\text{{Yes}}\\\\"
                        if x_after > 20
                        else
                        f"\\text{{Check stop:}}\\; x_{{{k}}} > 20\\;?\\; &\\Rightarrow\\; \\text{{No}}\\\\"
                    )
                )
                for (k, x_before, parity, x_after) in steps
            )
            + f"\\text{{Final output}}\\; x &= {self.answer}\\\\"
            + "\\end{aligned}\\]"
        )

    def generate(self, num):
        pseudocode = [
            "1  DECLARE x : INTEGER",
            f"2  x ← {self.x_copy}",
            "3",
            "4  REPEAT",
            "5      CALL UpdateX(VAR x)",
            "6  UNTIL x > 20",
            "7",
            "8  OUTPUT x",
            "9",
            "10  PROCEDURE UpdateX(VAR n : INTEGER)",
            "11      IF n MOD 2 = 0 THEN",
            "12          n ← n + 5",
            "13     ELSE",
            "14         n ← n * 2 + 1",
            "15     ENDIF",
            "16 ENDPROCEDURE"
        ]
        
        fig, ax = plt.subplots(figsize=(6, 7))
        plt.axis('off')
        
        y_pos = 0.95
        line_height = 0.08
                
        for line in pseudocode:
            color = 'black'
            weight = 'normal'
            
            ax.text(0.05, y_pos, line, 
                    fontsize=14, 
                    family='monospace', 
                    verticalalignment='top', 
                    color=color, 
                    weight=weight)
            
            y_pos -= line_height

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com044:

    def __init__(self):
        cols_AB = ["00", "01", "11", "10"]
        rows_CD = ["00", "01", "11", "10"]
        literals = {"A":1, "B":2, "C":3, "D":4, "A_bar":5, "B_bar":6, "C_bar":7, "D_bar":8}
        self.kmap = [
            [rnd.choice([0, 1]) for _ in range(4)],
            [rnd.choice([0, 1]) for _ in range(4)],
            [rnd.choice([0, 1]) for _ in range(4)],
            [rnd.choice([0, 1]) for _ in range(4)],
        ]
        ones = [
            (r, c)
            for r in range(4)
            for c in range(4)
            if self.kmap[r][c] == 1
        ]
        self.shaded_cell_row, self.shaded_cell_col = rnd.choice(ones)
        self.shaded_cell_value = self.kmap[self.shaded_cell_row][self.shaded_cell_col]

        self.shaded_cell_CD = rows_CD[self.shaded_cell_row]
        self.shaded_cell_AB = cols_AB[self.shaded_cell_col]

        self.A = int(self.shaded_cell_AB[0])
        self.B = int(self.shaded_cell_AB[1])
        self.C = int(self.shaded_cell_CD[0])
        self.D = int(self.shaded_cell_CD[1])

        self.result = []
        self.result.append("A" if self.A == 1 else "A_bar")
        self.result.append("B" if self.B == 1 else "B_bar")
        self.result.append("C" if self.C == 1 else "C_bar")
        self.result.append("D" if self.D == 1 else "D_bar")

        self.result_converted = [str(literals[name]) for name in self.result]
        self.answer = int("".join(self.result_converted))

        self.description = f"What is the Boolean expression that can be obtained for the Karnaugh map cell indicated in the given image? Form the answer using the following encoding rule: A = 1, B = 2, C = 3, D = 4, Ā = 5, B̄ = 6, C̄ = 7, D̄ = 8. Concatenate the digits in the order A, B, C, D to form the final numeric answer."
        self.topic = "Hardware and Virtual Machines"
        self.subtopic = "Boolean Algebra and Logic Circuits"
        self.source = "Adapted from Learnabout electronics (Module 2.5 Digital Logic Quiz)"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Identify coordinates of the shaded cell:}} &\\\\"
            f"\\text{{Column (AB)}} &= {self.shaded_cell_AB}\\\\"
            f"\\text{{Row (CD)}} &= {self.shaded_cell_CD}\\\\"
            f"\\text{{2. Extract Boolean values:}} &\\\\"
            f"A &= {self.A}, \\quad B = {self.B}, \\quad C = {self.C}, \\quad D = {self.D}\\\\"
            f"\\text{{3. Determine literals and encoding:}} &\\\\"
            f"\\text{{Variable A is }} {self.A} &\\rightarrow {'A (1)' if self.A == 1 else 'NOT A (5)'}\\\\"
            f"\\text{{Variable B is }} {self.B} &\\rightarrow {'B (2)' if self.B == 1 else 'NOT B (6)'}\\\\"
            f"\\text{{Variable C is }} {self.C} &\\rightarrow {'C (3)' if self.C == 1 else 'NOT C (7)'}\\\\"
            f"\\text{{Variable D is }} {self.D} &\\rightarrow {'D (4)' if self.D == 1 else 'NOT D (8)'}\\\\"
            f"\\text{{4. Concatenate encoded digits:}} &\\\\"
            f"\\text{{Sequence}} &= {self.result_converted[0]}, {self.result_converted[1]}, {self.result_converted[2]}, {self.result_converted[3]}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        cols_AB = ["00", "01", "11", "10"]
        rows_CD = ["00", "01", "11", "10"]

        fig, ax = plt.subplots(figsize=(5.2, 4.2))
        ax.set_xlim(-0.75, 4)
        ax.set_ylim(0, 4.65)
        ax.set_aspect("equal")
        ax.axis("off")

        for r in range(4):
            for c in range(4):
                x = c
                y = 3 - r  # Row 0 appears at top

                if r == self.shaded_cell_row and c == self.shaded_cell_col:
                    ax.add_patch(patches.Rectangle((x, y), 1, 1, facecolor="#5B7BC0", edgecolor="none"))

                ax.add_patch(patches.Rectangle((x, y), 1, 1, fill=False, linewidth=2.6, edgecolor="#5B7BC0"))
                ax.text(x + 0.5, y + 0.5, str(self.kmap[r][c]), ha="center", va="center", fontsize=16)

        ax.add_patch(patches.Rectangle((0, 0), 4, 4, fill=False, linewidth=3.2, edgecolor = "#5B7BC0"))

        for c, lab in enumerate(cols_AB):
            ax.text(c + 0.5, 4.12, lab, ha="center", va="bottom", fontsize=12)

        for r, lab in enumerate(rows_CD):
            ax.text(-0.12, 3 - r + 0.5, lab, ha="right", va="center", fontsize=12)

        ax.text(0.05, 4.42, "AB", ha="left", va="bottom", fontsize=14, color="black")
        ax.text(-0.65, 3.95, "CD", ha="left", va="center", fontsize=14, color="black")

        fig.tight_layout(pad=0.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close(fig)

class Com045:

    def __init__(self):
        self.heuristic = {"A":5, "B":6, "C":4, "D":3, "E":3, "F":1, "G":0} 
        self.start_node = "A"
        self.goal_node = "G"
        self.AB_cost = rnd.randint(1, 5)
        self.AC_cost = rnd.randint(1, 5)
        self.BC_cost = rnd.randint(1, 5)
        self.BD_cost = rnd.randint(1, 5)
        self.DF_cost = rnd.randint(1, 5)
        self.DG_cost = rnd.randint(1, 5)
        self.FG_cost = rnd.randint(1, 5)
        self.CE_cost = rnd.randint(1, 5)
        self.EG_cost = rnd.randint(1, 5)

        self.graph = {
            "A": {"B": self.AB_cost, "C": self.AC_cost},
            "B": {"C": self.BC_cost, "D": self.BD_cost},
            "C": {"E": self.CE_cost},
            "D": {"F": self.DF_cost, "G": self.DG_cost},
            "E": {"G": self.EG_cost},
            "F": {"G": self.FG_cost},
            "G": {},
        }

        G_SCORE = 0
        F_SCORE = 1
        PREVIOUS = 2

        self.steps = []
        visited = {}
        unvisited = {}

        # Init all nodes
        for node in self.graph:
            unvisited[node] = [sys.maxsize, sys.maxsize, None]

        start = self.start_node
        goal = self.goal_node

        unvisited[start][G_SCORE] = 0
        unvisited[start][F_SCORE] = self.heuristic[start]
        unvisited[start][PREVIOUS] = None

        self.steps.append({
            "event": "init",
            "start": start,
            "goal": goal,
            "open_init": {n: unvisited[n][:] for n in unvisited},
        })

        while True:
            current = get_minimum_fscore(unvisited)
            cur_g, cur_f, cur_prev = unvisited[current]

            self.steps.append({
                "event": "select_min",
                "current": current,
                "g": cur_g,
                "h": self.heuristic.get(current, 0),
                "f": cur_f,
                "open_size": len(unvisited),
            })

            # Goal reached
            if current == goal:
                visited[current] = unvisited[current]
                self.steps.append({
                    "event": "goal_reached",
                    "node": current,
                    "final_cost": cur_g,
                })
                break

            # Expand neighbors
            neighbors = self.graph[current]
            self.steps.append({
                "event": "expand",
                "node": current,
                "neighbors": {k: neighbors[k] for k in neighbors},
            })

            for nb, w in neighbors.items():
                # Skip if already finalized
                if nb in visited:
                    self.steps.append({
                        "event": "skip_neighbor",
                        "from": current,
                        "to": nb,
                        "reason": "already_visited",
                    })
                    continue

                tentative_g = cur_g + w
                old_g = unvisited[nb][G_SCORE]

                self.steps.append({
                    "event": "consider_edge",
                    "from": current,
                    "to": nb,
                    "w": w,
                    "tentative_g": tentative_g,
                    "old_g": old_g,
                })

                if tentative_g < old_g:
                    unvisited[nb][G_SCORE] = tentative_g
                    unvisited[nb][F_SCORE] = tentative_g + self.heuristic[nb]
                    unvisited[nb][PREVIOUS] = current

                    self.steps.append({
                        "event": "update",
                        "node": nb,
                        "new_g": unvisited[nb][G_SCORE],
                        "new_h": self.heuristic[nb],
                        "new_f": unvisited[nb][F_SCORE],
                        "previous": current,
                    })
                else:
                    self.steps.append({
                        "event": "no_update",
                        "node": nb,
                        "reason": "tentative_g_not_better",
                    })

            visited[current] = unvisited[current]
            del unvisited[current]

            self.steps.append({
                "event": "close",
                "node": current,
                "closed_g": visited[current][G_SCORE],
                "closed_f": visited[current][F_SCORE],
                "remaining_open": len(unvisited),
            })

        # Reconstruct route + store outputs
        if goal in visited:
            self.answer = visited[goal][G_SCORE]

            route = []
            cur = goal
            while cur is not None:
                route.append(cur)
                cur = visited[cur][PREVIOUS]

            route.reverse()
            self.shortest_route = route

            self.steps.append({
                "event": "reconstruct",
                "route": list(self.shortest_route),
                "answer": self.answer,
            })
        
        self.description = f"Given a directed weighted graph with heuristic estimates for each node, use the A* search algorithm to find the shortest/minimum cost from node {self.start_node} to node {self.goal_node}. The table underneath the graph provides the estimated distance from the nodes to the target node."
        self.topic = "Artificial Intelligence (AI)"
        self.subtopic = "Artificial Intelligence (AI)"
        self.source = "Adapted from Mahesh Huddar (Youtube)"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Heuristic:}} & \\\\"
            f"\\text{{A:5, B:6, C:4, D:3, E:3, F:1, G:0}} & \\\\"
            f"\\text{{1. Initialization:}} & \\\\"
            f"\\text{{Start Node: }} {self.start_node}, \\text{{ Goal Node: }} {self.goal_node} \\\\"
            f"g({self.start_node}) &= 0, \\quad h({self.start_node}) = {self.heuristic[self.start_node]} \\\\"
            f"f({self.start_node}) &= g({self.start_node}) + h({self.start_node}) = 0 + {self.heuristic[self.start_node]} = {self.heuristic[self.start_node]} \\\\"
            "\\text{{2. A* Search Process (Iterative expansion):}} & \\\\"
            "\\text{{We select the node with the lowest }} f(n) = g(n) + h(n) \\text{{ to expand.}} \\\\"
            "\\text{{Step-by-step trace:}} & \\\\"
        )
        search_trace = ""
        for step in self.steps:
            if step["event"] == "select_min":
                search_trace += f"\\\\\\text{{Expand {step['current']}: }} g={step['g']}, h={step['h']} \\rightarrow f={step['f']} \\\\"
            elif step["event"] == "update":
                search_trace += f"\\quad \\rightarrow \\text{{Update neighbor {step['node']}: }} g={step['new_g']}, f={step['new_g']}+{step['new_h']}={step['new_f']} \\\\"
            elif step["event"] == "goal_reached":
                search_trace += f"\\\\\\text{{Goal reached: }} {step['node']} \\text{{ with total cost }} g = {step['final_cost']} \\\\"
        self.reasoning += (
            search_trace +
            "\\text{{3. Route Reconstruction:}} & \\\\"
            f"\\text{{Path: }} " + " \\rightarrow ".join(self.shortest_route) + " \\\\"
            f"\\text{{Final minimum cost}} &= {self.answer} \\\\"
            f"\\text{{Final Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com045temp.png').convert('RGB')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(268, 119, self.AB_cost, fontsize=10, color='red')
        ax.text(260, 330, self.AC_cost, fontsize=10, color='red')
        ax.text(430, 212, self.BC_cost, fontsize=10, color='red')
        ax.text(529, 54, self.BD_cost, fontsize=10, color='red')
        ax.text(532, 405, self.CE_cost, fontsize=10, color='red')
        ax.text(806, 405, self.EG_cost, fontsize=10, color='red')
        ax.text(819, 200, self.DG_cost, fontsize=10, color='red')
        ax.text(797, 54, self.DF_cost, fontsize=10, color='red')
        ax.text(961, 212, self.FG_cost, fontsize=10, color='red')
        plt.axis('off')

        x0, x1 = 112, 1122
        y0, y1 = 450, 550
        width = x1 - x0
        height = y1 - y0

        keys = list(self.heuristic.keys())
        vals = [self.heuristic[k] for k in keys]
        n = len(keys)

        cell_w = width / n
        row_h = height / 2

        ax.add_patch(patches.Rectangle((x0, y0), width, height, fill=False, edgecolor='black', linewidth=2))

        for i, k in enumerate(keys):
            cx = x0 + i * cell_w

            # Top cell (header)
            ax.add_patch(patches.Rectangle((cx, y0), cell_w, row_h, fill=False, facecolor='white', edgecolor='black', linewidth=1.4))
            ax.text(cx + cell_w/2, y0 + row_h/2, k, ha='center', va='center', fontsize=8, color='black')

            # Bottom cell (value)
            ax.add_patch(patches.Rectangle((cx, y0 + row_h), cell_w, row_h, fill=False, facecolor='white', edgecolor='black', linewidth=1.4))
            ax.text(cx + cell_w/2, y0 + row_h + row_h/2, str(vals[i]), ha='center', va='center', fontsize=8, color='red')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", transparent=True)
        plt.close()

class Com046:

    def __init__(self):
        self.nodes = ["A", "B", "C", "D", "E"]
        self.start = rnd.choice(self.nodes)
        self.goal = rnd.choice([n for n in self.nodes if n != self.start])
        self.AB = rnd.randint(1, 8)
        self.AE = rnd.randint(1, 8)
        self.BE = rnd.randint(1, 8)
        self.BC = rnd.randint(1, 8)
        self.CD = rnd.randint(1, 8)
        self.ED = rnd.randint(1, 8)
        self.EC = rnd.randint(1, 8)
        self.graph = {
            "A": {"B": self.AB, "E": self.AE},
            "B": {"A": self.AB, "E": self.BE, "C": self.BC},
            "C": {"B": self.BC, "D": self.CD, "E": self.EC},
            "D": {"C": self.CD, "E": self.ED},
            "E": {"A": self.AE, "B": self.BE, "C": self.EC, "D": self.ED},
        }

        INF = float("inf")
        dist = {n: INF for n in self.nodes}
        prev = {n: None for n in self.nodes}
        visited = set()

        self.steps = []

        dist[self.start] = 0
        self.steps.append(("init", self.start, self.goal, dict(dist)))

        while len(visited) < len(self.nodes):
            # Pick the unvisited node with the smallest tentative distance
            u = None
            best = INF
            for n in self.nodes:
                if n not in visited and dist[n] < best:
                    best = dist[n]
                    u = n

            if u is None:
                self.steps.append(("stop_unreachable", dict(dist), set(visited)))
                break

            self.steps.append(("select", u, dist[u], set(visited), dict(dist)))

            if u == self.goal:
                self.steps.append(("stop_goal_selected", u, dist[u]))
                break

            visited.add(u)
            self.steps.append(("finalize", u, set(visited)))

            for v, w in self.graph[u].items():
                if v in visited:
                    self.steps.append(("skip_relax", u, v, w, "visited"))
                    continue

                old = dist[v]
                cand = dist[u] + w
                updated = cand < old

                self.steps.append(("relax_try", u, v, w, old, cand, updated))

                if updated:
                    dist[v] = cand
                    prev[v] = u
                    self.steps.append(("relax_apply", v, dist[v], prev[v], dict(dist), dict(prev)))

        if dist[self.goal] == INF:
            self.answer = None
            self.shortest_route = []
        else:
            self.answer = dist[self.goal]
            path = []
            cur = self.goal
            while cur is not None:
                path.append(cur)
                cur = prev[cur]
            self.shortest_route = list(reversed(path))

        self.steps.append(("final", self.answer, self.shortest_route, dict(dist), dict(prev)))

        self.description = f"Given an undirected weighted graph, use the Dijkstra algorithm to find the shortest length from node {self.start} to node {self.goal}."
        self.topic = "Artificial Intelligence (AI)"
        self.subtopic = "Artificial Intelligence (AI)"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Initialize Dijkstra's Algorithm:}} &\\\\"
            f"\\text{{Start Node: }} {self.start},\\; \\text{{Goal Node: }} {self.goal} \\\\"
            f"\\text{{Initialize distances:}} &\\\\"
            f"d({self.start}) &= 0 \\\\"
            f"d(v) &= \\infty \\quad \\text{{for all }} v \\neq {self.start} \\\\"
            f"\\text{{Initialize predecessor map:}} &\\\\"
            f"\\text{{prev}}(v) &= \\text{{None}} \\quad \\text{{for all nodes}} \\\\"
            f"\\text{{Initialize visited set:}} &\\\\"
            f"\\text{{visited}} &= \\emptyset \\\\"
            f"\\text{{2. Iterative Selection and Relaxation:}} &\\\\"
            + " \\\\ ".join([
                (
                    f"\\text{{Select node }} {s[1]} \\text{{ with minimum tentative distance: }} d({s[1]}) = {round(s[2], 10) if isinstance(s[2], (int, float)) else s[2]}"
                    if s[0] == "select" else
                    f"\\text{{Finalize node }} {s[1]}:\\; \\text{{visited}} \\leftarrow \\text{{visited}} \\cup \\{{{s[1]}\\}}"
                    if s[0] == "finalize" else
                    f"\\quad \\text{{Skip edge }}({s[1]},{s[2]})\\text{{ (neighbor already visited)}}"
                    if s[0] == "skip_relax" else
                    (
                        f"\\quad \\text{{Relax }}({s[1]},{s[2]})\\text{{ with }} w={s[3]}:\\; "
                        f"\\text{{candidate}} = d({s[1]}) + w = {round(s[5]-s[3],10)} + {s[3]} = {round(s[5],10)},\\; "
                        f"\\text{{current}}\\; d({s[2]}) = "
                        + (f"{round(s[4],10)}" if s[4] != float('inf') else "\\infty")
                        + "\\;\\Rightarrow\\; \\text{{update}}"
                        if s[0] == "relax_try" and s[6] else
                        f"\\quad \\text{{Relax }}({s[1]},{s[2]})\\text{{ with }} w={s[3]}:\\; "
                        f"\\text{{candidate}} = d({s[1]}) + w = {round(s[5]-s[3],10)} + {s[3]} = {round(s[5],10)},\\; "
                        f"\\text{{current}}\\; d({s[2]}) = "
                        + (f"{round(s[4],10)}" if s[4] != float('inf') else "\\infty")
                        + "\\;\\Rightarrow\\; \\text{{no update}}"
                        if s[0] == "relax_try" and (not s[6]) else
                        f"\\quad d({s[1]}) \\leftarrow {round(s[2],10)},\\; \\text{{prev}}({s[1]}) \\leftarrow {s[3]}"
                        if s[0] == "relax_apply" else
                        f"\\text{{Goal node selected; shortest distance finalized.}}"
                        if s[0] == "stop_goal_selected" else
                        f"\\text{{No more reachable unvisited nodes; stop.}}"
                        if s[0] == "stop_unreachable" else
                        f""
                    )
                )
                for s in self.steps
                if s[0] not in ["init", "final"] and (s[0] != "relax_apply" or True)
            ]) + " \\\\ "
            + (
                f"\\text{{3. Final Path Reconstruction:}} &\\\\"
                + (
                    f"\\text{{Shortest path: }} " + " \\rightarrow ".join(self.shortest_route) + " \\\\"
                    f"d({self.goal}) &= {self.answer} \\\\"
                    f"\\text{{Final Result}} &= {self.answer}"
                    if self.answer is not None else
                    f"\\text{{No path exists from }} {self.start} \\text{{ to }} {self.goal} \\\\"
                    f"\\text{{Final Result}} &= \\text{{None}}"
                )
            )
            + "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com046temp.png').convert('RGB')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(374, 197, self.AB, fontsize=10, color='black')
        ax.text(348, 430, self.AE, fontsize=10, color='black')
        ax.text(463, 312, self.BE, fontsize=10, color='black')
        ax.text(615, 114, self.BC, fontsize=10, color='black')
        ax.text(766, 312, self.CD, fontsize=10, color='black') 
        ax.text(607, 527, self.ED, fontsize=10, color='black')
        ax.text(585, 287, self.EC, fontsize=10, color='black')
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", transparent=True)
        plt.close()