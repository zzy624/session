# -*-coding:utf-8-*-

# 去除字典中value重复的项
# {'zhangsan':100, 'lisi':65, 'tianlaoshi':65, 'liulaoshi':99}

def main():
    dic = {'zhangsan':100, 'lisi':65, 'tianlaoshi':65, 'liulaoshi':99}
    b = dic.copy()
    a = []
    for key,value in dic.items():
        if value in a:
            del b[key]
        else:
            a.append(value)
    print(b)

if __name__ == '__main__':
    main()