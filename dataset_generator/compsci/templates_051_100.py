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