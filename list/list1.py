# -*-coding:utf-8-*-

def main():
    l = [[1, 'zhangsan', 3000], [2, 'lisi', 2500], [3, 'tiantian', 20000]]
    print(sorted(l,key=lambda x:x[2],reverse=True)[0][1])
    print(sorted(l,cmp=lambda x,y:cmp(x[2],y[2]),reverse=True)[0][1])


if __name__ == '__main__':
    main()