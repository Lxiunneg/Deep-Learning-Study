
import numpy
# 感知器


def print_table(logicGate):
    temp1 = logicGate(0,0)
    temp2 = logicGate(1,0)
    temp3 = logicGate(0,1)
    temp4 = logicGate(1,1)

    print("\t真值表\t")
    print(f"0\t|0\t|{temp1}|")
    print(f"1\t|0\t|{temp2}|")
    print(f"0\t|1\t|{temp3}|")
    print(f"1\t|1\t|{temp4}|")

# 逻辑 与门
def AND(x1,x2):
    x = numpy.array([x1, x2])
    w = numpy.array([0.5, 0.5])
    b = -0.7
    return 1 if(b + numpy.sum(x*w)) >= 0 else 0 # 三元

def OR(x1,x2):
    x = numpy.array([x1, x2])
    w = numpy.array([0.5, 0.5])
    b = -0.2
    return 1 if (b + numpy.sum(x * w)) >= 0 else 0  # 三元

def NOT(logicGate,x1,x2):
    return 0 if logicGate(x1,x2) == 1 else 1



def XOR(x1,x2):
    x = numpy.array([x1, x2])
    s1 = NOT(AND,x1,x2)
    s2 = OR(x1,x2)

    return AND(s1,s2)

if __name__ == '__main__':
    print_table(AND)
    # print_table(NOT(AND,1,1))
    print_table(OR)
    # print_table(NOT(OR,0,0))
    print_table(XOR)
    # print_table(NOT(XOR,1,1))