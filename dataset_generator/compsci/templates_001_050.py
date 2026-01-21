import random as rnd
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
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