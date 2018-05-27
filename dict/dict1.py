# -*-coding:utf-8-*-

# 把字符串 "k1:1|k2:2|k3:3" 处理成字典数据：{'k1':1,'k2';2,'k3':3}

def main():
    s = "k1:1|k2:2|k3:3"
    d = {}
    for i in s.split('|'):
        d[i.split(':')[0]] = i.split(':')[1]
    print(d)

if __name__ == '__main__':
    main()