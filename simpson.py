def simpson(bottom, top, span):

        area = 0
        
        for i in range(int((top - bottom) / (span * 2))):
                area += (span / 3) * (f(bottom + span * 2 * i) + 4 * f(bottom + span * (2 * i + 1)) + f(bottom + span * (2 * i + 2)))

        return area

def f(x):
        import math
        return math.sin((math.pi * x) / 3)