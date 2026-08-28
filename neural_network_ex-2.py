#y=3x+2

x=4
target=14

w=0.5
b=0
learning_rate=0.001


for i in range(30):
    z=w*x+b
    loss=(z-target)**2
    grad_w= 2*(z-target)*x
    grad_b= 2*(z-target)
    w= w- learning_rate*grad_w
    b= b- learning_rate*grad_b
    print("weight:", w,", bias:", b,", loss:", loss)
