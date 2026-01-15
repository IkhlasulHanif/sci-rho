# helper functions 
import random as rnd

def generate_binary(length, allow_leading_zeros=False):
    bits = [rnd.choice([0, 1]) for _ in range(length)]
    binary_str = "".join(map(str, bits))
    
    if not allow_leading_zeros:
        binary_str = binary_str.lstrip('0')
        # If the string becomes empty (all zeros), reset to "0"
        if not binary_str:
            binary_str = "0"
            
    return binary_str