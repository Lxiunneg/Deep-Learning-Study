import numpy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles


def step_function(x):
    return numpy.array(x>0, dtype=np.int_)

def sigmoid(x):
    return 1/(1+numpy.exp(-x))

def ReLU(x):
    return numpy.maximum(0, x)

def matrix_dot():
    A = numpy.array([[1,2],[3,4]])
    B = numpy.array([[5,6],[7,8]])
    print(A.dot(B))
    print(B.dot(A))


if __name__ == '__main__':
    # x = numpy.arange(-5.0,5.0,0.1)
    # y1 = step_function(x)
    # y2 = sigmoid(x)
    # y3 = ReLU(x)
    # plt.plot(x,y1,linestyle = "--",label="simple")
    # plt.ylim(-0.1,1.1)
    # plt.plot(x,y2,label="sigmoid")
    # plt.plot(x,y3,linestyle = ":",label="ReLU")
    # plt.show()

    matrix_dot()

