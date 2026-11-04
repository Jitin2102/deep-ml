import math

def softmax(x):
    m = max(x)
    shifted = [v - m for v in x]
    e = [math.exp(v) for v in shifted]
    return [v / sum(e) for v in e]