import random as rnd
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# target folder : "root/dataset/compsci/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "compsci", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Com051:

    def __init__(self):
        self.num = 7
        self.first_arr = rnd.sample(range(10, 35), self.num)
        self.traces = []
        arr = self.first_arr.copy()
        for i in range(1, len(arr)):
            before = arr.copy()
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            after = arr.copy()

            self.traces.append({
                "pass": i,
                "key": key,
                "before": before,
                "after": after,
                "sorted_prefix_before": before[:i],
                "sorted_prefix_after": after[:i+1],
            })

        X = rnd.randint(1, len(self.traces))
        self.second_arr = self.traces[X - 1]["after"].copy()
        self.answer = X

        self.description = f"Two array are shown in the figure below. The first array is the initial array. The second array is the result of running insertion sort on the first array for X passes. Find X."
        self.topic = "Computational thinking and Problem-solving"
        self.subtopic = "Algorithms"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial Array}} &= [{', '.join(map(str, self.first_arr))}]\\\\"
            f"\\text{{Target Array}} &= [{', '.join(map(str, self.second_arr))}]\\\\"
            "\\text{{Insertion Sort Procedure:}} &\\\\"
            "\\text{{In each pass }} i, \\text{{ the element at index }} i \\text{{ (key) is inserted into the sorted prefix.}} &\\\\"
            + " \\\\ ".join([
                f"\\text{{Pass }} {t['pass']}: \\text{{ Key }} = {t['key']}, \\text{{ Prefix }} {t['before'][:t['pass']]} \\rightarrow \\text{{ Result }} {t['after']}"
                for t in self.traces
            ]) + "\\\\"
            "\\text{{Comparison and Identification:}} &\\\\"
            f"\\text{{The array after Pass }} {self.answer} \\text{{ matches the target array:}} [{', '.join(map(str, self.second_arr))}]&\\\\"
            f"\\text{{Final Result }} (X) &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com051temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        x = 700
        for val1, val2 in zip(self.first_arr, self.second_arr):
            ax.text(x, 435, val1, fontsize=14, color="#272727")
            ax.text(x, 688, val2, fontsize=14, color='#272727')
            x += 158
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Com052:

    def __init__(self):
        self.array = [None, 8, 12, 16, 20, 12, 14, 16, 20, 20, 22] # Starts from index 1
        self.x = 1
        self.trace = []
        # func itik
        def itik_logic(a: int, b:int) -> int:
            if b == 0:
                itik = a
            else:
                itik = itik_logic(b, a % b)
            return itik
        # func bebek
        def bebek_logic(x: int) -> int:
            if x > 10:
                self.trace.append({"x": x, "val": 0, "is_base": True})
                return 0
            
            next_val = bebek_logic(x * 2)
            current_val = self.array[x]
            res = itik_logic(current_val, next_val)
            
            self.trace.append({
                "x": x, 
                "val": res, 
                "array_val": current_val, 
                "next_x": x * 2, 
                "next_val": next_val,
                "is_base": False
            })
            return res
        
        self.answer = bebek_logic(self.x)

        self.description = f"What is the output of the given program, if insert_num is {self.x}?"
        self.topic = "Computational thinking and Problem-solving"
        self.subtopic = "Recursion"
        self.source = "Adapted from Indonesia's National Science Olympiad Selection Test for Informatics at the Regency/City Level 2018"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Input x}} &= {self.x} \\\\"
            f"\\text{{Array (1-based indexing)}} &= {self.array[1:]} \\\\"
            f"\\text{{The function }} itik(a, b) &\\text{{ calculates }} \\gcd(a, b).\\\\"
            f"\\text{{The function }} bebek(x) &\\text{{ is defined recursively:}}\\\\"
            f"bebek(x) &= \\begin{{cases}} 0 & \\text{{if }} x > 10 \\\\ itik(array[x], bebek(2x)) & \\text{{otherwise}} \\end{{cases}}\\\\"
            "\\text{{Evaluation:}} &\\\\"
            + " \\\\ ".join([
                f"\\text{{Base Case: }} bebek({t['x']}) &= {round(float(t['val']), 10)}" if t['is_base']
                else (
                    f"bebek({t['x']}) &= itik(array[{t['x']}], bebek({t['next_x']}))\\\\"
                    f"&= itik({round(float(t['array_val']), 10)}, {round(float(t['next_val']), 10)})\\\\"
                    f"&= {round(float(t['val']), 10)}"
                )
                for t in self.trace
            ])
            + f"\\\\ \\text{{Therefore, the final result is:}} &\\\\"
            + f"\\text{{Output}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('compsci/temp_image/Com052temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()