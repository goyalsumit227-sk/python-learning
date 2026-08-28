x=3
target=6

w=0.5
learning_rate=0.01

for i in range(10):
    y_pred=w*x
    loss=(y_pred-target)**2
    grad= 2*(y_pred-target)*x
    w= w-learning_rate*grad
    print("weight:", w,", loss:", loss)
