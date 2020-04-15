prime = []  # 用一个列表来存储素数
print("功能：找出所有小于等于1000的素数")
for i in range(2, 1000 + 1):  # 1不是素数，range“前闭后开”
    yes = True
    for j in range(2, i):
        if i % j == 0:
            yes = False
            break  # 不是素数
    if yes is True:  # Python的True首字母大写
        prime.append(i)  # 是素数
print(prime)
