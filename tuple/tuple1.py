# -*-coding:utf-8-*-


def main():

    t = ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
    s = 0
    for i in t:
        s = s + i[2]
    arg = s / len(t)
    print(arg)

if __name__ == '__main__':
    main()