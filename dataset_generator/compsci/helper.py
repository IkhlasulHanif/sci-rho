# helper functions 
import random as rnd
import sys

def generate_binary(length, allow_leading_zeros=False):
    bits = [rnd.choice([0, 1]) for _ in range(length)]
    binary_str = "".join(map(str, bits))
    
    if not allow_leading_zeros:
        binary_str = binary_str.lstrip('0')
        # If the string becomes empty (all zeros), reset to "0"
        if not binary_str:
            binary_str = "0"
            
    return binary_str

def get_minimum_fscore(open_dict):
    """Return the node in open_dict with the smallest f-score (tie-break: smaller g, then name)."""
    best_node = None
    best_f = sys.maxsize
    best_g = sys.maxsize
    for n, (g, f, prev) in open_dict.items():
        if (f < best_f) or (f == best_f and g < best_g) or (f == best_f and g == best_g and (best_node is None or n < best_node)):
            best_node = n
            best_f = f
            best_g = g
    return best_node

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None