x1=3
x2=4


w1=0.5
w2=-0.2

b=1

z=x1*w1 + x2*w2 + b

def ReLU(x):
    return max(0, x)

print(ReLU(z))