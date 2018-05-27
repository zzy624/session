# -*-coding:utf-8-*-


def main():

    t = ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
    m = t[0]
    for i in range(len(t)):
        if t[i][2] > m[2]:
            m = t[i]
    print(m[1])

if __name__ == '__main__':
    main()