import random as rnd

# write helper functions here
def randrange_float(start, stop, step):
    """
    Generates a random float number N such that start <= N < stop, 
    with a specific step size.
    """
    num_steps = int((stop - start) / step)
    random_step = rnd.randint(0, num_steps)
    return start + random_step * step

def fmt_time(x, pos=None):
    total_minutes = int(round(x * 60))
    hh = (total_minutes // 60) % 24
    mm = total_minutes % 60
    return f"{hh:02d}:{mm:02d}"

# Helper for clean formatting (prevents "+ -", "1x", or "0x")
def fmt_poly(coeff, var, is_leading=False):
    if coeff == 0: return ""
    sign = "+" if coeff > 0 else "-"
    val = abs(coeff)
    str_val = str(val) if (val != 1 or var == "") else ""
    if is_leading:
        return f"{'' if coeff > 0 else '-'}{str_val}{var}"
    return f" {sign} {str_val}{var}"