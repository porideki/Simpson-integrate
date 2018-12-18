def simpson(bottom, top, span):

    n = (top - bottom) // span
    sections = []

    for i in range((n / 2) - 1):
        sections = (f(bottom + span * 2 * i) + 4 * f(bottom + span * 2 * (i + 1) + f(bottom + span * 2 * (i + 2))))
        
    

def f(x):
    import math
    return math.sin((math.pi * x)/3)