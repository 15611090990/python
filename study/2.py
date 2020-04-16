import random
i = int(input("请输入次数",))


def touzi(a):
    for x in range(1, a+1):
        t = random.random()
        # print(t)
        if t < 0.17:
            print(1)
        elif t < 0.33:
            print(2)
        elif t < 0.5:
            print(3)
        elif t < 0.67:
            print(4)
        elif t < 0.83:
            print(5)
        else:
            print(6)


touzi(i)
